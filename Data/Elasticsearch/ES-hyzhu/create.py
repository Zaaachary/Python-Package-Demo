from elasticsearch import Elasticsearch
import sys, os, json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--recreate', action='store_true')
parser.add_argument('--index', default='origin')
args = parser.parse_args()

if __name__ == "__main__":

    es = Elasticsearch('127.0.0.1:9200')
    
    if args.recreate: 
        # 创建新索引
        if es.indices.exists(index=args.index):
            es.indices.delete(index=args.index)
            
        res = es.index(index=args.index, body = {
            'mappings': {
                '_source': {
                    'enabled': True
                },
                'properties': {
                    'title': {'type': 'text'},
                    'content': {'type': 'text'},
                    'img_content': {'type': 'keyword'},
                    'id': {'type': 'long'}
                }
            }
        })

    # 插入数据
    corpus = json.load(open('corpus.json', encoding='utf-8'))
    for item in corpus:
        es.create(index=args.index, id=item['id'], body=item)

