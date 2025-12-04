from multiprocessing import Value
from stack import arrayStack


class postfixEval:
    ##eval's postfix arithmetic expressions

    def evaluate(self, expression):
        stack = arrayStack
        tokens = expression.split()
        ##splits string by spaces to get nums/operators

        for token in tokens:
            if token in "+-*/":
                try:
                    right = stack.pop()
                    left = stack.pop()
                except IndexError:
                    raise ValueError("Error: Not enough operands for operator " + token ". Invalid expression.")

                result = 0
                if token == '+':
                    result = left + right
                elif token == '-':
                    result = left - right
                elif token == '*':
                    result = left*right
                elif token == '/':
                    if right == 0:
                        raise ValueError("ERROR: can't divide by zero. Phew, almost the end of the world right then.")
                    result = left/right

                #push result back to stack:
                stack.push(result)
            else:
                #for conversion of invalid input:
                try:
                    stack.push(float(token))
                except ValueError:
                    raise ValueError(f"Unknown token: {token}")
        #final result
        if len(stack) !=1:
            raise ValueError("Error: Too many operands left. Invalid expression.")
        return stack.pop()





