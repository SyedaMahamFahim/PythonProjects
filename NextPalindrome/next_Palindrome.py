def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


calories_list=[]
numbers=int(input("Enter the range  maximum  of list: "))
print("Enter the calories list: \n")
for i in range (1,numbers+1):
    calories=int(input(f"Enter the {i} number of calories list: "))
    calories_list.append(calories)

for i in range(numbers):
        print(
            f"Next palindrome for {calories_list[i]} is {next_palindrome(calories_list[i])}")