from stack import arrayStack
from postfix_eval import postfixEval
from infix_conv import in2postfixConv

if __name__=="__main__":
    converter = in2postfixConv()
    evaluator = postfixEval()

    print("---Infix>Postfix Test Program---")
    

    ##setting postfix list as per project instructions
    pftest1 = ["5 3 +","8 2 - 3 +","5 3 8 * +","6 2 / 3 +","5 8 + 3 -","5 3 + 8 *","8 2 3 * + 6 -","5 3 8 * + 2 /","8 2 + 3 6 * -","5 3 + 8 2 / -"]
    print("Testing postfix evaluation...\n")
    print(f"{'Expression':<20} | {'Result'}")
    print("-" * 30)

    for expr in pftest1:
        try:
            result = evaluator.evaluate(expr)
            print(f"{expr:<20} | {result}")
        except Exception as e:
            print(f"{expr:<20} | Error: {e}")

    i2ptest1 = ["A + B","A + B * C","( A + B ) * C","A * B + C / D","( A + B ) * ( C - D )","A + B * C - D / E","A * ( B + C ) / D","( A + B * C ) / ( D - E )","A + ( B - C ) * D","( A + B * ( C - D ) ) / E"]
    print("Testing infix to postfix converter...\n")
    print(f"{'Infix Expression':<30} | {'Postfix Result'}")
    print("-" * 60)

    for infix in i2ptest1:
        try:
            pfix = converter.convert(infix)
            print(f"{infix:<30} | {pfix}")
        except Exception as e:
            print(f"{infix:<30} | Error: {e}")
