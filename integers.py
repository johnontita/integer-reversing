"""
Write a program that takes an integer as input and returns an integer with
reversed digit ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19.

"""
def reversing_integers(num):
    sum=0
    sign=1
    if num<0:
        sign=-1
        num=num*-1
    while num>0:
        rem=num%10 #modulus operator to return a reminder
        sum=sum*10+rem
        num=num//10 #floor division rounds down the results to a whole value
    if not -21474833648<sum<21474833648:
        return 0
    return sign*sum
num=int(input("enter an integer"))
print(reversing_integers(num))
# print(reversing_integers(124))