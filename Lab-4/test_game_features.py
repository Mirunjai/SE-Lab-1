"""Dependency-free logic tests for the Lab 4 game changes."""
import importlib.util
import os
import sys
import tempfile
import types
import unittest
from pathlib import Path

class FakeRect:
    def __init__(self, x, y, width, height):
        self.x, self.y, self.width, self.height = x, y, width, height
    @property
    def left(self): return self.x
    @property
    def right(self): return self.x + self.width
    @property
    def top(self): return self.y
    @property
    def bottom(self): return self.y + self.height
    @bottom.setter
    def bottom(self, value): self.y = value - self.height
    def colliderect(self, other):
        return self.left < other.right and self.right > other.left and self.top < other.bottom and self.bottom > other.top

class FakeSurface:
    def get_rect(self, **kwargs): return types.SimpleNamespace(**kwargs)
class FakeFont:
    def render(self, *_args, **_kwargs): return FakeSurface()

fake_pygame = types.ModuleType("pygame")
fake_pygame.Rect = FakeRect
fake_pygame.font = types.SimpleNamespace(Font=lambda *_args, **_kwargs: FakeFont())
fake_pygame.draw = types.SimpleNamespace(rect=lambda *_args, **_kwargs: None, line=lambda *_args, **_kwargs: None)
sys.modules.setdefault("pygame", fake_pygame)
spec = importlib.util.spec_from_file_location("dino_game_under_test", Path(__file__).with_name("game.py"))
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)

class FakeObstacle:
    def __init__(self, x, y, width=20, height=30, speed=0):
        self.rect, self.speed, self.passed = FakeRect(x, y, width, height), speed, False
    def update(self): self.rect.x -= self.speed
    def is_off_screen(self): return self.rect.right < 0

class DinoRunFeatureTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.old_cwd = os.getcwd()
        os.chdir(self.temp_dir.name)
    def tearDown(self):
        os.chdir(self.old_cwd)
        self.temp_dir.cleanup()
    def test_high_score_updates_only_when_run_is_better(self):
        Path(game.HIGH_SCORE_FILE).write_text("0", encoding="utf-8")
        instance = game.Game()
        instance.state, instance.score, instance.spawn_interval = "play", 120, 99999
        instance.obstacles = [FakeObstacle(82, 280)]
        instance.update()
        self.assertEqual(instance.high_score, 12)
        self.assertEqual(Path(game.HIGH_SCORE_FILE).read_text(encoding="utf-8"), "12")
        instance.state, instance.score = "play", 50
        instance.obstacles = [FakeObstacle(82, 280)]
        instance.update()
        self.assertEqual(instance.high_score, 12)
    def test_dino_ground_and_air_colours(self):
        self.assertEqual(game.dino_tint(True), (83, 141, 78))
        self.assertEqual(game.dino_tint(False), (70, 130, 220))
    def test_obstacle_clear_is_counted_once(self):
        instance = game.Game()
        instance.state, instance.spawn_interval = "play", 99999
        obstacle = FakeObstacle(40, 280)
        instance.obstacles = [obstacle]
        instance.update()
        self.assertTrue(obstacle.passed)
        self.assertEqual(game.COMBO_COUNT, 1)
        self.assertEqual(game.COMBO_POPUP_FRAMES, game.COMBO_POPUP_DURATION)
        instance.update()
        self.assertEqual(game.COMBO_COUNT, 1)
    def test_double_jump_limit(self):
        dino = game.Dino(80, game.GROUND_Y)
        dino.jump()
        dino.jump()
        self.assertEqual(dino.jump_count, 2)
        dino.jump()
        self.assertEqual(dino.jump_count, 2)
    def test_landing_resets_jump_counter(self):
        dino = game.Dino(80, game.GROUND_Y)
        dino.jump()
        dino.rect.bottom = game.GROUND_Y
        dino.vel_y = 0
        dino.update(game.GROUND_Y)
        self.assertEqual(dino.jump_count, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
