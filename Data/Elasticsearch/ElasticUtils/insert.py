#! -*- encoding:utf-8 -*-
"""
@File    :   insert.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   
"""
import json
import os
from tqdm import tqdm
from elasticsearch import Elasticsearch, helpers

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
        pbar.update(len(body))

    pbar.close()
    es.index(index=index_name, body=data1)  #一条插入


def insert_whole_text(file_path):
    # 调用后插入数据
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            example = json.loads(line)
            data.append({
                'id': int(example['id']),
                'sentence': ' '.join(example['text']),
                'entity': example['title']
            })

    index_name = "wiki-whole-text"
    insertData(data, index_name, one_bulk=1000)

def insert_sentence(file_path):
    # 调用后插入数据
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            example = json.loads(line)
            for sent in example['text']:
                data.append({
                    'id': int(example['id']),
                    'sentence': sent,
                    'entity': example['title']
                })

    index_name = "wiki-sentence"
    insertData(data, index_name, one_bulk=1000)

def insert_all():
    file_list = os.listdir('DATA\\WikiResult')
    for index, filename in enumerate(file_list):
        print(f'[{index}/{len(file_list)}] Now insert {filename}')
        print('')
        insert_whole_text('DATA\\WikiResult\\'+filename)
        insert_sentence('DATA\\WikiResult\\'+filename)


if __name__ == "__main__":
    insert_all()

