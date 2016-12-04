from datetime import datetime
from tkinter import Tk, Frame, Label, StringVar, font
import os.path as path
import sys

from dateutil.rrule import rrule, YEARLY
from pytz import UTC
from tzlocal import get_localzone

class Halloween:
    def __init__(self, localzone=get_localzone()):
        self.localzone = localzone
        _year = self._now().year
        _dtstart = localzone.localize(datetime(_year, 10, 31))
        self.rrule = rrule(
            YEARLY,
            bymonth=10,
            bymonthday=31,
            byhour=0,
            byminute=0,
            bysecond=0,
            dtstart=_dtstart,
        )

    def _now(self):
        return self.localzone.localize(datetime.now())

    @property
    def next(self):
        return self.rrule.after(self._now())

    @property
    def until(self):
        return self.next - self._now()



class GUI:
    def __init__(self, root, halloween):
        if getattr(sys, 'frozen', False):
            icon = path.join(sys._MEIPASS, 'pumpkin.ico')
        else:
            icon = path.join(path.dirname(path.abspath(__file__)), 'pumpkin.ico')
        self.halloween = halloween
        self.root = root
        self.root.iconbitmap(icon)
        root.resizable(0,0)
        root.title("Silver Shamrock")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.mainframe = mainframe = Frame(root, bg="#FA8E0F")
        mainframe.grid(column=0, row=0, sticky="NEWS")
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        self.days = days = StringVar()
        headingFont = font.Font(
            family="TkHeadingFont",
            size=32,
            weight="bold",
        )
        label = Label(
            mainframe,
            textvariable=days,
            anchor="center",
            font=headingFont,
            foreground="#9601D4",
            bg="#05CD1D"
        )
        label.grid(column=0, row=0, sticky="NEWS")
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.loop()

    def loop(self):
        until = self.halloween.until
        days = until.days
        minutes, seconds = divmod(until.seconds, 60)
        hours, minutes = divmod(minutes, 60)
        self.days.set(
            "{} Days\n{} Hours\n{} Minutes\n{} Seconds\n\n'Til Halloween!".format(
                days,
                hours,
                minutes,
                seconds,
            )
        )
        self.root.after(1000, self.loop)

h = Halloween()
root = Tk()
gui = GUI(root, h)
root.mainloop()