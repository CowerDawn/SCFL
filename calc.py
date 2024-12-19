import tkinter as tk
from tkinter import messagebox
import math
import time

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x550")
        self.root.configure(bg="#f5f5f5")
        self.root.attributes("-alpha", 0.95)

        self.expression_var = tk.StringVar()
        self.expression_var.set("")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_ui()

    def create_ui(self):
        self.display_frame = tk.Frame(self.root, bg="#e0e0e0", highlightbackground="gray", highlightthickness=1)
        self.display_frame.pack(pady=10, fill="both", expand=True)

        self.expression_label = tk.Label(self.display_frame, textvariable=self.expression_var, anchor="e", font=("Arial", 24), bg="#ffffff", fg="#333333", padx=10, pady=10)
        self.expression_label.pack(fill="both", expand=True)

        self.result_label = tk.Label(self.display_frame, textvariable=self.result_var, anchor="e", font=("Arial", 16), bg="#ffffff", fg="#555555", padx=10, pady=5)
        self.result_label.pack(fill="both", expand=True)

        self.buttons_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.buttons_frame.pack(fill="both", expand=True)

        buttons = [
            ("7", "#ffffff"), ("8", "#ffffff"), ("9", "#ffffff"), ("/", "#ff9999"),
            ("4", "#ffffff"), ("5", "#ffffff"), ("6", "#ffffff"), ("*", "#ff9999"),
            ("1", "#ffffff"), ("2", "#ffffff"), ("3", "#ffffff"), ("-", "#ff9999"),
            ("0", "#ffffff"), (".", "#ffffff"), ("=", "#99ff99"), ("+", "#ff9999"),
            ("√", "#cceeff"), ("sin", "#cceeff"), ("cos", "#cceeff"), ("tan", "#cceeff"),
            ("ln", "#cceeff"), ("exp", "#cceeff"), ("!", "#cceeff"), ("C", "#ffcccc")
        ]

        self.buttons = []
        row, col = 1, 0
        for text, color in buttons:
            button = tk.Button(self.buttons_frame, text=text, font=("Arial", 18), bg=color, fg="#333333", relief="flat",
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            self.buttons.append(button)
            col += 1
            if col > 3:
                col = 0
                row += 1

        for i in range(4):
            self.buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.buttons_frame.grid_rowconfigure(i, weight=1)

        self.root.bind("<Key>", self.on_key_press)

    def on_button_click(self, text):
        if text == "C":
            self.expression_var.set("")
            self.result_var.set("0")
        elif text == "=":
            self.calculate_result()
            self.animate_replace_expression()
        elif text == "√":
            self.expression_var.set(f"sqrt({self.expression_var.get()})")
            self.calculate_result()
        elif text == "sin":
            self.expression_var.set(f"sin({self.expression_var.get()})")
            self.calculate_result()
        elif text == "cos":
            self.expression_var.set(f"cos({self.expression_var.get()})")
            self.calculate_result()
        elif text == "tan":
            self.expression_var.set(f"tan({self.expression_var.get()})")
            self.calculate_result()
        elif text == "ln":
            self.expression_var.set(f"log({self.expression_var.get()})")
            self.calculate_result()
        elif text == "exp":
            self.expression_var.set(f"exp({self.expression_var.get()})")
            self.calculate_result()
        elif text == "!":
            self.expression_var.set(f"factorial({self.expression_var.get()})")
            self.calculate_result()
        else:
            current_value = self.expression_var.get()
            if current_value == "":
                self.expression_var.set(text)
            else:
                self.expression_var.set(current_value + text)
            self.calculate_result()

    def calculate_result(self):
        try:
            expression = self.expression_var.get()
            expression = expression.replace("sqrt", "math.sqrt")
            expression = expression.replace("sin", "math.sin")
            expression = expression.replace("cos", "math.cos")
            expression = expression.replace("tan", "math.tan")
            expression = expression.replace("log", "math.log")
            expression = expression.replace("exp", "math.exp")
            expression = expression.replace("factorial", "math.factorial")
            result = eval(expression)
            self.result_var.set(str(result))
        except Exception as e:
            self.result_var.set("Error")

    def animate_replace_expression(self):
        result = self.result_var.get()
        for i in range(1, len(result) + 1):
            self.expression_var.set(result[:i])
            self.root.update()
            time.sleep(0.05)

    def on_key_press(self, event):
        key = event.keysym
        if key == "Return":
            self.calculate_result()
            self.animate_replace_expression()
        elif key == "BackSpace":
            current_value = self.expression_var.get()
            self.expression_var.set(current_value[:-1] if current_value else "")
            self.calculate_result()
        elif key == "Escape":
            self.expression_var.set("")
            self.result_var.set("0")
        elif key in "0123456789.+-*/()":
            self.on_button_click(key)
        elif key in ["s", "i", "n", "c", "o", "t", "a", "l", "g", "q", "r", "e", "x", "p", "f", "!"]:
            self.expression_var.set(self.expression_var.get() + key)
            self.calculate_result()

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
