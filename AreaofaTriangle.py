a = float(input("Enter the first number:"))
b = float(input("Enter the first number:"))
c = float(input("Enter the first number:"))

s = (a+b + c) / 2
area = (s*(s-a) * (s-b) * (s-c)) ** 0.5

print('The area is : %0.2f' % area )