def f():
    a = 2 

    class My:
        def __init__(self, name):
            self.name = name

        def print_name(self):
            print(self.name)

    def num():
        print('1124')

    def inner():
        print(a)
        num()
        My('橙子').print_name()
        
    return inner

y = f()
y()
# 2
# 1124
# 橙子
print(y.__closure__)
# (<cell at 0x0000024C136205E0: type object at 0x0000024C137A52D0>, 
# <cell at 0x0000024C136201F0: int object at 0x00007FFBEFD8E348>, 
# <cell at 0x0000024C136216C0: function object at 0x0000024C134B04A0>)

