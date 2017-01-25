import math, numbers

class DyNum(numbers.Number):

    def __init__(self, *args, **kwargs):
        if len(args):
            self.update(args[0])
        else:
            self._valf = kwargs["func"]
        self._prev = None
        self._frozen = False

    def __str__(self):
        return str(self._valf())
        
    def update(self, val):
        self._valf = lambda v = val: v
        
    @property
    def val(self):
        if not self._frozen:
            self._prev = self._valf()
        return self._prev
        
    @val.setter
    def val(self, val):
        self.update(val)
        self._prev = self._valf()
        
    @property 
    def prev(self):
        return self._prev

    def freeze(self, frozen=True):
        self._frozen = frozen
        
    def thaw(self):
        self.freeze(False)

    # ADD    
    def __add__(self, y):
        return DyNum(func = lambda s=self, yval=y: s.val + yval)

    def __radd__(self, x):
        return DyNum(func = lambda s=self, xval=x: xval + s.val)

    def __iadd__(self, y):
        self.update(self._valf() + y)
    # SUB 
    def __sub__(self, y):
        return DyNum(func = lambda s=self, yval=y: s.val - yval)

    def __rsub__(self, x):
        return DyNum(func = lambda s=self, xval=x: xval - s.val)

    def __isub__(self, y):
        self.update(self.val - y)
    # MUL 
    def __mul__(self, y):
        return DyNum(func = lambda s=self, yval=y: s.val * yval)

    def __rmul__(self, x):
        return DyNum(func = lambda s=self, xval=x: xval * s.val)

    def __imul__(self, y):
        self.update(self.val * y)
    # TRUEDIV 
    def __truediv__(self, y):
        return DyNum(func = lambda s=self, yval=y: s.val / yval)

    def __rtruediv__(self, x):
        return DyNum(func = lambda s=self, xval=x: xval / s.val)

    def __itruediv__(self, y):
        self.update(self.val / y)
    # POW
    def __pow__(self, y):
        return DyNum(func = lambda s=self, yval=y: s.val ** yval)

    def __rpow__(self, x):
        return DyNum(func = lambda s=self, xval=x: xval ** s.val)

    def __ipow__(self, y):
        self.update(self.val ** y)
    # CONVERSIONS
    def __int__(self):
        return int(self.val)
        
    def __float__(self):
        return float(self.val)
    
    def __round__(self):
        return round(self.val)

        
x = DyNum(5)
y = DyNum(3)

a = x + y
b = x * y
c = x / y
d = x - y

print(a, b, c, d)
x.update(55)
print(a, b, c, d)
print(math.sin(float(a)))
print(math.sin(58))