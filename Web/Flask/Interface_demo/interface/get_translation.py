# coding=utf-8
from interface import request, app
import json
from itertools import groupby
from stanfordcorenlp import StanfordCoreNLP
import requests
import nltk

with open("data/corpus.json", "r", encoding="utf-8") as f:
    dic = json.load(f)

with open("data/geo.json", "r", encoding="utf-8") as f:
    geobackup = json.load(f)

nlp = StanfordCoreNLP('http://localhost', port=8999)

with open("data/translation/translation_sent_detokenized.zh", "r", encoding="utf-8") as f:
    translation_sent_detokenized = json.load(f)
# 接口
@app.route('/get_translation', methods=['POST'])
def get_translation():
    """ TODO 接口逻辑 """
    params = json.loads(request.get_data(as_text=True))
    docIDs = list()
    for doc in params['docs']:
        docIDs.append(int(doc["id"]))
    
    GeoLists = list()
    for docID in docIDs:
        geolist = all_docs_geo_list[docID]
        GeoLists.append(geolist)
    return json.dumps(GeoLists)