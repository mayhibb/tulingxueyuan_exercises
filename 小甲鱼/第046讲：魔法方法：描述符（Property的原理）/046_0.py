class Descriptor():
    def __get__(self,instance,owner):
        print("get.....",self,instance,owner)
    def __set__(self,instance,value):
        print('set....',self,instance,value)
    def __delete__(self,instance):
        print("def....",self,instance)


class Test():
    x = Descriptor()



text = Test()



class Myproperty():
    def __init__(self,fget=None,fset=None,fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self,instance,owner):
        return self.fget(instance)
    def __set__(self,instance,value):
        self.fset(instance,value)
    def __delete__(self,instance):
        self.fdel(instance)

class C:
    def __init__(self):
        self._x = None
    def getX(self):
        return self._x
    def setX(self,value):
        self._x = value
    def delX(self):
        del self._x

    a = Myproperty(getX,setX,delX)
    
    
        
