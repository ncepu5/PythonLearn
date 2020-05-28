import json

# # 打印字典
# def displayInventory(inventory):
#     print
#     'Inventory：'
#     item_total = 0
#     for k, v in inventory.items():
#         print
#         str(v) + ' ' + k
#         item_total += v
#     print
#     'Total number of items:' + str(item_total)
#
# # 列表添加到字典
# def addToInventory(inventory,addItems):
#     for k in addItems:
#         if k in inventory.keys():
#             inventory[k]+=1
#         else:
#             inventory[k]=1
#     return  inventory
#
# if __name__ == '__main__':
#
#         inv = {'gold coin': 42, 'rope': 1}
#         print(inv)
#         # list = {'Google', 'Runoob', 1997, 2000}
#         dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#         inv = addToInventory(inv, dragonLoot)
#         print(inv)
#         displayInventory(inv)


# nid = "1,2"
# print(nid.split(','))
# datas = []
# for i in nid.split(','):
#     mydict = {}
#     mydict["id"] = str(i)
#     mydict["checked"] = True
#     datas.append(mydict)
# print(str(datas))


sex_dict = {"male": "0.3", "female": "-0.26"}

json_str = json.dumps(sex_dict)  # 将 Python 对象编码成 JSON 字符串
new_dict = json.loads(json_str)  # 用于将已编码的 JSON 字符串解码为 Python 对象

list = []
list.append(sex_dict)
list.append(sex_dict)

print(list)
list.clear()
print(list)

