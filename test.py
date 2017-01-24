class ONum(object):

    def __init__(self, *args, **kwargs):
        if len(args):
            self.update(args[0])
        else:
            self._valf = kwargs["func"]

    def __str__(self):
        return str(self._valf())
        
    def update(self, val):
        self._valf = lambda v = val: v
    
    def __add__(self, y):
        print("__add__")
        return ONum(func = lambda s=self, yval=y: s._valf() + yval)

    def __radd__(self, x):
        print("__radd__")
        return ONum(func = lambda s=self, xval=x: xval + s._valf())

    def __iadd__(self, y):
        print("__iadd__")
        x = self + y
        self._valf = lambda xval=x: xval._valf

        
x = ONum(5)
y = ONum(3)

#x = x + 1
#print(x)

print(x)
x += 1
print(x)

#print(x+3, type(x+3)) # __add__
#print(3+x, type(3+x)) # __radd__

"""
x += 3  # __iadd__
print(x, type(x))

print(x+y, type(x+y)) # __add__ __radd__

u = ONum(1)

z = 3+(u+1)+5 # add, radd, add, radd, add
print(z, type(z))

print(id(z))
z += x # iadd, radd
print(z, type(z))
print(id(z))
"""