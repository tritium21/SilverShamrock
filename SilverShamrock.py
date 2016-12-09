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
        self.halloween = halloween
        self.root = root
        self.initialize()
        self.loop()

    def initialize(self):
        self.days = StringVar()
        self.initialize_window()
        self.initialize_mainframe()

    def initialize_mainframe(self):
        self.mainframe = Frame(root, bg="#FA8E0F")
        self.mainframe.grid(column=0, row=0, sticky="NEWS")
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.headingFont = font.Font(
            family="TkHeadingFont",
            size=32,
            weight="bold",
        )
        self.label = Label(
            self.mainframe,
            textvariable=self.days,
            anchor="center",
            font=self.headingFont,
            foreground="#9601D4",
            bg="#05CD1D"
        )
        self.label.grid(column=0, row=0, sticky="NEWS")
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def initialize_window(self):
        self.set_icon()
        self.root.resizable(0,0)
        self.root.title("Silver Shamrock")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def set_icon(self):
        if getattr(sys, 'frozen', False):
            icon = path.join(sys._MEIPASS, 'pumpkin.ico')
        else:
            icon = path.join(
                path.dirname(path.abspath(__file__)),
                'pumpkin.ico',
            )
        self.root.iconbitmap(icon)

    def loop(self):
        until = self.halloween.until
        days = until.days
        minutes, seconds = divmod(until.seconds, 60)
        hours, minutes = divmod(minutes, 60)
        fmt = "{} Days\n{} Hours\n{} Minutes\n{} Seconds\n\n'Til Halloween!"
        self.days.set(fmt.format(days, hours, minutes, seconds))
        self.root.after(1000, self.loop)

if __name__ == "__main__":
    h = Halloween()
    root = Tk()
    gui = GUI(root, h)
    root.mainloop()