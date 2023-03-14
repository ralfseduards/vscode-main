import datetime as dt
import calendar

import re


a = dt.datetime.today().strftime("%d/%m/%Y")


print("")

deadline = input(f"\t\tHi todays date {a}, input goal date (dd/mm/yyyy):").strip()

if day := re.match(r"^(\d{2})/(\d{2})/(\d{4})$", deadline):
    if 31 > int(day.group(1)) > 0:
        print("invalid day!!!")
    elif 12 > int(day.group(2)) > 0:
        print("invalid month!!!!")
    else:
        print(day.group(1), day.group(2), day.group(3))
else:
    print("invalid date!!!")
    exit()


delta = day - a 