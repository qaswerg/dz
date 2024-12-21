def check_skobki(s):
    brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack = []
    for char in s:
        if char in brackets:
            top_element = stack.pop() if stack else None

            if brackets[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack