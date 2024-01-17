print("this solution is to find the root of an quadratic equation")
print("the equation is ax^2 + bx + c = 0")
a = float(input("enter the value of a: "))
b = float(input("enter the value of b: "))
c = float(input("enter the value of c: "))
determinant = b**2 - 4*a*c
root1 = (-b + determinant**0.5)/(2*a)
root2 = (-b - determinant**0.5)/(2*a)
print(f"the roots of the equation are: , {root1}",)
print(f"the roots of the equation are:, {root2} ",)
1