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
        self.update(self._valf() + y)


        
x = DyNum(5)
y = DyNum(3)


print(x-y)
print(y-x)
print(x)
x -= 33
print(x)