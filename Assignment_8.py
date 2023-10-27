# Jane owns a money lending business called Save To Grow Credit that loans out money. 
# A given client of this company is given a loan that has to be repaid in a months time (30 days) or less days with 10% interest. 
# If the client fails to pay at the end of 30 days, the client is charged a fine of 1% of the loan per day. 
# Write a python application that determines the total amount that is paid by the client to the company after a given number of days?


print("Save To Grow Credit.")

name = input("Enter client name:")
amount = int(input("Enter amount of loan :"))
duration = int(input("Enter days taken with the loan:"))


if duration <= 30 :
    total = (amount * 10/100 ) + amount
    print("Total amount of ", name , "is: ", total)
if duration >= 30 :
    extra_days = duration - 30
    total = (amount * 1/100 * extra_days) + amount
    print("Total amount of ", name , "is: ", total)
    



    