# its clear that hello is not a function, and so bugs out, we need to define it as a function
# def hello():
#      print("Hello ")

# name=input("what's your name? ")
# hello()
# print(name)
#here the output of hello and my name are are diff lines, which is kinda shit, 
#the following bit will fix this

# def hello(to="world"):
#      print("Hello,", to )
# hello( )
# name=input("what's your name? ")
# hello(name)

#if we want to define functions we must put the def before we use it (or call it) 
# that can make it hard to code cuz you end up writing code top to bottom. 
#so we use the main def function to help us. 

def main():
    name = input("what's your name? ")
    hello(name)

def hello(to="world"):
     print("Hello,", to )
main()


