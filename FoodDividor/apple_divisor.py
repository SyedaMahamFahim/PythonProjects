"""
The task you have to perform is “Divide the Apples.” This task consists of a total of 10 points to evaluate your performance.

Problem Statement:-
Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to distribute the apples. These “n” number of apples is provided to harry by his friends, and he can request for few more or few less apples.

You need to print whether a number is in range mn to mx, is a divisor of “n” or not.

Input:

Take input n, mn, and mx from the user.

Output:
Print whether the numbers between mn and mx are divisor of “n” or not. If mn=mx, show that this is not a range, and mn is equal to mx. Show the result for that number.

Example:
If n is 20 and mn=2 and mx=5

2 is a divisor of20

3 is not a divisor of 20

…

5 is a divisor of 20

"""

no_of_apples=int(input("Enter the numbers of apple Harry has got: "))
mini_students=int(input("Enter the minimum numbers of students: "))
max_students=int(input("Enter the maximum numbers of students: "))
for i in range(mini_students,max_students+1):
    if no_of_apples%i==0:
        print(f"{i}  is a divisor of {no_of_apples}")
    else:
        print(f"{i}  is not a divisor of {no_of_apples}")

