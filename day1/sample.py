n=int(input())
c100=n//100 #c100 is integer bcz n is int
n=n%100
c50=n//50
n=n%50
c20=n//20
n=n%20
c10=n//10
n=n%10
c2=n//2
n=n%2
n1=c100+c50+c20+c10+c2
print("the number of notes",n1)