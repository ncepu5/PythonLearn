
import time
from py2neo import Graph #pip install py2neo

print(time.time())


a = int(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
print(type(a))

b = '%d' % int(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
print(type(b))
print('%d' % int(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))))



# c = int(time.strftime('%Y%m%d', time.localtime(time.time())))
c = '%d' % int(time.strftime('%Y%m%d', time.localtime(time.time())))
print(c)



graph = Graph('bolt://172.18.33.8:7687', username='neo4j', password='casia@1234')
cql = 'merge (n:Person16Ceng{person_id:123456})'
graph.run(cql)

cqlSelect = 'MATCH(n: Day:Person16Ceng{day:' + '%d' % int(time.strftime('%Y%m%d', time.localtime(time.time()))) +'}) RETURN n LIMIT 25'
g = graph.run(cqlSelect ).data()
print(g.__len__())
if g.__len__() == 0:
    graph.run('merge (n:Day:Person16Ceng{day:' + '%d' % int(time.strftime('%Y%m%d', time.localtime(time.time()))) +'})')
else:
    for i in g:
        print(i)

# 创建关系
# match (a:Day:Person16Ceng{day:20200429}), (b:Person16Ceng{person_id:123456}) merge (a)-[r:INCLUDES_PERSON{DataType:'Person16Ceng'}]->(b) return r
relationCql = 'match (a:Day:Person16Ceng{day:' + '%d' % int(time.strftime('%Y%m%d', time.localtime(time.time()))) + '}), (b:Person16Ceng{person_id:123456}) merge (a)-[r:INCLUDES_PERSON{DataType:"Person16Ceng"}]->(b) return r'
g = graph.run(relationCql).data()