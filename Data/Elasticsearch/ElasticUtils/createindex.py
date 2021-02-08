#! -*- encoding:utf-8 -*-
"""
@File    :   CreateIndex.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :  
"""


from elasticsearch import Elasticsearch

es = Elasticsearch()

def deleteInices(my_index):
    if True and es.indices.exists(my_index):  # 确认删除再改为True
        es.indices.delete(index=my_index, request_timeout=200)
        print("delete is complete")


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
    createIndex('wiki-whole-text')
    createIndex('wiki-sentence')
    # deleteInices('wiki-index')
    # createIndex('wiki-index', 'my doc2')  
    # deleteInices('my_index')
