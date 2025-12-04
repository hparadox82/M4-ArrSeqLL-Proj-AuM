from postfix_eval import Value
from stack import arrayStack


class in2postfixConv:
    ##converts infix > postfix expressions using stack
    def __init__(self):
        self.precedence = {'+':1, '-':1, '*':2, "/":2}
        ##defines operator precedence; higher num = higher precedence.

    def convert(self, expression):
        stack = arrayStack()
        output = []
        tokens = expression.split()
        ##converts space sep'd infix string to postfix

        for token in tokens:

            #add to output if operand
            if token not in self.precedence and token not in "()":
                output.append(token)
            #push to stack if "("
            elif token == '(':
                stack.push(token)
            #if ")", pop until find matching "("
            elif token == ')':
                try:
                    top_token = stack.pop()
                    while top_token !='(':
                        output.append(top_token)
                        top_token = stack.pop()
                except IndexError:
                    raise ValueError("Error: Mismatched parenthesis.")

            #push current if pops operator with >= precedence
            elif token in self.precedence:
                while (not stack.is_empty() and stack.top() !='(' and self.precedence[stack.top()] >= self.precedence[token]):
                    output.append(stack.pop())
                stack.push(token)
            else:
                raise ValueError(f"Error: Unknown token '{token}'")
        
        #pop remaining operators
        while not stack.is_empty():
            top_token = stack.pop()
            if top_token == '(':
                raise ValueError("Error: Mismatched parenthesis; missing ')'.")
            output.append(top_token)
        return " ".join(output)



