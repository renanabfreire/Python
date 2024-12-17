class A:
    vc = 123


a1 = A()
a2 = A()

a2.vc = 321

print(a1.vc)
print(a2.vc)
print(A.vc)

print()


class B:
    vc = 456

    def __int__(self):
        self.vc = 654


b1 = B()
b2 = B()

print(b1.vc)
print(b2.vc)
print(B.vc)
