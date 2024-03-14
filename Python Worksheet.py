
print("Exponent Calculator")
while True:
    
    number1 = int(input("First Number"))
    number2 = int(input("Second Number"))

    answer1 = number1 ** number2

    print(answer1)
    stop = input("Do you want to go again? yes or no: ")
    if stop == "no":
        break

print("1")
print("2 2")
print("3 3 3")
print("4 4 4 4")
print("5 5 5 5 5")

print("Range")

def print_numbers_between(start, end):
    if start <= end:
        for num in range(start, end + 1):
            print(num, end=", " if num < end else "\n")
    else:
        for num in range(start, end - 1, -1):
            print(num, end=", " if num > end else "\n")

number3 = int(input("Give a number"))
number4 = int(input("Give another number"))
print_numbers_between(number3, number4)

print("Primes")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_between(start, end):
    if start >= end:
        print("Invalid input: start number must be less than end number")
        return
    
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

start_num = int(input("Enter start number: "))
end_num = int(input("Enter end number: "))
print_primes_between(start_num, end_num)

print("Factorial")

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage:
number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is: {factorial(number)}")