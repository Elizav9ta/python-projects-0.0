#2
x = "awesome"
def myfunc():
    x = "fantastic"#local
    print("Python is " + x)

myfunc()
print("Python is " + x)