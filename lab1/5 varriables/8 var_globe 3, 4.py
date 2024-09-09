#3
def myfunc():
    global x
    x = "fantastic 1"

myfunc()

print("Python is " + x)

#4
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)