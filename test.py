class ONum(object):

    def __init__(self, val):
        self.val = val
        
    def __add__(self, y):
        return ONum(self.val + y)
        
    def __radd__(self, x):
        return x + self.val
        
    def __iadd__(self, y):
        self.val += y
        return self
        
x = ONum(5)
print(x+3, type(x+3))
print(3+x, type(3+x))

x += 3
print(x, type(x))