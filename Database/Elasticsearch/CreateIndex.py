#! -*- encoding:utf-8 -*-
"""
@File    :   CreateIndex.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   https://blog.csdn.net/Herbe_chanceux/article/details/108761823
"""


from elasticsearch import Elasticsearch

es = Elasticsearch()

def deleteInices(my_index):
    if True and es.indices.exists(my_index):  # 确认删除再改为True
        print("delete is complete")
        es.indices.delete(index=my_index)


def createIndex(index_name):
    # index settings
    settings = {
        "mappings":{
            "properties": {
                        "id": {"type": "integer"},
                        "sentence": {"type": "text"},
                        "entity":{"type":"text"},
                    }
        }
    }
    # create index
    es.indices.create(index=index_name, body=settings)
    print("creating index is succeed!")

if __name__ == "__main__":
    # deleteInices('wiki-index')
    createIndex('wiki-index')
    # createIndex('wiki-index', 'my doc2')  
    # deleteInices('my_index')

