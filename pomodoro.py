from tkinter import *
from tkinter import messagebox
from tkmacosx import Button as PrettyButton
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#006400"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_TIME = 5
SHORT_BREAK_TIME = 5
LONG_BREAK_TIME = 7
REPS = 0
timer = None


def reset_timer():
  window.after_cancel(timer)
  canvas.itemconfig(timer_text, text="00:00")
  title_label.config(text="TIMER")
  check_marks.config(text="")
  global REPS
  REPS = 0


def start_timer():
  global REPS
  REPS += 1

  if REPS % 8 == 0:
    count_down(LONG_BREAK_TIME)
    title_label.config(text="LONG BREAK", fg=RED)
    messagebox.showinfo("Big break time", "Great job! Time for a big break!")
  elif REPS % 2 == 0:
    count_down(SHORT_BREAK_TIME)
    title_label.config(text="SHORT BREAK", fg=PINK)
    messagebox.showinfo("Break time!", "Good job! Time for a break!")
  else:
    count_down(WORK_TIME)
    title_label.config(text="WORK", fg=GREEN)
    if REPS > 1:
      messagebox.showinfo("Work time!", "Time to get back to work!")



def count_down(count):
  count_min = math.floor(count / 60)
  count_sec = count % 60

  if count_sec < 10:
    count_sec = f"0{count_sec}"
  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count - 1)
  else:
    start_timer()

    marks = "work sessions: "
    work_sessions = str(math.floor(REPS / 2))
    check_marks.config(text=marks + work_sessions)


window = Tk()
window.title("flight pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# timer label
title_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=("Diary Of A Wimpy Kid Font", 30, "bold"))
title_label.grid(column=1, row=0)

# tkinter canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = PrettyButton(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = PrettyButton(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
