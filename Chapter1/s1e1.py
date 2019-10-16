#Show how the values of four variables(a, b, c, d) can be rearranged to (b,c,d,a) by a sequence of replacements.

#Very simple with a fifth temporary variable


a="a"
b="b"
c="c"
d="d"

print(a,b,c,d)

t=a
a=b
b=c
c=d
d=t

print(a,b,c,d)