# REMOVING DUPLICATES IN THE LIST


numbers = [1, 2, 3, 2, 6, 7]  # Define a list of numbers
uniques = []  # Initialize an empty list to store unique numbers

# Iterate through each number in the 'numbers' list
for number in numbers:
    # Check if the current number is not already in the 'uniques' list
    if number not in uniques:
        # If the number is not in 'uniques', append it to the list
        uniques.append(number)

# Print the list containing unique numbers
print(uniques)
