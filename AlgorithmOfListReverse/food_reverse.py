"""
The task you have to perform is “Foods and Calories.” This task consists of a total of 15 points to evaluate your performance.

Problem Statement:-
You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount of calories. You have to reserve this list of food items containing calories.

You have to use the following three methods to reserve a list:

Inbuild method of python
List name [::-1] slicing trick
Swap the first element with the last one and second element with second last one and so on like,
[6 7 8 34 5] -> [5 34 8 7 6]

Input:
Take a list as an input from the user

[5, 4, 1]

Output:
[1, 4, 5]

[1, 4, 5]

[1, 4, 5]

All three methods give the same results!
"""

def Reverse(calories_list):
    if (len(calories_list)==1):
        return calories_list
    return Reverse(calories_list[1:]) + calories_list[0:1]

def build(calories_list):
    calories_list.reverse()
    return calories_list


calories_list=[]
numbers=int(input("Enter the range  maximum  of list: "))
print("Enter the calories list: \n")
for i in range (1,numbers+1):
    calories=int(input(f"Enter the {i} number of calories list: "))
    calories_list.append(calories)

print(f"\nThe actual list is : {calories_list}")

#By creating a new method
print("\nBy using recursion: ",end='')      
print(Reverse(calories_list)) 

#By using in built method 
print("By using built-in reverse method: ",end='')
print(build(calories_list)) 

#By using slicing method 
slicing=calories_list[::-1]
print(f"By using slicing method: {slicing}")