# Define key metrics
average_customer_acquisition_cost = 1000  # Average cost of acquiring a customer
expected_customer_lifetime_value = 1500  # Expected value of a customer over their lifetime

# Calculate the ROI (Return on Investment)
roi = (expected_customer_lifetime_value - average_customer_acquisition_cost) / average_customer_acquisition_cost

# Interpretation and suggestion
if roi > 0:
    interpretation = "The company is generating a positive ROI for customer acquisition."
    suggestion = "Consider increasing the customer acquisition budget to acquire more customers."
else:
    interpretation = "The company is not generating a positive ROI for customer acquisition."
    suggestion = "Evaluate the efficiency of customer acquisition channels and strategies."

# Print the results
print("Interpretation:")
print(interpretation)
print("\nSuggestion:")
print(suggestion)
print("\nROI (Return on Investment): {:.2%}".format(roi))
