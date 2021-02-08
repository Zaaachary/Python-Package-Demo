from elasticsearch import Elasticsearch
import sys, os, json
import nltk

es = Elasticsearch('127.0.0.1:9200')

def searchES(index, value):
    dsl = {
        'query': {
            'match': {
                'content': value
            }
        }
    }
    return es.search(index=index, body=dsl, size=100)


def testSearch():
    corpus = json.load(open('corpus.json', encoding='utf-8'))
    first_correct = 0
    correct = 0
    for item in corpus:
        result = searchES('origin', item['title'])
        if item['id'] == int(result['hits']['hits'][0]['_id']):
            first_correct +=1
        for hit in result['hits']['hits']:
            if int(hit['_id']) == item['id']:
                correct += 1
    
    print('All Samples = %d, first correct = %d, ratio = %.4f' % (len(corpus), first_correct, first_correct / len(corpus)))
    print('All Samples = %d, correct = %d, ratio = %.4f' % (len(corpus), correct, correct / len(corpus)))


if __name__ == "__main__":

    testSearch()
