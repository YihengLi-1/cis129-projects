# Module 5 Lab-5
# Your Name: Yiheng Li
# Date: 2024-10-10
# Description: This program calculates the store and employee bonus based on monthly sales and sales increase percentages. 
# It then prints the bonus amounts and congratulates if the maximum bonus amounts are reached.

def main():
    # declare local variables
    monthlySales = 0.0  # monthly sales amount
    storeAmount = 0.0   # store bonus amount
    empAmount = 0.0     # employee bonus amount
    salesIncrease = 0.0 # percent of sales increase

    # call to getSales function
    monthlySales = getSales("Enter the monthly sales: ")

    # call to getIncrease function
    salesIncrease = getIncrease("Enter the percent of sales increase: ")

    # call to calcStoreBonus function
    storeAmount = calcStoreBonus(monthlySales)

    # call to calcEmpBonus function
    empAmount = calcEmpBonus(salesIncrease)

    # call to printBonus function
    printBonus(storeAmount, empAmount)


# This function gets the monthly sales
def getSales(prompt):
    monthlySales = float(input(prompt))  # Ask the user to input the monthly sales
    return monthlySales                  # Return the input as a float number


# This function gets the percent of increase in sales
def getIncrease(prompt):
    salesIncrease = float(input(prompt))  # Ask the user to input the sales increase percentage
    salesIncrease = salesIncrease / 100   # Convert percentage to decimal
    return salesIncrease                  # Return the sales increase


# This function determines the storeAmount bonus based on monthly sales
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount  # Return the calculated store bonus


# This function calculates the employee bonus based on the sales increase
def calcEmpBonus(salesIncrease):
    if salesIncrease >= 0.05:
        empAmount = 75
    elif salesIncrease >= 0.04:
        empAmount = 50
    elif salesIncrease >= 0.03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount  # Return the calculated employee bonus


# This function prints the bonus information and checks for the highest bonus
def printBonus(storeAmount, empAmount):
    # Print the store and employee bonus amounts
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $", empAmount)
    
    # If both store and employee bonuses are at their maximum, print a congratulatory message
    if storeAmount == 6000 and empAmount == 75:
        print("Congrats! You have reached the highest bonus amounts possible!")


# Start the program
main()