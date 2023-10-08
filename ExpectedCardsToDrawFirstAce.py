expected_cards = 0
remaining_non_aces = 48  # Initial number of non-ace cards remaining

for draw_number in range(1, 53):
    probability_non_ace = remaining_non_aces / (52 - draw_number + 1)
    expected_cards += probability_non_ace * draw_number
    remaining_non_aces -= 1

print(f"Expected number of cards to draw before seeing the first ace: {expected_cards:.2f}")
