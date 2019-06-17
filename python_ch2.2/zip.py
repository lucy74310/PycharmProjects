
seq1 = {'foo', 'bar', 'baz'}       # set이라 순서 없음 순서원하면 리스트로 하면 됨
seq2 = {'one', 'two', 'three'}

z = zip(seq1, seq2)
print(z, type(z))

for t in z:
    print(t, type(t))

tl = [('foo', 'one'), ('baz', 'two'), ('bar', 'three')]

seq3, seq4 = zip(*tl)
print(seq3, seq4, type(seq3))
