import random

l = []

for i in range(50):
    num = random.randint(0,200)
    if num not in l:
        l.append(num)


def merge(a, b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


def mergesort(x):
    print("Added a new line")
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x) // 2
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
    return merge(a, b)


print('The maximum number is : {}'.format(mergesort(l)[-1]) )
