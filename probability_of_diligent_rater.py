# probability_of_diligent_rater.py

# Probability that a rater is diligent
P_Diligent = 0.90

# Probability that a diligent rater labels a piece as good (non-spam)
P_G_4_Diligent = (0.80)**4

# Probability that a rater is non-diligent
P_Non_Diligent = 1 - P_Diligent

# Probability that a non-diligent rater labels a piece as good (non-spam)
P_G_4_Non_Diligent = 1.00**4

# Probability that a rater labels 4 pieces as good
P_G_4 = P_G_4_Diligent * P_Diligent + P_G_4_Non_Diligent * P_Non_Diligent

# Using Bayes' theorem to find the probability that a rater is diligent given G=4
P_Diligent_G_4 = (P_G_4_Diligent * P_Diligent) / P_G_4

print("Probability that a rater is diligent given G=4:", P_Diligent_G_4)
