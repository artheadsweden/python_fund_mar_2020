import tkinter as tk


def main():
    window = tk.Tk()
    label1 = tk.Label(window, text="Red", bg="red", fg="white")
    label1.pack()
    label2 = tk.Label(window, text="Green", bg="green", fg="black")
    label2.pack()
    label3 = tk.Label(window, text="Blue", bg="blue", fg="white")
    label3.pack()
    window.mainloop()


if __name__ == '__main__':
    main()
