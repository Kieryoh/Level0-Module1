from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    pizza = 'y u m'
    water = 'e'
    cat = 'a'
    dog = 'b'
    fish = 'c'
    parrot = 'd'

    input = simpledialog.askstring(title='t', prompt='f')

    if input == 'pizza'