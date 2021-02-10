# TUPLES
# temp = x
# x = y
# y = temp
#
# # is the same as writing
# (x,y) = (y,x)

# can be used to return more than one value from a function


def quotient_and_remainder(x,y):
    q = x // y
    r = x % y
    return q, r

(quot, rem) = quotient_and_remainder(4, 5)

def x():
    return 1,2,3
(a,b,c) = x()
print(a, b, c)

def xy(x,y):
    return x+y
xy(1,2)