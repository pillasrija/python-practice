def sum(start,end):
    result = 0
    for i in range(start,end+1):
        result = result+i
    print(result)

sum(10,20)


def sum(start,end):
    if(start>end):
        print("start should be less than end")
        return
    result = 0
    for i in range(start,end+1):
         result = result+i
    return result

s=sum(1,5)
print(s)


# global variables vs local variables
xy = 100
def cool():
    xy = 200
    print(xy)
cool()
print(xy)

t = 1
def increment():
    global t
    t = 100
    print(t)

increment()
print()

# passing arguments the method

def func(i,j=100):
    print(i,j)

func(50)
func(50,250)


def named_args(name,greeting):
    print(greeting+" "+name)
named_args("pavan","hi")
named_args(name='pavan',greeting='hi')

def my_func(a,b,c):
    print(a,b,c)
my_func(10,20,30)
my_func(a=10,b=20,c=30)


# returning multiple values from function
def bigger(a,b):
    if a>b:
        return a,b
    else:
        return b,a
s = bigger(100,200)
print(s)
print(type(s))

