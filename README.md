# Guess the Number — Android Python Game

A small Kivy game where Android chooses a random number from 1 to 100. Enter a guess and the app tells you to go **higher** or **lower** until you find it.

## Files
- `main.py` — Android/Kivy user interface.
- `game_logic.py` — game logic.
- `buildozer.spec` — Android packaging configuration.
- `test_game_logic.py` — unit tests.
- `build_apk.sh` — helper script for building a debug APK.

## Run tests
```bash
python3 -m unittest -v test_game_logic.py
```

## Run on desktop
Install Kivy and launch:
```bash
python3 -m pip install kivy
python3 main.py
```

## Build an APK on Linux / WSL2
Buildozer's Android toolchain requires Linux (native Linux or WSL2 works well):
```bash
chmod +x build_apk.sh
./build_apk.sh
```

The generated APK will be placed in the `bin/` directory. Copy it to your Android phone and open it to install. Android may ask you to allow installation from that source.

If Java compatibility errors occur with your system JDK, install JDK 17 and make it active before building.
