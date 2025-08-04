def greet(name):
    print(f"Hello, {name}!")

def square(n):
    return n * n

def main():
    name = input("Enter your name: ")
    greet(name)
    print("Square of 5 is:", square(5))

if __name__ == "__main__":
    main()
