def minRemoveToMakeValid(s):
    # Create a stack to keep track of indices of opening parentheses
    stack = []
    
    # Create a set to store the indices of parentheses to be removed
    to_remove = set()
    
    # Iterate through the string and mark the parentheses to be removed
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                to_remove.add(i)
    
    # Add remaining unmatched opening parentheses to the set
    to_remove.update(stack)
    
    # Construct the valid string by excluding characters at indices in to_remove
    result = []
    for i, char in enumerate(s):
        if i not in to_remove:
            result.append(char)
    
    # Convert the result list to a string and return it
    return ''.join(result)

# Example usage
input_string = ")a(b((cd)e(f)g)"
result = minRemoveToMakeValid(input_string)
print(result)  # Output: "ab((cd)e(f)g)"
