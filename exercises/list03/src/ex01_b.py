from impl.queue import Queue

def main():
    queue = Queue()
    queue.enqueue(7)
    queue.enqueue(3)
    queue.dequeue()
    queue.enqueue(5)
    queue.enqueue(9)
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(19)
    queue.enqueue(1)
    queue.dequeue()
    queue.dequeue()
    print(queue.items)

if __name__ == "__main__":
    main()
