from multiprocessing import Process, Pipe
import time
import json

def consumer(p, name):
    left,right=p
    left.close()
    while True:
        try:
            listBao=right.recv()
            print('%s 收到包:%s' %(name, listBao))
            for i in range(len(listBao)):
                # print("list序号：%s   值：%s" % (i + 1, listBao[i]))
                dict = listBao[i]
                print(dict['imgPath'])

        except EOFError:
            right.close()
            break

if __name__ == "__main__":
    left, right = Pipe() #从第一个参数向第二个参数发送数据
    c1 = Process(target=consumer, args=((left, right), 'c1'))
    c1.start()

    while True:
        print("准备发送数据")
        time.sleep(1)
        # left.send("123456")
        # # seq = (1 for i in range(10))
        # # list = [1 for i in range(10)]

        list = []

        sex_dict = {
    "person_id": "4564afd564164afdafdF",
    "person_info": {
        "male": "0.3",
        "female": "-0.26",
        "age16less,": "-0.26",
        "age16_30Count": "-0.26",
        "age30_45Count": "-0.26",
        "age45_60Count": "-0.26",
        "age60moreCount": "-0.26"
    },
    "boundingBoxes": [
        {
            "x": 517,
            "y": 255,
            "width": 144,
            "height": 389
        },
        {
            "x": 572,
            "y": 265,
            "width": 125,
            "height": 369
        }
    ],
    "imgPath": "sss/aaa/4564afd5aaaaaaaaaafdF.png"
}

        json_str = json.dumps(sex_dict)  # 将 Python 对象编码成 JSON 字符串
        new_dict = json.loads(json_str)  # 用于将已编码的 JSON 字符串解码为 Python 对象

        list.append(sex_dict)
        list.append(sex_dict)

        left.send(list)
        list.clear()
