class Node:
    def __init__(self, date):
        self.date = date
        self.next = None


def insertionSort(head):
    sorted_head = None
    current = head

    while current:
        new_node = current.next
        if sorted_head is None or current.date < sorted_head.date:
            current.next = sorted_head
            sorted_head = current
        else:
            temp = sorted_head
            while temp.next and temp.next.date < current.date:
                temp = temp.next
            current.next = temp.next
            temp.next = current
        current = new_node

    return sorted_head


def printList(head):
    while head:
        print(head.date)
        head = head.next
    print("None")


head = Node(3)
head.next = Node(1)
head.next.next = Node(2)

print("Danh sach ban dau:")
printList(head)

head = insertionSort(head)

print("Danh sach sau khi sap xep:")
printList(head)
