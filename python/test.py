class A(object):
    __isinstance = None
    __init_first = True

    def __init__(self, age):
        # if self.__init_first:
        self.age = age
        print( self.age)
        #     self.age = age
        #     print(age)
        #     A.__init_first = False

    def __new__(cls, age):
        if not cls.__isinstance:
            cls.__isinstance = object.__new__(cls)
        return cls.__isinstance

if __name__ == "__main__":
     a = A(1)
     b = A(2)
     print(a.age)
     print(id(a))
     print(id(b))
     a.age = 3
     print(b.age)