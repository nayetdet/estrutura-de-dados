from impl.linked_list import LinkedList

def get_len(l):
    s = 0
    if l is None or l.head is None:
        return s
    
    cur = l.head
    while cur is not None:
        s += 1
        cur = cur.next

    return s

def divide(l):
    if l is None or l.head is None:
        return None, None

    tam = get_len(l)
    cur = l.head

    l1 = LinkedList()
    l1_tam = tam // 2
    for _ in range(l1_tam):
        l1.append(cur.data)
        cur = cur.next
    
    l2 = LinkedList()
    l2_tam = l1_tam + (tam % 2)
    for _ in range(l2_tam):
        l2.append(cur.data)
        cur = cur.next
    
    return l1, l2

def main():
    l = LinkedList([1, 2, 6, 13, 34])
    l1, l2 = divide(l)
    l1.display()
    l2.display()

if __name__ == "__main__":
    main()
