from factorial import factorial
from fibonacci import fibonacci

def main():
    n=int(input("enter a value"))
    print("Factorial of "+str(n)+":", factorial(n))
    print("First "+str(n)+" Fibonacci numbers:", fibonacci(n))

if __name__ == "__main__":
    main()
