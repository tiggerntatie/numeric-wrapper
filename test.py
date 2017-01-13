class ONum(object):

    def __init__(self, val):
        self.val = val
        
    def __str__(self):
        return str(self.val)
        
    def __add__(self, y):
        return ONum(self.val + y)
        
    def __radd__(self, x):
        return ONum(x + self.val)
        
    def __iadd__(self, y):
        self.val += y
        return self
        
x = ONum(5)
y = ONum(3)
print(x+3, type(x+3))
print(3+x, type(3+x))

x += 3
print(x, type(x))

print(x+y, type(x+y))

u = ONum(1)

z = 3+(u+1)+5
print(z, type(z))