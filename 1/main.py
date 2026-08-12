class N:
    def __init__(self, v):
        self.v = v
        self.n = None


class L:
    def __init__(self):
        self.h = None
        self.t = None

    def add(self, v):
        node = N(v)
        if not self.h:
            self.h = node
            self.t = node
        else:
            self.t.n = node
            self.t = node

    def show(self):
        res = []
        c = self.h
        while c:
            res.append(c.v)
            c = c.n
        return res


def rem(l1):
    l2 = L()
    c = l1.h
    while c:
        if c.v % 2 == 0:
            l2.add(c.v)
        c = c.n
    return l2


s1 = L()
for x in [1, 2, 3, 5]:
    s1.add(x)
r1 = rem(s1)
print("test1:", r1.show())
s2 = L()
for x in [5, 5, 5]:
    s2.add(x)
r2 = rem(s2)
print("test2:", r2.show())
s3 = L()
for x in [2, 4, 6]:
    s3.add(x)
r3 = rem(s3)
print("test3:", r3.show())
s4 = L()
r4 = rem(s4)
print("test4:", r4.show())
