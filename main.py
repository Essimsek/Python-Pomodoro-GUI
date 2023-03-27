import time
from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT = (FONT_NAME, 40, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
rp = 0  # repeat count
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
	global rp
	rp = 0
	screen.after_cancel(timer)  # Cancelling the timer
	check_mark.config(text="")
	timer_label.config(text="Timer")
	canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
	global rp
	work_sec = WORK_MIN * 60
	short_break = SHORT_BREAK_MIN * 60
	long_break = LONG_BREAK_MIN * 60
	if rp == 7:
		timer_label.config(text="Break", font=FONT, fg=GREEN, bg=PINK)
		count_down(long_break)
	if rp % 2 == 0:
		timer_label.config(text="Work", font=FONT, fg=GREEN, bg=PINK)
		count_down(work_sec)
	else:
		timer_label.config(text="Break", font=FONT, fg=GREEN, bg=PINK)
		count_down(short_break)
	rp += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
	global timer
	minute = floor(count / 60)
	second = count % 60
	canvas.itemconfig(timer_text, text=f"{minute:02d}:{second:02d}")
	if count > 0:
		timer = screen.after(1000, count_down, count - 1)
	else:
		start_timer()
		mark = ""
		for i in range(rp//2):
			mark += "✔"
		check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


# Set the window
screen = Tk()
screen.title("Pomodoro")
screen.config(padx=100, pady=50, bg=PINK)


# get image with canvas
canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=2, pady=10, padx=10)


# Label
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=PINK)
timer_label.grid(row=0, column=2, padx=10, pady=10)

check_mark = Label(text="", fg=GREEN, bg=PINK, font=(FONT_NAME, 25, "bold"))
check_mark.grid(row=3, column=2)

# Start button
start_button = Button(padx=5, pady=5, text="Start", bg=PINK, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=1)


# Reset button
reset_button = Button(padx=5, pady=5, text="Reset", bg=PINK, highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=3)

screen.mainloop()






