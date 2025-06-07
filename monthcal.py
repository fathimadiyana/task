import datetime


month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))


print("\nMon Tue Wed Thu Fri Sat Sun")


first_day = datetime.date(year, month, 1)
start_day = first_day.weekday()  


if month == 12:
    next_month = datetime.date(year + 1, 1, 1)
else:
    next_month = datetime.date(year, month + 1, 1)

days_in_month = (next_month - first_day).days


print("    " * start_day, end="")


for day in range(1, days_in_month + 1):
    print(f"{day:>3} ", end="")
    if (start_day + day - 1) % 7 == 6:  
        print()
