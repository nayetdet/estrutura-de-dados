from impl.linked_list import LinkedList

def get_even_sum(l):
    s = 0
    if l is None or l.head is None:
        return s

    cur = l.head
    while cur is not None:
        if cur.data % 2 == 0:
            s += cur.data
        cur = cur.next

    return s

def main():
    l = LinkedList([1, 2, 6, 13, 34])
    l.display()
    print(get_even_sum(l))

if __name__ == "__main__":
    main()
