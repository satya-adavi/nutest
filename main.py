from factorial import factorial
from fibonacci import fibonacci
from temp import func1
from temp import func2
import threading
from file_read import read_input_from_file
import os

def main():
    n=int(input("enter a value"))
    print("Factorial of "+str(n)+":", factorial(n))
    print("First "+str(n)+" Fibonacci numbers:", fibonacci(n))

    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Checking current directory",os.curdir)
    input_file_path = os.path.join(os.curdir, 'sub_folder', 'inp.txt')
    inputs = read_input_from_file(input_file_path)
    print(inputs)


if __name__ == "__main__":
    main()

