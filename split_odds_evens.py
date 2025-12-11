from singly_linked_list import SinglyLinkedList

class SplitEO(SinglyLinkedList):
    def spleo(self):

        if self._SinglyLinkedList__head is None:
            raise SinglyLinkedList.EmptyListException()
        evenList = SinglyLinkedList()
        oddList = SinglyLinkedList()

        current = self._SinglyLinkedList__head

        self._SinglyLinkedList__head = None
        self._SinglyLinkedList__tail = None
        self._SinglyLinkedList__count = 0

        while current:
            next_node = current.next
            current.next = None

            if current.data % 2 == 0:
                if evenList._SinglyLinkedList__head is None:
                    evenList._SinglyLinkedList__head = current
                    evenList._SinglyLinkedList__tail = current

                else:
                    evenList._SinglyLinkedList__tail.next = current
                    evenList._SinglyLinkedList__tail = current
                evenList._SinglyLinkedList__count +=1

            else:
                if oddList._SinglyLinkedList__head is None:
                    oddList._SinglyLinkedList__head = current
                    oddList._SinglyLinkedList__tail = current

                else:
                    oddList._SinglyLinkedList__tail.next = current
                    oddList._SinglyLinkedList__tail = current
                oddList._SinglyLinkedList__count +=1

            #move on:
            current = next_node

        return evenList, oddList
