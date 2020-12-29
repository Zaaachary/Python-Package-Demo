#! -*- encoding:utf-8 -*-
"""
@File    :   query.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   search es
"""

from elasticsearch import Elasticsearch

def login_es(host ="localhost",port = "9200"):
    return Elasticsearch(hosts=[{"host": host, "port": port}])

def search(query):
    global es
    result = es.search(
        index = 'wiki-index',
        body = {
            "query": {
                "match": {
                    # "id": query
                    'sentence':query
                }
            }
        }
    )
    return result


if __name__ == "__main__":
    global es
    es = Elasticsearch()

    print(search('have a'))
