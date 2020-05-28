#所有进程都是由父进程启动的


import multiprocessing
import os


def show_info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id', os.getpid())
    print('\n\n')


def fffff(name):
    show_info('function fffff')
    print(name)


if __name__ == '__main__':
    show_info('main process line')
    p = multiprocessing.Process(target=fffff, args=('children process', ))
    p.start()