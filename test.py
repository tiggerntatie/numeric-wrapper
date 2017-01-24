class DyNum(object):

    def __init__(self, *args, **kwargs):
        if len(args):
            self.update(args[0])
        else:
            self._valf = kwargs["func"]

    def __str__(self):
        return str(self._valf())
        
    def update(self, val):
        self._valf = lambda v = val: v

    # ADD    
    def __add__(self, y):
        return DyNum(func = lambda s=self, yval=y: s._valf() + yval)

    def __radd__(self, x):
        return DyNum(func = lambda s=self, xval=x: xval + s._valf())

    def __iadd__(self, y):
        self.update(self._valf() + y)
    # SUB 
    def __sub__(self, y):
        return DyNum(func = lambda s=self, yval=y: s._valf() - yval)

    def __rsub__(self, x):
        return DyNum(func = lambda s=self, xval=x: xval - s._valf())

    def __isub__(self, y):
        self.update(self._valf() - y)
    # MUL 
    def __mul__(self, y):
        return DyNum(func = lambda s=self, yval=y: s._valf() * yval)

    def __rmul__(self, x):
        return DyNum(func = lambda s=self, xval=x: xval * s._valf())

    def __imul__(self, y):
        self.update(self._valf() * y)
    # TRUEDIV 
    def __truediv__(self, y):
        return DyNum(func = lambda s=self, yval=y: s._valf() / yval)

    def __rtruediv__(self, x):
        return DyNum(func = lambda s=self, xval=x: xval / s._valf())

    def __itruediv__(self, y):
        self.update(self._valf() / y)
    # POW
    def __pow__(self, y):
        return DyNum(func = lambda s=self, yval=y: s._valf() ** yval)

    def __rpow__(self, x):
        return DyNum(func = lambda s=self, xval=x: xval ** s._valf())

    def __ipow__(self, y):
        self.update(self._valf() ** y)
    # CONVERSIONS
    def __int__(self):
        return int(self._valf())
        
    def __float__(self):
        return float(self._valf())
    
    def __round__(self):
        return round(self._valf())

        
x = DyNum(5)
y = DyNum(3)

z = x + 3*y + x**2
print(float(z))
print(int(z))
print(round(z))
x.update(2)
print(z)
xx = DyNum(z)
print(xx)

