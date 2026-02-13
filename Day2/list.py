nums = list(map(int, input("Enter numbers separated by space: ").split()))

even = [n for n in nums if n % 2 == 0]
odd = [n for n in nums if n % 2 != 0]

print("Even numbers:", even)
print("Odd numbers:", odd)
