from controller.ControllerUI import ControllerUI
import tkinter as tk

def main():
    root = tk.Tk()
    gameController = ControllerUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()