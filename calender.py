import calendar

month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

print("Calendar:")
print(calendar.month(year, month))
