
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    class EmptyListException(Exception):
        pass

    class NodeNotFoundException(Exception):
        pass

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def build_forward_list(self, iterable):
        for item in iterable:
            self.__append(item)

    def build_backward_list(self, iterable):
        for item in iterable:
            self.__prepend(item)

    def __append(self, value):

        new_node = Node(value)

        if self.__head is None:
            self.__head = self.__tail = new_node

        else:
            self.__tail.next = new_node
            self.__tail = new_node
            self.__count += 1

    def __prepend(self, value):
        new_node = Node(value)
        new_node.next = self.__head
        self.__head = new_node
        if self.__tail is None:
            self.__tail = new_node
        self.__count += 1

    def insert_after(self, after_value, new_value):
        if self.__head is None:
            raise SinglyLinkedList.EmptyListException()
        current = self.__head
        while current and current.data != after_value:
            current = current.next
        if current is None:
            raise SinglyLinkedList.NodeNotFoundException()

        new_node = Node(new_value)
        new_node.next = current.next
        current.next = new_node
        if current == self.__tail: #if inserted at end of list
            self.__tail = new_node #re-route the tail pointer
        self.__count += 1

    def remove(self, value):
        if self.__head is None:
            raise SinglyLinkedList.EmptyListException()
        current = self.__head
        previous = None
        while current and current.data != value:
            previous = current
            current = current.next
        if current is None:
            raise SinglyLinkedList.NodeNotFoundException()
        if previous is None:
            self.__head = current.next #remove first node
        else:
            previous.next = current.next #remove an interior node
        if current == self.__tail:
            self.__tail = previous #remove the last node
            self.__count -= 1

    def remove_all(self, value):
        if self.__head is None:
            return

        while self.__head and self.__head.data == value:
            self.__head = self.__head.next
            self.__count -= 1
        
        if self.__head is None:
            self.__tail = None
            return

        current = self.__head
        while current.next:
            if current.next.data == value:

                current.next = current.next.next
                self.__count -= 1

                if current.next is None:
                    self.__tail = current
            else:

                current = current.next

    def display(self):
        current = self.__head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    def display_reverse(self):
        def _reverse_recursive(node):
            return _reverse_recursive(node.next) + [node.data] if node else []
        print(" <- ".join(map(str,_reverse_recursive(self.__head))))

    def display_reverse_nr(self): #nonrecursive
        stack = []
        current = self.__head
        
        while current:
            stack.append(current.data)
            current = current.next
            
        output_parts = ["None"]
        while stack:
            output_parts.append(str(stack.pop()))
        output_parts.append("Head")
        
        print(" <- ".join(output_parts))

    def __iter__(self):
        current = self.__head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        return self.__count
    
