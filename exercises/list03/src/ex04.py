from impl.deque import Deque
from impl.queue import Queue

def main():
    deque = Deque([1, 2, 3, 4, 5, 6, 7, 8])
    queue = Queue()

    while not deque.is_empty():
        value = deque.peek_front()
        queue.enqueue(value)
        deque.remove_front()

    print(f"Queue: {queue.items}")

if __name__ == "__main__":
    main()
