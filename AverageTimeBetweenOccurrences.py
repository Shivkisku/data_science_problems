def average_time_between_occurrences():
    # Probability of getting the given number on a single roll
    probability_single_roll = 1 / 6

    # Calculate the average time between occurrences
    average_time = 1 / probability_single_roll

    return average_time

# Example usage:
given_number = 3  # Replace with the desired number
result = average_time_between_occurrences()
print(f"The average time between occurrences of the number {given_number} is: {result:.2f} rolls")
