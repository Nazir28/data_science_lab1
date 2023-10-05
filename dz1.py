from core import Node, print_linked_list
def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def run_dz_1():
    h, a, b, c, d = Node(1), Node(2), Node(3), Node("Внезапно"), Node(5)
    h.next = a
    a.next = b
    b.next = c
    c.next = d
    print("Задача 1 Связанные списки:")
    print_linked_list(h)

    new_head = reverse_linked_list(h)

    print("---")
    print("Развёрнутый связный список:")
    print_linked_list(new_head)
