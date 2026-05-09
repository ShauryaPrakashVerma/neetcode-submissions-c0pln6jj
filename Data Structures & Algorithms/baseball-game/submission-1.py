class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sums = 0

        for i in operations:
            if i.lstrip("-").isdigit():
                stack.append(int(i))
            elif i == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
            elif i == "C":
                stack.pop()
            elif i == "D":
                stack.append(2 * int(stack[-1]))
        
        for i in stack:
            sums += i
        return sums