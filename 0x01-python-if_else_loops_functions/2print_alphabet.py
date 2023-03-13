number = int(input())
LastDigit = number % 10
if(LastDigit > 5):
    print(f"Last digit of {number} is {LastDigit} and is greater than 5")
elif(LastDigit == 0):
    print(f"Last digit of {number} is {LastDigit} and is 0")
else:
    print(f"Last digit of {number} is {LastDigit} and is less than 6 and not 0")
