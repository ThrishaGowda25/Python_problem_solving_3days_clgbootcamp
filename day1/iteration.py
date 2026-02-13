#fancy number
number=input("enter the number: ")
if len(number)!=4 or not number.isdigit():
    print("get lost")
else:
    increasing=True
    decreasing=True
    
    for i in range(3):
        if number[i]>=number[i+1]:
            increasing=False
        if number[i]<=number[i+1]:
            decreasing=False
    if increasing:
        print("Fancy Number")
    elif decreasing:
        print("fancy number")
    else:
        print("not a fancy number")
