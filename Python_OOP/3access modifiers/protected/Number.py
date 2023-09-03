class Number:
    def __init__(self, _x):
        self._x = _x

    def _protected_method(self):
        return self._x
    
class PositiveNum(Number):
    def __init__(self, _x):
        super().__init__(_x)

        

'''
protected: cannot be accessed directly from outside the class.
           but it can be accessed from subclass
'''