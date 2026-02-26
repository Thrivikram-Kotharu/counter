# Global Counter (Windows Desktop App)

This is a **desktop counter app** (not a browser app).

## Features

- Always-on-top popup window that shows the current count.
- Global hotkeys:
  - Press `+` to increase the count.
  - Press `-` to decrease the count.
- Hotkeys work even when another window is focused.
- In-app **Reset** button to reset the counter to `0`.

## Install and run on your Windows PC

### Option A (recommended): use the built `.exe`

1. Copy `GlobalCounter.exe` to your PC.
2. Double-click `GlobalCounter.exe` to run.
3. If Windows SmartScreen shows a warning, click:
   - **More info** → **Run anyway**.

> If you do not already have `GlobalCounter.exe`, build it once using **Option B** below.

### Option B: run from Python source

1. Install **Python 3.10+** from: https://www.python.org/downloads/windows/
   - During install, check **Add Python to PATH**.
2. Open **Command Prompt** in the project folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```

## Build the `.exe` yourself (one-time)

1. Open **Command Prompt** in the project folder.
2. Install build tool:
   ```bash
   pip install pyinstaller
   ```
3. Build executable:
   ```bash
   pyinstaller --noconfirm --onefile --windowed --name GlobalCounter app.py
   ```
4. Find output at:
   - `dist\GlobalCounter.exe`

## Optional: run on startup with Windows

1. Press `Win + R`, type `shell:startup`, and press Enter.
2. Put a shortcut to `GlobalCounter.exe` in that Startup folder.

## Troubleshooting

- If `+` does not increase on your keyboard layout, try `Shift` + `=`.
- If hotkeys do not work in some apps, run `GlobalCounter.exe` as Administrator.
- If `pip` is not recognized, reopen Command Prompt and try:
  ```bash
  python -m pip install -r requirements.txt
  ```
