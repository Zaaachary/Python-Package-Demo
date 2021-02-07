#coding=utf-8
import json
from interface import request, app


# 接口
@app.route('/getline', methods=['POST'])
def getline():
    # 时间地点都是全的
    params = json.loads(request.get_data(as_text=True))
    text = params['text'] # 检索内容 text = "xxx航母"
    docs = params['docs'] # 文章ID docs = [id, id, id...]
    result = {}
    """ TODO 接口逻辑 """
    for doc_id in docs:
        with open('data/event_lemm.json', 'r') as fin:
            table = json.load(fin)
        if doc_id['id'] in table.keys():
            result[doc_id['id']] = table[doc_id['id']]
    """ END """
    return json.dumps(result)

# 接口
@app.route('/getline_dep', methods=['POST'])
def getline_dep():
    # 没时间的也保留
    params = json.loads(request.get_data(as_text=True))
    text = params['text'] # 检索内容 text = "xxx航母"
    docs = params['docs'] # 文章ID docs = [id, id, id...]
    result = {}
    """ TODO 接口逻辑 """
    for doc_id in docs:
        with open('data/event_dep.json', 'r') as fin:
            table = json.load(fin)
        if doc_id['id'] in table.keys():
            result[doc_id['id']] = table[doc_id['id']]
    """ END """
    return json.dumps(result)


# 接口
@app.route('/getline_all', methods=['POST'])
def getline_all():
    # 内容不做时间地点过滤
    params = json.loads(request.get_data(as_text=True))
    text = params['text'] # 检索内容 text = "xxx航母"
    docs = params['docs'] # 文章ID docs = [id, id, id...]
    result = {}
    """ TODO 接口逻辑 """
    for doc_id in docs:
        with open('data/event_all.json', 'r') as fin:
            table = json.load(fin)
        if doc_id['id'] in table.keys():
            result[doc_id['id']] = table[doc_id['id']]
    """ END """
    return json.dumps(result)

# result{
#     doc_id:[
#           {
#           'SENTENCE':
#           'DATE': [num, month, day]
#           'LOCATION':
#           'TRIGGER':[str,str]
#           }，
#            ...
#       ]
# ...
# }

