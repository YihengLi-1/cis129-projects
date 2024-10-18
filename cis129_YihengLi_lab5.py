# Lab 5 The Bottle Return Program

# Step 1: Declare variables below
total_bottles = 0
counter = 1
today_bottles = 0
total_payout = 0
keep_going = "y"

# Step 2: Loop to run program again
while keep_going == "y":
    # Step 3: Code to set value of variables
    for day in range(1, 8):
        today_bottles = int(input(f"Enter number of bottles returned for day #{day}: "))
        total_bottles += today_bottles

    total_payout = total_bottles * 0.10

    # Print the results
    print(f"The total number of bottles collected is {total_bottles}")
    print(f"The total paid out is ${total_payout:.2f}")

    # Ask if the user wants to enter another week's worth of data
    keep_going = input("Do you want to enter another week's worth of data? (Enter y or n): ")
    
