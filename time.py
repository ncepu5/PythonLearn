
import time

if __name__ == '__main__':
    print(time.time())
    a = int(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
    print(type(a))
    b = '%d' % int(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
    print(type(b))
    print('%d' % int(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))))
    # c = int(time.strftime('%Y%m%d', time.localtime(time.time())))
    c = '%d' % int(time.strftime('%Y%m%d', time.localtime(time.time())))
    print(c)