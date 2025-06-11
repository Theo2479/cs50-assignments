# x=input("what is x? ")
# y=input("what is y? ")
# # just showing the values 
# z= int(x) + int(y)
# #math operation: the plus sign is not math adding it just combinds the strings, therefore must use int(x) and int(y) 
# print(z) Output the result
# #alternativly you can you remove the use of the variable z and just print the result directly. 
# #by nesting the int function inside the input function

# x=int(input("what is x? "))
# y=int(input("what is y? "))
# print(x + y)
# Output the result

# you can also use decimal numbers by using float instead of int
# x=float(input("what is x? "))
# y=float(input("what is y? "))
# print(x + y)
# Output the result

# you can also use the round function to round the result to a certain number of decimal places
# x=float(input("what is x? "))
# y=float(input("what is y? "))
# z= round(x + y, 2)  # rounding to 2 decimal places
# print(z) # Output the result

# you can also use the format function to format the result to a certain number of decimal places
# x=float(input("what is x? "))
# y=float(input("what is y? "))
# z= round(x + y, 2)  # rounding to 2 decimal places
# print(f"{z:,}")
# Output the result with commas as thousands separators

#we can also use division
# x=float(input("what is x? "))
# y=float(input("what is y? "))
# z= round(x / y, 2)  #the rouding and formatting is not important here, but you can do both, unformatted or formatted
# print(f"{z:,}") #the F string is not necessary here 

#here we will practice using the def functions and return functions 
def main():
    x=int(input("what is x? "))  
    print("x squared is", square(x))

def square(n):
    return n * n  #returning the square of the number
# this is a simple function that takes a number and returns its square
# you can also use def square(n): return n ** 2 (with the number being raised to the power of 2)
# or use def square(n): return pow(n, 2) (with the pow function)

main()
