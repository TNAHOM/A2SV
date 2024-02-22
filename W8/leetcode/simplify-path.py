class Solution:
    def simplifyPath(self, path: str) -> str:
        #** . -> current directory
        #** .. -> up level
        #** /// -> /
        # .... -> 

        split_ = path.split('/')
        stack = []
        split_ = list(filter(lambda x: len(x) > 0, split_))
        print(split_)
        for x in split_:
            print(x)
            # stack.append('/')
            if x == '.':
                continue
            elif stack and x == '/' and stack[-1] == '/':
                stack.pop()
                continue
            elif x[0] == '.' and x[1]== '.' and len(x) == 2:
                if stack:
                    stack.pop()
                continue
            stack.append(x)

        print(stack)
        return '/' +'/'.join(stack)