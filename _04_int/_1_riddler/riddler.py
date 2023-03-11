from tkinter import messagebox, simpledialog, Tk
"""
* Write a python program that asks the user a minimum of 3 riddles.



* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
if __name__ == '__main__':
    window = Tk()
    window.withdraw

    score = 0

    answer1 = simpledialog.askstring(title='Q1', prompt="I fly when I am born, lie when I'm alive, and run when I am dead. What am I?")
    answer2 = simpledialog.askstring(title='Q2', prompt="When my father was 31 I was 8. Now he is twice as old as me. How old am I?")
    answer3 = simpledialog.askstring(title='Q3', prompt="What can you hold in your right hand, but not in your left?")

    if answer1 == 'a snowflake':
        messagebox.showinfo(message='Correct!')
        score += 1
    else:
        messagebox.showerror(message='Incorrect.')
        score -= 1

    if answer2 == '23':
        messagebox.showinfo(message='Correct!')
        score += 1
    else:
        messagebox.showerror(message='Incorrect.')
        score -= 1

    if answer3 == 'ylh':
        messagebox.showinfo(message='Correct!')
        score += 1
    else:
        messagebox.showerror(message='Incorrect.')
        score -= 1

    messagebox.showinfo(message='Your score was ' + str(score))