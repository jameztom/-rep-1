n=int(input("Enter the number:"))
rev=0
ne=n
while n>0:
    num=num%10
    rev=rev*10+num
    n=n//10
if ne==rev:
    print("Palindrome")
else:
    print("Not palindrome")