#coding=utf-8
import json
from ES.search import searchES
from interface import request, app
import nltk

"""
['aspect1', 'aspect2'...]

[
    {
        id: 5,
        sents: [1, 3]
    },
    ...
]
"""

# 接口
@app.route('/search', methods=['POST'])
def search():
    """ TODO 接口逻辑 """
    params = json.loads(request.get_data(as_text=True))
    result = searchES(params['index'], params['text'])
    for doc in result['hits']['hits']:
        doc['_source']['sents'] = [nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(doc['_source']['content'])]
    return json.dumps(result)




