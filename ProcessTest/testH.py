
from multiprocessing import Process, Pipe
import time

# def producer(seq, p):
#     left, right = p
#     right.close()
#     for i in seq:
#         left.send(i)
#         # time.sleep(1)
#     else:
#         left.close()
#
# def consumer(p, name):
#     leftPipe, rightPipe = p
#     leftPipe.close()
#     while True:
#         try:
#             baozi = rightPipe.recv()
#             print('%s 收到包:%s' % (name, baozi))
#         except EOFError:
#             rightPipe.close()
#             break


def proc1(pipe):
    print(pipe)
    while True:
        for i in range(10000):
            print ("send: %s" %(i))
            pipe.send(i)
            time.sleep(1)

def proc2(pipe):
    print(pipe)
    while True:
        print ("proc2 rev:", pipe.recv())
        time.sleep(1)

if __name__ == "__main__":

    leftPipe = Pipe()
    rightPipe = Pipe()

    p1 = Process(target=proc1, args=(leftPipe[0], ))
    p1.start()

    p2 = Process(target=proc2, args=(leftPipe[1], ))
    p2.start()

    p1.join()
    p2.join()

    # c1 = Process(target=consumer, args=((leftPipe, rightPipe), 'c1'))
    # c1.start()
    #
    # seq = (i for i in range(10))
    # producer(seq, (leftPipe, rightPipe))
    #
    # rightPipe.close()
    # leftPipe.close()
    #
    # c1.join()