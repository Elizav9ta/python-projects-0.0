"""Define a class which has at least two methods: 
getString: to get a string from console input printString: 
to print the string in upper case."""

class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

# Example usage
manipulator = StringManipulator()
manipulator.getString()
manipulator.printString()
