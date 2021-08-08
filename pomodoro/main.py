"""

This script creates a GUI that represents a 'Pomodoro'
count down timer to help users work while taking breaks.

This script requires that 'tkinter' be installed within the Python
environment you are running this script in.

"""

import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = '✔'
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    """Resets the timer
    """
    global reps
    window.after_cancel(timer)
    reps = 0
    timer_label.config(text='Timer', fg=GREEN)
    checkmark_label.config(text='')
    canvas.itemconfig(timertext, text='00:00')

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    """Starts the timer
    """
    global reps
    reps += 1
    if reps % 2 == 1:
        count_down(WORK_MIN * 60)
        timer_label.config(fg=RED, text='Work')
    elif reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(fg=GREEN, text='Break')
    else:
        count_down(60 * SHORT_BREAK_MIN)
        timer_label.config(fg=PINK, text='Break')

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    """Starts the current countdown

    :param count: int
        The number of seconds for the current timer
    """
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds == 0:
        seconds = '00'
    elif seconds < 10 and seconds != 0:
        seconds = f'0{seconds}'
    canvas.itemconfig(timertext, text=f'{minutes}:{seconds}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        checkmark_label.config(text=f'{checkmark*math.ceil(reps/2)}')
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timertext = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=2, column=2)

timer_label = tkinter.Label(text='Timer', font=(FONT_NAME, 28, 'bold'), bg=YELLOW, fg=GREEN)
timer_label.grid(row=1, column=2)

checkmark_label = tkinter.Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=2, row=4)

start_button = tkinter.Button(text='Start', command=start_timer)
start_button.grid(row=3, column=1)

reset_button = tkinter.Button(text='Reset', command=reset_timer)
reset_button.grid(row=3, column=3)

window.mainloop()