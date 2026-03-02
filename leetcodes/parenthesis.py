def is_balanced(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in bracket_map.values():  # Opening bracket
            stack.append(char)
        elif char in bracket_map:  # Closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        # Ignore non-bracket characters if needed

    return not stack  # True if stack is empty (all matched)

# Example usage
print(is_balanced("([])"))     # True
print(is_balanced("([)]"))     # False
print(is_balanced("{[()]}"))   # True
print(is_balanced("((("))      # False
