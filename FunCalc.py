import tkinter as tk
from tkinter import messagebox
import random


class MoveWindowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Integrated App")

        self.window_width = 400
        self.window_height = 300
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x = (self.screen_width - self.window_width) // 2
        self.y = (self.screen_height - self.window_height) // 2
        self.distance = 20
        self.move_counter = 0  # Counter for window moves

        self.create_move_window()
        self.create_calculator()
        self.center_window(self.root)  # Center the main window

        # Bind the "q" key event to check for exit
        self.root.bind('<Key>', self.check_key)

    def move_window(self, event=None):
        if self.root.state() == "normal":
            random_x = random.randint(-50, 50)
            random_y = random.randint(-50, 50)
            self.x += random_x
            self.y += random_y
            self.distance *= 2
            x_offset = int(self.distance * (random.random() * 2 - 1))
            y_offset = int(self.distance * (random.random() * 2 - 1))
            new_x = self.x + x_offset
            new_y = self.y + y_offset

            if new_x < 0 or new_y < 0 or new_x + self.window_width > self.screen_width or new_y + self.window_height > self.screen_height:
                self.x = (self.screen_width - self.window_width) // 2
                self.y = (self.screen_height - self.window_height) // 2
                self.root.geometry(f"{self.window_width}x{self.window_height}+{self.x}+{self.y}")
                self.distance = 20
                self.move_window()
            else:
                self.root.geometry(f"{self.window_width}x{self.window_height}+{new_x}+{new_y}")
                self.move_counter += 1  # Increment move counter
                if self.move_counter == 10:
                    self.move_counter = 0  # Reset move counter after 30 moves
                    self.show_exit_prompt()

    def center_window(self, window):
        x = (self.screen_width - self.window_width) // 2
        y = (self.screen_height - self.window_height) // 2
        window.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

    def create_move_window(self):
        close_button = tk.Button(self.root, bg="lightgray", relief="flat", command=self.root.destroy)
        close_button.place(x=0, y=0, width=self.window_width, height=10)
        close_button.bind("<Motion>", self.move_window)
        self.root.protocol("WM_DELETE_WINDOW", self.move_window)

    def create_calculator(self):
        input_frame = tk.LabelFrame(self.root, text="Input Fields", padx=10, pady=10)
        input_frame.pack(padx=10, pady=10)

        operation_label = tk.Label(input_frame, text="Operation:")
        operation_label.grid(row=0, column=0, padx=5, pady=5)

        operations = ['+', '-', '*', '/']
        self.operation_var = tk.StringVar(self.root)
        self.operation_var.set(operations[0])
        operation_menu = tk.OptionMenu(input_frame, self.operation_var, *operations)
        operation_menu.grid(row=0, column=1, padx=5, pady=5)

        num1_label = tk.Label(input_frame, text="First Number:")
        num1_label.grid(row=1, column=0, padx=5, pady=5)
        self.num1_entry = tk.Entry(input_frame)
        self.num1_entry.grid(row=1, column=1, padx=5, pady=5)

        num2_label = tk.Label(input_frame, text="Second Number:")
        num2_label.grid(row=2, column=0, padx=5, pady=5)
        self.num2_entry = tk.Entry(input_frame)
        self.num2_entry.grid(row=2, column=1, padx=5, pady=5)

        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        calculate_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def calculate(self):
        operation = self.operation_var.get()
        num1 = self.num1_entry.get()
        num2 = self.num2_entry.get()

        if operation not in ['+', '-', '*', '/']:
            messagebox.showerror("Error", "Invalid operation.")
            return

        if not self.is_number(num1) or not self.is_number(num2):
            messagebox.showerror("Error", "Enter numerical values for numbers.")
            return

        num1 = float(num1)
        num2 = float(num2)

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero.")
                return
            else:
                result = num1 / num2

        function_string = f"{num1} {operation} {num2}"

        self.result_label.config(text=f"Result: {result}\nFunction: {function_string}")

        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)

    def show_exit_prompt(self):
        messagebox.showinfo("Exit Prompt", "Press 'q' to exit.")

    def check_key(self, event):
        if event.char == 'q':
            self.exit_app()

    def exit_app(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MoveWindowApp(root)
    root.mainloop()
