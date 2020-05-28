from multiprocessing import Process, Queue


def Child_Process(queue):
    for i in range(10):
        queue.put("Data From Child Process", i)


if __name__ == '__main__':
    for i in range(6, 10):
        print(i)

    q = Queue()
    p = Process(target=Child_Process, args=(q,))
    p.start()
    print(q.get())
    p.join()