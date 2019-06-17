def f(x):
    y = x * 2
    return y


for i in range(10):
    print('{0}:{1}'.format(i, (lambda x: x*2)(i)), end=' ')
else:
    print()
