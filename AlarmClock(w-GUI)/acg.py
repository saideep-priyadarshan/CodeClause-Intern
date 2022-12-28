import datetime as dt
import time
from tkinter import *
from tkinter import Tk
from playsound import playsound


def alarm(setAlarmTimer):
    while True:
        time.sleep(1)
        actualTime = dt.datetime.now()
        currentTime = actualTime.strftime("%H : %M : %S")
        currentDate = actualTime.strftime("%d / %m / %Y")
        the_message = "Current Time: " + str(currentTime)
        print(the_message)
        if currentTime == setAlarmTimer:
            playsound('alarm.mp3')
            break


def getAlarmTime():
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"
    alarm(alarmSetTime)


guiWindow: Tk = Tk()
guiWindow.title("Alarm Clock")
guiWindow.geometry("480x240")
guiWindow.config(bg="#474d4d")
guiWindow.resizable(width=False, height=False)

Label(guiWindow, text="Set time in 24-hour format", fg="#e7e6e1",
      bg="#43476f", font=("Arial", 18)).place(x=97, y=175)

Label(guiWindow, text="Hour      Minute     Second",
      font=60, fg="#e7e6e1", bg="#474d4d").place(x=200, y=10)

Label(guiWindow, text="Time for Alarm:", fg="#e7e6e1", bg="#4d5180",
      relief="solid", font=("Helvetica", 13, "bold")).place(x=57, y=54)

hour = StringVar()
minute = StringVar()
second = StringVar()

Entry(guiWindow, textvariable=hour, bg="#cfd0d2", width=4,
      font=20).place(x=200, y=53)

Entry(guiWindow, textvariable=minute, bg="#cfd0d2", width=4,
      font=20).place(x=282, y=53)

Entry(guiWindow, textvariable=second, bg="#cfd0d2", width=4,
      font=20).place(x=375, y=53)

Button(guiWindow, text="Set The Alarm", fg="#e7e6e1", bg="#16773f", width=15,
       command=getAlarmTime, font=20).place(x=148, y=110)

guiWindow.mainloop()