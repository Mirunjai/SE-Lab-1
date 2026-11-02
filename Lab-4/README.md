# Lab 4 - Dino Run (Vibe Coding)

Assigned starter: https://github.com/SETAPESU26/36_dinoRun

## Completed code tasks
1. Fixed the high-score comparison so the saved best updates only when the current run is higher.
2. Implemented grounded/airborne dino tint (green on the ground, blue in the air).
3. Implemented one-time obstacle clear counting and a brief visible notification.
4. Implemented double jump (two jumps before landing).

## Run
```bash
python -m pip install -r requirements.txt
python game.py
```
Controls: Space, Up Arrow, or W.

## Tests
```bash
python -m unittest -v test_game_features.py
```
The tests use a minimal Pygame stub to verify game logic without an SDL window. This does not replace live-game testing.

## Video evidence - outstanding
The worksheet requires genuine 10-second `before.mp4` and `after.mp4` gameplay recordings. They are not included because this execution environment did not have Pygame installed and could not reach the package index to install it. See `VIDEO_CAPTURE_GUIDE.md` for recording steps. Do not treat mock footage as gameplay evidence.

## Repository boundary
This work belongs to the personal repository. No pull request is made to the SETAPESU26 starter repository.
