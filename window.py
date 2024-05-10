import tkinter as tk
import tkinter.messagebox as mb

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        btn_error = tk.Button(self, text="Calculator",
                              command=self.show_error)

        opts = {'padx': 100, 'pady': 50, 'expand': True, 'fill': tk.BOTH}

        btn_error.pack(**opts)



    def show_error(self):
        msg = "Warning message! Your data has started to be deleted after 5 sec:)"
        mb.showerror("Warning", msg)

if __name__ == "__main__":
    app = App()
    app.mainloop()