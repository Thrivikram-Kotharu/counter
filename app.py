import tkinter as tk
from tkinter import ttk
from pynput import keyboard


class CounterApp:
    def __init__(self) -> None:
        self.count = 0
        self.shift_pressed = False

        self.root = tk.Tk()
        self.root.title("Global Counter")
        self.root.attributes("-topmost", True)
        self.root.resizable(False, False)

        self.root.configure(padx=16, pady=16)

        self.count_var = tk.StringVar(value=str(self.count))

        ttk.Label(self.root, text="Count", font=("Segoe UI", 12)).pack()
        ttk.Label(
            self.root,
            textvariable=self.count_var,
            font=("Segoe UI", 42, "bold"),
            width=6,
            anchor="center",
        ).pack(pady=(4, 12))

        controls = ttk.Frame(self.root)
        controls.pack()

        ttk.Button(controls, text="Reset", command=self.reset_count).pack(side="left", padx=(0, 8))
        ttk.Button(controls, text="+", command=self.increment).pack(side="left", padx=4)
        ttk.Button(controls, text="-", command=self.decrement).pack(side="left", padx=4)

        hint = (
            "Global hotkeys:\n"
            "  + to increase count\n"
            "  - to decrease count\n"
            "Works even when this window is not focused"
        )
        ttk.Label(self.root, text=hint, font=("Segoe UI", 9), justify="left").pack(pady=(12, 0))

        self.listener = keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release)
        self.listener.start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def update_count_display(self) -> None:
        self.count_var.set(str(self.count))

    def increment(self) -> None:
        self.count += 1
        self.update_count_display()

    def decrement(self) -> None:
        self.count -= 1
        self.update_count_display()

    def reset_count(self) -> None:
        self.count = 0
        self.update_count_display()

    def on_key_press(self, key: keyboard.Key | keyboard.KeyCode) -> None:
        if key in (keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r):
            self.shift_pressed = True
            return

        key_char = getattr(key, "char", None)

        if key_char == "+" or (key_char == "=" and self.shift_pressed):
            self.root.after(0, self.increment)
        elif key_char == "-":
            self.root.after(0, self.decrement)

    def on_key_release(self, key: keyboard.Key | keyboard.KeyCode) -> None:
        if key in (keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r):
            self.shift_pressed = False

    def on_close(self) -> None:
        self.listener.stop()
        self.root.destroy()

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    CounterApp().run()
