# Global Counter (Windows Desktop App)

This is a **desktop counter app** (not a browser app).

## Features

- Always-on-top popup window that shows the current count.
- Global hotkeys:
  - Press `+` to increase the count.
  - Press `-` to decrease the count.
- Hotkeys work even when another window is focused.
- In-app **Reset** button to reset the counter to `0`.

## Run locally

1. Install Python 3.10+ on Windows.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app:
   ```bash
   python app.py
   ```

## Build a Windows `.exe`

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Build:
   ```bash
   pyinstaller --noconfirm --onefile --windowed --name GlobalCounter app.py
   ```
3. Your executable will be in:
   - `dist/GlobalCounter.exe`

## Notes

- On some Windows setups, global key capture may require running the app with sufficient permissions.
- `+` is typically `Shift` + `=` on many keyboards. Both `+` and `-` are supported.
