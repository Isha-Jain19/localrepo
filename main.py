def greet(name):
    return f"Hello, {name}"

def square(n):
    return n * n

def cube(n):
    return n ** 3

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    name = input("Enter your name: ")
    print(greet(name))
    print("square of 3 is:", square(3))
    print("Cube of 3 is:", cube(3))
    print("Factorial of 5 is:", factorial(5))

if __name__ == "__main__":
    main()
