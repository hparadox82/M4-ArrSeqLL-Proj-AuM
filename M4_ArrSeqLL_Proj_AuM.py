from stack import arrayStack
from postfix_eval import postfixEval
from infix_conv import in2postfixConv
from singly_linked_list import SinglyLinkedList
from split_odds_evens import SplitEO

if __name__=="__main__":

    print("----Split Even Odd Test----\n    |Building list...\n")
    split_list=SplitEO()
    data2 = [11, 25, 32, 42, 57, 64, 79]
    split_list.build_forward_list(data2)

    print(">>>>Original list: ")
    split_list.display()

    print("\n>>>>Splitting....")
    evens, odds = split_list.spleo()

    print("\n>>>>Evens: \n")
    evens.display()

    print("\n>>>>Odds: \n")
    odds.display()

    print("\n>>>>Verifying that list is empty....\n     |If nothing is displayed, then the list is empty!")
    split_list.display()