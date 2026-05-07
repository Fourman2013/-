import random
name = input()
age = input()
print(f"Привіт {name}, тобі {age}!")

age_check = int(input())
if age_check >= 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")

number = random.randint(1, 10)
for i in range(3):
    guess = int(input())
    if guess == number:
        print("Вітаю! Ти вгадав!")
        break
    elif guess > number:
        print("Менше")
    else:
        print("Більше")

start = int(input())
end = int(input())
for i in range(start, end + 1):
    print(i, end=" ")
print()

n_even = int(input())
if n_even % 2 != 0:
    n_even -= 1
for i in range(n_even, 1, -2):
    print(i, end=" ")
print()

n_fact = int(input())
factorial = 1
for i in range(1, n_fact + 1):
    factorial *= i
print(factorial)
