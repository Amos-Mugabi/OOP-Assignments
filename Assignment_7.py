# write a  complete py program tht does the following.
# it aks th user to enter an integer n that is btwn 1 and 9.
# it repeatedly reads n from the user until the supplied value of n is legal.
# It prints out a picture of a triangle with n rows in which the symbol used to print each row is the row's number.
# example
# give me an integer btwn 1 and 9.5
# 1
# 33
# 555
# 323


def print_triangle(n):
    for i in range(1, n + 1):
        print(str(i) * i)

while True:
    try:
        n = int(input("Give me an integer between 1 and 9: "))
        if 1 <= n <= 9:
            print_triangle(n)
            break
        else:
            print("Please enter a valid integer between 1 and 9.")
    except ValueError:
        print("Invalid input. Please enter a valid integer between 1 and 9.")



