def partySuccessCheck(day, attendees):
    days = ["SUN", "MON", "TUE", "WED", "THUR", "FRI", "SAT"]

    # Input constraint
    if day not in days or attendees < 0:
        return "Invalid Input"

    if day in ["FRI", "SAT", "SUN"]:
        if attendees >= 1500:
            return "successful"
        else:
            return "unsuccessful"
    else:
        if 700 <= attendees <= 1000:
            return "successful"
        else:
            return "unsuccessful"


# main
day = input("Enter the day: ").strip().upper()
attendees = int(input("Enter the number of attendees: ").strip())

checksuccess = partySuccessCheck(day, attendees)
print(checksuccess)
