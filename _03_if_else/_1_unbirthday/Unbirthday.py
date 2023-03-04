from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    birthday = simpledialog.askstring(title='Unbirthday', prompt='What is your birthday? (mm/dd)')

    if birthday == '03/03':
        messagebox.showinfo(message='Happy Birthday!')
    else:
        messagebox.showinfo(message='Happy Unbirthday!')