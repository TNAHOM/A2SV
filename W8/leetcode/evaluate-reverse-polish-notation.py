class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # print(''.isnumeric())
        for x in tokens:
            if x not in ('*', '/', '-', '+'):
                stack.append(int(x))
            else:

                first = stack.pop()
                second = stack.pop()

                if x == '+':
                    stack.append(first+second)
                elif x == '-':
                    stack.append(second-first)
                elif x == '*':
                    stack.append(first*second)
                elif x == '/':
                    stack.append(int(second/first))
        
        return stack[0]