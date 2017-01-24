class ONum(object):

    def __init__(self, *args, **kwargs):
        self._valf = lambda v = kwargs.get('func', args[0]) : v

    def __str__(self):
        return str(self._valf())
    
    """    
    @property
    def _val(self):
        return self._valf()
        
    @_val.setter
    def _val(self, val):
        self._valf = lambda x = val: x
    
    """
    def __add__(self, y):
        print("__add__")
        return ONum(func = lambda s=self, yval=y: s._valf() + yval)

    """
    def __radd__(self, x):
        #print("__radd__")
        self._val = lambda s = self, v = x : ONum(x + s.val)
        return self.val
        
    def __iadd__(self, y):
        #print("__iadd__")
        self.val += y
        return self
    """

        
        
x = ONum(5)
y = ONum(3)

print(x)
z = x + 3
print(z)


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