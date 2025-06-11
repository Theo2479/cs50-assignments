def einstein():
    x=int(input("give me the mass of an object in kg: "))  
    print("the energy or joules of said object is", equation(x))

def equation(n):
    return (300000000**2)*n

einstein()
