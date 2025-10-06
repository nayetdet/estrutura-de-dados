from impl.queue import Queue

def main():
    queue = Queue()
    queue.enqueue(71)
    queue.enqueue(31)
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(9)
    queue.dequeue()
    queue.dequeue() # ERRO!
    queue.dequeue()
    queue.enqueue(1)
    queue.enqueue(20)
    queue.dequeue()
    print(queue.items)

if __name__ == "__main__":
    main()
