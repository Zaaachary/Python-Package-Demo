#! -*- encoding:utf-8 -*-
"""
@File    :   Example Usage.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   https://elasticsearch-py.readthedocs.io/en/7.10.0/
"""
# %%
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}

res = es.index(index="test-index", id=1, body=doc)
print(res['result'])
# %%
res = es.get(index="test-index", id=1)
print(res)
print(res['_source'])

# %%
es.indices.refresh(index="test-index")

# %%
res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
# %%
