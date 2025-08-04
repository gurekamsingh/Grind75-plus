#problem:
# Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN).
# The expression is given as a list of strings, where each string is either an operator (+, -, *, /) or an integer.
# The operators apply to the two most recent numbers in the stack.
# Approach:
# Use a stack to keep track of numbers.
# For each token:
# - If it's a number, push it onto the stack.
# - If it's an operator, pop the two top numbers from the stack, apply the operator, and push the result back onto the stack.
# At the end, the stack will contain one element which is the result.


class Solution:
    def evalRPN(self, tokens: str) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(b - a)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack[0]

# Example usage:
tokens = ["2", "1", "+", "3", "*"]
solution = Solution()
print(solution.evalRPN(tokens))  # Output: 9

# time complexity: O(n) where n is the number of tokens
# space complexity: O(n) for the stack
# This approach uses a stack to evaluate the expression in reverse Polish notation, ensuring that operations are applied in the correct order.

# brute force approach:
# We can also use a brute force approach by iterating through the tokens and applying the operations directly, but this would be less efficient and more complex to manage.
# The stack-based approach is preferred for its clarity and efficiency.