a = int(input('put the first memeber: '))
b = int(input('put the denominator: '))
c = int(input('put the amount of members: '))

d = a * (b ** c)

while a != d:
    print(a)
    a *= b