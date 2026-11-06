print("==================================================")
print("           CALENDAR VERIFICATION SYSTEM           ")
print("==================================================")

year = int(input("Enter year: "))
if year <= 0:
    print("Error: Please enter a positive year.")
else:
    if year % 100 == 0:
        if year % 400 == 0:
            status = "LEAP YEAR"
            days_in_year = 366
            days_in_february = 29
            reason = "Divisible by 400"
        else:
            status = "COMMON YEAR"
            days_in_year = 365
            days_in_february = 28
            reason = "Century year not divisible by 400"
    elif year % 4 == 0:
        status = "LEAP YEAR"
        days_in_year = 366
        days_in_february = 29
        reason = "Divisible by 4 and not a century year"

    else:
        status = "COMMON YEAR"
        days_in_year = 365
        days_in_february = 28
        reason = "Not divisible by 4"

print("\n----------------------------------------")
print("Year:", year)
print("Status:", status)
print("Days in Year:", days_in_year, "days")
print("Days in February:", days_in_february, "days")
print("Reason:", reason)
print("----------------------------------------")