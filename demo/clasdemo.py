class C1(object):
    def c1(self,arg):
        print(arg)

def b(self,b1):
    print(b1)

if __name__ == '__main__':
    C1.b = b
    c = C1()
    c.b(2)