array = []

a = int(input())

for i in range(0, a):
    x = int(input())
    array.append(x)

print(array)

r = sorted(array)

print(r)

if array == r :
    print('araye moratab ast')

else:
    print('araye na morabat ast')
