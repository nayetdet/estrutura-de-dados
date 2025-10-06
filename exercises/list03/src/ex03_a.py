from impl.deque import Deque

def main():
    deque = Deque()
    deque.add_front(4)
    print("add_front(4) ->", deque.items)

    deque.add_rear(8)
    print("add_rear(8) ->", deque.items)

    deque.add_rear(9)
    print("add_rear(9) ->", deque.items)

    deque.add_front(5)
    print("add_front(5) ->", deque.items)
    print("peek_rear() ->", deque.peek_rear(), "| estado:", deque.items)
    print("remove_front() ->", deque.remove_front(), "| estado:", deque.items)
    print("remove_rear() ->", deque.remove_rear(), "| estado:", deque.items)

    deque.add_rear(10)
    print("add_rear(10) ->", deque.items)
    print("peek_front() ->", deque.peek_front(), "| estado:", deque.items)
    print("peek_rear() ->", deque.peek_rear(), "| estado:", deque.items)

    deque.add_rear(6)
    print("add_rear(6) ->", deque.items)
    print("remove_front() ->", deque.remove_front(), "| estado:", deque.items)

if __name__ == "__main__":
    main()
