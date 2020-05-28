
from multiprocessing import Process, Pipe
import time
import random


def runAttribute(name):
    print("2222222222222222222")
    #
    time.sleep(random.randrange(1, 5))
    print("3333333333333333")

def producer(seq, p):
    left, right = p
    right.close()
    for i in seq:
        left.send(i)
        # time.sleep(1)
    else:
        left.close()

def consumer(p, name):
    leftPipe, rightPipe = p
    leftPipe.close()
    while True:
        try:
            baozi = rightPipe.recv()
            print('%s 收到包:%s' % (name, baozi))
        except EOFError:
            rightPipe.close()
            break

if __name__ == "__main__":

    leftPipe, rightPipe = Pipe()

    Process(target=runAttribute, args=(leftPipe,)).start()

    c1 = Process(target=consumer, args=((leftPipe, rightPipe), 'c1'))
    c1.start()

    seq = (i for i in range(10))
    producer(seq, (leftPipe, rightPipe))

    rightPipe.close()
    leftPipe.close()

    c1.join()