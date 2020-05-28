from multiprocessing import Process, Pipe
import multiprocessing

def processFun1(conn,name):
    print(multiprocessing.current_process().pid,"进程发送数据：",name)
    conn.send(name)

def processFun2(conn, name):
    print(multiprocessing.current_process().pid, "接收数据：")
    print(conn2.recv())

if __name__ == '__main__':

    #创建管道
    conn1, conn2 = Pipe()
    # 创建子进程
    process1 = Process(target=processFun1, args=(conn1,"http://c.biancheng.net/python/"))
    process2 = Process(target=processFun2, args=(conn2, "http://c.biancheng.net/python/"))
    # 启动子进程
    process1.start()
    process2.start()
    process1.join()
    process2.join()
