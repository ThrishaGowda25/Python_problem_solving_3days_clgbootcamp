s1=input()
mid=len(s1)//2
first=s1[:mid]
last=s1[mid:]
firstr=first[::-1]
lastr=last[::-1]

print(firstr+lastr)
