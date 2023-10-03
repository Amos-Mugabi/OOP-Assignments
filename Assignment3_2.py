#  2. Object Oriented Version
class AverageCalculator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def calculate_average(self):
        total = 0
        count = 0

        for number in range(self.start, self.end + 1):
            total += number
            count += 1

        average = total / count
        return average

calculator = AverageCalculator(1, 50)
result = calculator.calculate_average()
print("Average of numbers between 1 to 50 is:", result)




