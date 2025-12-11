from stack import arrayStack
from postfix_eval import postfixEval
from infix_conv import in2postfixConv
from singly_linked_list import SinglyLinkedList

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


print("----Building forward list----\n")
sll_fwd = SinglyLinkedList()
sll_fwd.build_forward_list([10,20,30,40,50])
sll_fwd.display()

print(">>>>Deleting first node: ", end="")
sll_fwd.remove(10)
sll_fwd.display()

print(">>>>Deleting last node: ", end="")
sll_fwd.remove(50)
sll_fwd.display()

print(">>>>Deleting interior node: ", end="")
sll_fwd.remove(30)
sll_fwd.display()
print("\n----------------------------\n")

print("----Building backwards----\n")
sll_back = SinglyLinkedList()
sll_back.build_backward_list([10,20,30,40,50])
sll_back.display()

print(">>>>Deleting first node: ", end="")
sll_back.remove(50)
sll_back.display()

print(">>>>Deleting last node: ", end="")
sll_back.remove(10)
sll_back.display()

print(">>>>Deleting interior node: ", end="")
sll_back.remove(30)
sll_back.display()
print("\n----------------------------\n")

print("----Nonrecursive reverse printing----\n")
sll_rev = SinglyLinkedList()
sll_rev.build_forward_list([1,2,3,4,5])

print("\n>>>>Insertion order: ", end="")
sll_rev.display()

print("\n>>>>Reverse order (recursive): ", end="")
sll_rev.display_reverse()

print("\n>>>>Reverse (nonrecursive): ", end="")
sll_rev.display_reverse_nr()
print("\n----------------------------\n")

print("----Remove test----\n")
sll_remall = SinglyLinkedList()
sll_remall.build_forward_list([1,3,7,3,4,8,1])
sll_remall.display()

print(">>>>Removing 1+dupes\n")
sll_remall.remove_all(1)
sll_remall.display()

print("\n>>>>Removing 7+dupes\n")
sll_remall.remove_all(7)
sll_remall.display()
print("\n----Singly Linked List Test Done----\n")