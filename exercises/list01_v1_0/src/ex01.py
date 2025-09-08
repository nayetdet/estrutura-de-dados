from impl.linked_list import LinkedList

def remove_evens(l):
    if l is None or l.head is None:
        return l

    while l.head is not None and l.head.data % 2 == 0:
        l.head = l.head.next

    cur = l.head
    while cur is not None and cur.next is not None:
        if cur.next.data % 2 == 0:
            cur.next = cur.next.next
        cur = cur.next

    return l

def main():
    l = LinkedList([1, 2, 6, 13, 34])
    remove_evens(l)
    l.display()

if __name__ == "__main__":
    main()
