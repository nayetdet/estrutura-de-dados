from impl.queue import Queue

def main():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(3)
    queue.dequeue()
    queue.enqueue(2)
    queue.enqueue(8)
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(9)
    queue.enqueue(1)
    queue.dequeue()
    queue.enqueue(7)
    print(queue.items)

if __name__ == "__main__":
    main()
