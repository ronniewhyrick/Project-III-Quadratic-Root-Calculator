#Ron Whyrick
#Project 3: Root Calculator

#Description*************************************************************************************************************
#Completed part 1 of a two part project
##simple root calculator that only work with quadratic equations. 

#Prelude
import cmath

#Iteration
def main():
    global s,r1,r2
    #Program Start
    print("Welcome to the root calculator")
    print("Plug in the Corresponding Coefficients for Y = aX^2 + bX + C")
    #inputs
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    #Arithmetic 
    s = cmath.sqrt(b**2 - 4*a*c)
    r1 = (-1*b + s)/(2*a)
    r2 = (-1*b - s)/(2*a)
    #Classify
    if s.imag == 0.0:
        trivial()
    else:
        cmplx()
        
#Classifying functions
#Real Roots
def trivial():
    global s,r1,r2
    print("Your root is not Complex")
    r1 = str(r1.real)
    r2 = str(r2.real)
    print("1st root is = " + r1 + "\n2nd root is = " + r2)
#Complex Roots     
def cmplx():
    global s,r1,r2
    r1 = str(r1)
    r2 = str(r2)
    print("Your Root is Complex")
    print("1st root is = " + r1 + "\n2nd root is = " + r2)
#Declarations 
if __name__=="__main__":
    main()
