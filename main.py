from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Pomodoro Timer")
    reps=0
    tick_label.config(text="")



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    #Counts reps and adds one tick for every work and short break completed. Resets after long break
    tick_counter = math.ceil((reps/2)-1)%4
    tick_label.config(text="✓"*tick_counter)
    if reps % 2 !=0:
        count_down(WORK_MIN*60)
        timer_label.config(text="Work")
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        timer_label.config(text="Long Break")
    else:
        count_down(SHORT_BREAK_MIN*60)
        timer_label.config(text="Short Break")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time_left):
    global timer
    minutes = math.floor(time_left / 60)
    seconds = time_left % 60

    canvas.itemconfig(timer_text,text=f"{minutes:02d}:{seconds:02d}")
    if time_left >0:
        timer = window.after(100, count_down, time_left -1)
    else:
        start_timer()




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Pomodoro Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1, pady=20)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(105, 112, image=tomato_img)
timer_text = canvas.create_text(107, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start",width=10, highlightthickness=0, command=start_timer)
start_button.grid(row=2,column=0)


reset_button = Button(text="Reset",width=10, highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)

tick_label = Label(text="",fg=GREEN,bg=YELLOW, font=("",16))
tick_label.grid(row=3,column=1)

window.mainloop()
