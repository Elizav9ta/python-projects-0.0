#1 code which only runs when it is called.
def my_function():
  print("Hello from a function")

my_function()

#2
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
#If the number of arguments is unknown, add a * before the parameter name:

#3
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


#4
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
