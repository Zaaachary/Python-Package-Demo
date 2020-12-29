#! -*- encoding:utf-8 -*-
"""
@File    :   mainInsert.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   
"""
# %%
from elasticsearch import Elasticsearch, helpers
from tqdm import tqdm

es = Elasticsearch()

def insertData(words, index_name, one_bulk):
    # 插入数据
    # one_bulk表示一个bulk里装多少个
    body = []
    body_count = 0  # 记录body里面有多少个.
    # 最后一个bulk可能没满one_bulk,但也要插入

    print("need to insert %d" % len(words))
    pbar = tqdm(total=len(words))

    for word in words:
        # data1 = {"id": word['id'],  # id
        #          "sentence": word['words'],
        #          "entity":word['']}  # text
        data1 = word
        every_body = \
            {
                "_index": index_name,  # 索引文件名
                # "_type": my_doc,   # 数据文件名
                "_source": data1  # 文档正文
            }

        if body_count < one_bulk:
            body.append(every_body)
            body_count += 1
        else:
            helpers.bulk(es, body)  # 还是要用bulk啊，不然太慢了
            pbar.update(one_bulk)
            body_count = 0
            body = []
            body.append(every_body)
            body_count += 1

    if len(body) > 0:
        # 如果body里面还有，则再插入一次（最后非整块的）
        helpers.bulk(es, body)
        # pbar.update(len(body))
        print('done2')

    pbar.close()
    res = es.index(index=index_name, body=data1)  #一条插入
    # res = es.index(index=index_name,doc_type=my_doc,id=my_key_id,body=data1)  #一条插入
    print("insert data completed!")


def mainInsert():
    # 调用后插入数据
    index_name = "wiki-index"
    # words = getAllWords(path="/Wiki_processing/wikiextractor/extracted/AA/wikipedia_sentences.txt")
    words = [{'id':3, 'sentence':'have a look.', 'entity':'look'}]
    # words = [{'id':1, 'sentence':'just have a test.', 'entity':'test'}]
    insertData(words, index_name, one_bulk=5000)

if __name__ == "__main__":
     mainInsert()
