
def sum_values_two_list (A,B):
    if A.len() != B.len():
        return None
    else:
        summ_list = LinkedList()
        current1 = A.head
        current2 = B.head
    while current1 and current2:
        summ = current1.value + current2.value
        summ_list.add_in_tail(Node(summ))
        current1 = current1.next
        current2 = current2.next
    if current1 is None:
        while current2:
            summ_list.add_in_tail(Node(current2.value))
            current2 = current2.next
    else:
        while current1:
            summ_list.add_in_tail(Node(current1.value))
            current1 = current1.next
    return summ_list


