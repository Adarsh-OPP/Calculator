def addition(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

def division(a, b):
    print(a / b)

def multiplication(a, b):
    print(a * b)

def square(a):
    print(a**2)

def cube(a):
    print(a**3)

def main():
    while True:
        print(
            "Addition = 1\n"
            "Subtraction = 2\n"
            "Division = 3\n"
            "Multiplication = 4\n"
            "Squaring = 5\n"
            "Cubing = 6\n"
            "Exit = 0"
        )
        
        choose = int(input("What you want to do: "))

        if choose == 1:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            addition(a, b)
        elif choose == 2:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            subtract(a, b)
        elif choose == 3:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            division(a, b)
        elif choose == 4:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            multiplication(a, b)
        elif choose == 5:
            a = int(input("Enter the number: "))
            square(a)
        elif choose == 6:
            a = int(input("Enter the number: "))
            cube(a)
        elif choose == 0:
            print("EXITING.....")
            break
        else:
            print("Enter the right operation number")

main()
