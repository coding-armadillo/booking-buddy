import calendar
from datetime import datetime

calendar.setfirstweekday(6)
c = calendar.month(datetime.now().year, datetime.now().month, w=2)
lines = c.strip().split("\n")[2:]
c = 0
for line in lines:
    days = line.split()
    if c == 0 and len(days) < 7:
        days = [None] * (7 - len(days)) + days
    print(days)
