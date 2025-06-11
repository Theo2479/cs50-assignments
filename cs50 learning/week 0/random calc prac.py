
def main():
    x=float(input("what is x? ")) 
    y=float(input("what is y? "))
    z=round((x*y + square(x)+square(y)),2)
    print(z)

def square(n):
    return n * n

main()


