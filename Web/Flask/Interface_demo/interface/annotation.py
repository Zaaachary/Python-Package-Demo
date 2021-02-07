#coding=utf-8
import json, os, time
import nltk
from interface import request, app

annotation_path = 'data/annotation.json'

# 接口
@app.route('/getAnt', methods=['POST'])
def getAnt():
    """ TODO 接口逻辑 """
    params = json.loads(request.get_data(as_text=True))
    aspects = params['aspects']
    docs = params['docs']
    if (os.path.exists(annotation_path)):
        ant = json.load(open(annotation_path, encoding='utf-8'))
        for i, (doc, doc_aspects) in enumerate(zip(docs, aspects)):
            if doc['id'] in ant:
                for j, doc_aspect in enumerate(doc_aspects):
                    for ant_aspect in ant[doc['id']]:
                        if ant_aspect['sent_index'] == doc_aspect['sent_index'] and ant_aspect['aspect'] == doc_aspect['aspect']:
                            aspects[i][j]['ant_value_index'] = ant_aspect['ant_value_index']
                            if len(ant_aspect['ant_value_index']) > 0:
                                aspects[i][j]['ant'] = True
                            else:
                                aspects[i][j]['ant'] = False

    return json.dumps(aspects)
 
# 接口
@app.route('/getAllAnt', methods=['POST'])
def getAllAnt():    

    if (os.path.exists(annotation_path)):
        ant = json.load(open(annotation_path, encoding='utf-8'))
        return json.dumps(ant)
    return json.dumps({})

# 接口
@app.route('/removeAnt', methods=['POST'])
def removeAnt():    
    params = json.loads(request.get_data(as_text=True))
    aspect = params['aspect']
    doc = params['doc']
    if (os.path.exists(annotation_path)):
        ant = json.load(open(annotation_path, encoding='utf-8'))
        for i, ant_aspect in enumerate(ant[doc['id']]):
            if ant_aspect['sent_index'] == aspect['sent_index'] and ant_aspect['aspect'] == aspect['aspect']:
                ant[doc['id']].pop(i)
                break
    fileObject = open(annotation_path, 'w')
    fileObject.write(json.dumps(ant))
    fileObject.close()
    return json.dumps({'success': True})

@app.route('/saveAnt', methods=['POST'])
def saveAnt():
    """ TODO 接口逻辑 """
    params = json.loads(request.get_data(as_text=True))
    aspect = params['aspect']
    aspect['time'] = time.time()
    aspect['sent_words'] = nltk.word_tokenize(aspect['sent'])
    doc = params['doc']
    ant = {}
    if (os.path.exists(annotation_path)):
        ant = json.load(open(annotation_path, encoding='utf-8'))
    if doc['id'] in ant:
        flag = False
        for i, ant_aspect in enumerate(ant[doc['id']]):
            if ant_aspect['sent_index'] == aspect['sent_index'] and ant_aspect['aspect'] == aspect['aspect']:
                ant[doc['id']][i] = aspect
                flag = True
        if not flag:
            ant[doc['id']].append(aspect)

    else:
        ant[doc['id']] = [aspect]
    
    fileObject = open(annotation_path, 'w')
    fileObject.write(json.dumps(ant))
    fileObject.close()

    return json.dumps({'success': True})




