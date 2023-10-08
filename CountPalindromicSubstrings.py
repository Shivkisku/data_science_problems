def is_palindrome(s):
    # Check if a string s is a palindrome
    return s == s[::-1]

def count_palindromic_substrings(s):
    count = 0

    # Iterate through all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if is_palindrome(substring):
                count += 1

    return count

# Example usage:
input_string = "aba"
result = count_palindromic_substrings(input_string)
print(f"The count of palindromic substrings in '{input_string}' is {result}")
