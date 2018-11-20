
class A():
    def a(self):
        print("这是基类中的方法‘a’")

class B(A):
    def b(self):
        print("这是子类中的一个方法‘b’")
        print("* "*10)
        super(B,self).a()
        print("* "*10)
        A().a()

