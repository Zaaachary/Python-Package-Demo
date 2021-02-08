#! -*- encoding:utf-8 -*-
"""
@File    :   query.py
@Author  :   Zachary Li
@Contact :   li_zaaachary@163.com
@Dscpt   :   search es
"""
from elasticsearch import Elasticsearch


def login_es(host="localhost", port="9200"):
    return Elasticsearch(hosts=[{"host": host, "port": port}])


def search_sentence(es, sentence='', entity='', mode='both', dev=False, size=20):
    if mode not in ['sentence', 'entity', 'both', 'test']:
        return None

    body2 = {
        "size": size,
        "query": {
            "bool": {
                "must": {"match": {"entity": entity}},
                "should": {"bool": {"must": {"match": {"sentence": sentence}}}}
            }
        }
    }    

    match = {}
    match[mode] = sentence if mode == 'sentence' else entity

    body1 = {
        "size":size,
        "query": {
            "bool":{"should":{"match": match}}
        }
    }

    if mode != 'test':
        body = body2 if mode == 'both' else body1
    else:
        # body = body3
        pass

    res = es.search(
        index='wiki-sentence',
        body=body
    )
    if dev == True:
        print("Got %d Hits:" % res['hits']['total']['value'])
        for hit in res['hits']['hits']:
            print("%(id)s %(entity)s ||  %(sentence)s" % hit["_source"])
    return res


def search_whole_text(es, mode, target, size=20):

    if mode not in ['sentence', 'entity']:
        return None

    match = {}
    match[mode] = target

    res = es.search(
        index='wiki-whole-text',
        body={
            "size": size,
            "query": {
                "match": match
            }
        }
    )
    # print("Got %d Hits:" % res['hits']['total']['value'])
    # for hit in res['hits']['hits']:
    #     print("%(id)s %(entity)s" % hit["_source"])
    return res


if __name__ == "__main__":
    global es
    es = Elasticsearch()
    question = "people typically playing guitar"
    # qc = "punishing"
    ch = "making music"
    # case1 = "predictive models are involved with predicting a value based on other values in the dataset. the process of training a predictive model is known as supervised learning.	predict a value based on other values in the dataset. process of training a pred model is supervised learning."
    # case2 = "used to define an approximation of the actions that users will execute before involving the users themselves in real tests ex. mhp, klm, goms	use mathematical formulas to derive measures of user performance e.g. fitts' law"
    # search_sentence(es, case2, 'predictive models')
    # target = input()
    # print(search_whole_text(es, 'sentence', target, target))

    # search_sentence(es, sentence=qc+ch, entity=question, mode='both', dev=True, size=10)
    # search_sentence(es, sentence=question, entity=qc+ch, mode='both', dev=True, size=10)

    search_sentence(es, sentence=question+' '+ch, mode='sentence', dev=True, size=10)
