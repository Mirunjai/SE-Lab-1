"""Smart home device controller used for the static-analysis lab."""

import json

HUB_HOST = "127.0.0.1"
HUB_PORT = 8080
POWER_USAGE = {"light": 10, "fan": 60, "thermostat": 1500, "tv": 120}
DEVICES = {}


def add_device(device_name, kind, room="Living Room", settings=None):
    """Add a device without sharing mutable settings between devices."""
    device_settings = {} if settings is None else dict(settings)
    DEVICES[device_name] = {
        "kind": kind,
        "room": room,
        "on": False,
        "settings": device_settings,
    }


def toggle_device(device_name):
    """Toggle a device and return its new state, or None when absent."""
    if device_name in DEVICES:
        DEVICES[device_name]["on"] = not DEVICES[device_name]["on"]
        return DEVICES[device_name]["on"]
    print("Device not found:", device_name)
    return None


def set_temperature(device_name, value):
    """Set a thermostat temperature clamped to the supported range."""
    device = DEVICES.get(device_name)
    if device is None:
        print("Device not found:", device_name)
        return False
    if device["kind"] != "thermostat":
        print(device_name, "is not a thermostat")
        return False
    device["settings"]["temperature"] = min(max(value, 16), 30)
    return True


def devices_in_room(room):
    """Return device names in the requested room."""
    return [name for name, info in DEVICES.items() if info["room"] == room]


def power_usage():
    """Return total power usage for devices currently switched on."""
    active = [info for info in DEVICES.values() if info["on"]]
    return sum(POWER_USAGE.get(info["kind"], 0) for info in active)


def save_state(file_name="home_state.json"):
    """Save the current device state to JSON."""
    with open(file_name, "w", encoding="utf-8") as file_handle:
        json.dump(DEVICES, file_handle, indent=2)


def hub_address():
    """Return the configured hub address."""
    return f"{HUB_HOST}:{HUB_PORT}"


def main():
    """Run the demonstration scenario."""
    add_device("Ceiling Light", "light")
    add_device("Bedroom Fan", "fan", "Bedroom")
    add_device("Thermostat", "thermostat", "Bedroom")
    add_device("Smart TV", "tv")
    toggle_device("Ceiling Light")
    toggle_device("Thermostat")
    toggle_device("Garage Door")
    set_temperature("Thermostat", 35)
    set_temperature("Ceiling Light", 20)
    print("Bedroom devices:", devices_in_room("Bedroom"))
    print("Current power use (W):", power_usage())
    print("Hub address:", hub_address())
    print("Light settings:", DEVICES["Ceiling Light"]["settings"])
    print("Devices on:", [name for name, info in DEVICES.items() if info["on"]])
    save_state()


if __name__ == "__main__":
    main()
