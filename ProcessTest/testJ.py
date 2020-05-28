from multiprocessing import Process,Pipe
import time

def f(conn):
    seq = (i for i in range(10))
    for i in range(10):
        time.sleep(2)
        # print("send:", i)
        conn.send([i, 'test', None])
    # print(conn.recv())
    conn.close()

if __name__ == "__main__":
    left, right = Pipe() #产生两个返回对象，一个是管道这一头，一个是另一头
    p = Process(target=f, args=(right,))
    p.start()

    while True:
        print ("rev:", left.recv())
        time.sleep(1)

    # parent_conn.send('father test')

    p.join()
