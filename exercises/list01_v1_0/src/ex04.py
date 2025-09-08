from impl.linked_list import LinkedList

def merge(l1, l2):
    l = LinkedList()
    cur1 = l1.head if l1 else None
    cur2 = l2.head if l2 else None

    while cur1 is not None or cur2 is not None:
        if cur1 is not None:
            l.append(cur1.data)
            cur1 = cur1.next

        if cur2 is not None:
            l.append(cur2.data)
            cur2 = cur2.next

    return l

def main():
    l1 = LinkedList([1, 2, 3])
    l2 = LinkedList([4, 5, 6])
    l = merge(l1, l2)
    l.display()

if __name__ == "__main__":
    main()
