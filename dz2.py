from core import Node, print_linked_list

def insert_sort_linked_list(head):
    if not head or not head.next:
        return head
    dummy = Node()
    current = head
    while current:
        prev = dummy
        next_node = current.next

        while prev.next and prev.next.value < current.value:
            prev = prev.next

        current.next = prev.next
        prev.next = current

        current = next_node

    return dummy.next


node4, node2, node1, node3 = Node(4), Node(2), Node(1), Node(3)
node4.next, node2.next, node1.next = node2, node1, node3

def run_dz_2():
    print("Задача 2 Пузырьки")
    print("Исходный несортированный связанный список:")
    print_linked_list(node4)

    # Сортируем связанный список
    sorted_head = insert_sort_linked_list(node4)

    print("---")
    print("Отсортированный связанный список:")
    print_linked_list(sorted_head)
