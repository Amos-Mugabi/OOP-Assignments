
# Write a procedural python program that calculates the average of numbers between 1 to 50 and display the results. 
# Rewrite the program and convert it into an object-oriented version.

#  1. Procedural Program

def calculate_average():
    total = 0
    count = 0

    for number in range(1, 51):
        total += number
        count += 1

    average = total / count
    return average

result = calculate_average()
print("Average of numbers between 1 to 50 is:", result)





