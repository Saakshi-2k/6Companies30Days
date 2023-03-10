# Leetcode problem:150- Evaluate reverse polish notation 
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(token))

        return stack[0]
