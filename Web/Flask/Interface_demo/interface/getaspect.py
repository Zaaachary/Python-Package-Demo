#coding=utf-8
from interface import request, app
import json
import nltk
import os
# import tensorflow as tf
# from stanfordcorenlp import StanfordCoreNLP
# from aspect_extraction.infer import create_sess_and_model as create_aspect_sess_model, infer_aspect, infer_aspect_by_batch
# from value_extraction.infer import create_sess_and_model as create_value_sess_model, infer_value

# g_as = tf.Graph()
# g_v = tf.Graph()

# sess_as, model_as = create_aspect_sess_model(g_as)
# sess_v, model_v = create_value_sess_model(g_v)

with open("data/corpus.json", "r", encoding="utf-8") as f:
    corpus = json.load(f)
with open("data/aspect_results_by_doc.json", "r", encoding="utf-8") as f:
    aspect_results_by_doc = json.load(f)
with open("data/corpus_value_results.json", "r", encoding="utf-8") as f:
    value_results = json.load(f)

# nlp = StanfordCoreNLP('http://localhost', port=8999)

# 接口
@app.route('/getaspect', methods=['POST'])
def aspect_extraction():
    """ TODO 接口逻辑 """
    params = json.loads(request.get_data(as_text=True))
    result = []
    doc_ids = []
    for doc in params['docs']:
        doc_ids.append(doc['id'])
        
    for doc_id in doc_ids:
        for item in corpus:
            if item['id'] == int(doc_id):
                content = item['content']
                result.append(get_aspects_from_doc(content, doc_id))

    '''
    [ result
        [ 文档1
            [ 属性1
                {
                    'text' : 原句
                    'aspect' : 属性
                    'value' : [值1, 值2,...]
                    'text_index' : 句子序号 # 句子在文档中的位置
                    'aspect_index' : [属性序号] # 在tokens中的位置,例 [2,3]
                    'value_index' : [[值1序号], [值2序号], ...] # 在tokens中的位置,例 [[4], [6,7], [10]]
                }
            ]
            [ 属性2
                ...
            ]
            ...
        ]
        [ 文档2
            ...
        ]
        ...
    ]

    '''

    # result = searchES(params['index'], params['text'])
    return json.dumps(result)

def get_aspects_from_doc1(doc, doc_id):
    aspects = []
    sentences = nltk.sent_tokenize(doc)
    lines = sentences.copy()
    for i in range(len(lines)):
        ner_result = nlp.ner(lines[i])
        for token, tag in ner_result:
            if tag == 'DATE' or tag == 'TIME':
                if token.isdigit():
                    new_token = '^'.join(token)
                    lines[i] = lines[i].replace(token, new_token)

    if str(doc_id) in aspect_results_by_doc.keys():
        results = aspect_results_by_doc[str(doc_id)]
    else:
        results = infer_aspect_by_batch(sess_as, model_as, lines)
        aspect_results_by_doc[str(doc_id)] = results
        with open("data/aspect_results_by_doc.json", "w", encoding="utf-8") as f:
            json.dump(aspect_results_by_doc, f)

    for result, line in zip(results, lines):
        values = get_value_by_aspect(result, line)
        for value in values:
            value['text_index'] = sentences.index(value['text'])
        aspects += values

    return aspects

def get_aspects_from_doc(doc, doc_id):
    aspects = []

    if str(doc_id) in aspect_results_by_doc.keys():
        results = aspect_results_by_doc[str(doc_id)]
        sentences = nltk.sent_tokenize(doc)
        for sent_id, (result, sentence) in enumerate(zip(results, sentences)):
            # ner_result = nlp.ner(sentence)
            line = sentence
            # for token, tag in ner_result:
            #     if tag == 'DATE' or tag == 'TIME':
            #         if token.isdigit():
            #             new_token = '^'.join(token)
            #             line = line.replace(token, new_token)
            if len(line.split()) == 0:
                continue

            # values = get_value_by_aspect(result, line)
            values = get_value_from_file(result, line, doc_id, str(sent_id))
            for value in values:
                value['text_index'] = sentences.index(sentence)
            aspects += values

    else:
        sentences = nltk.sent_tokenize(doc)
        results = []
        for sentence in sentences:
            ner_result = nlp.ner(sentence)
            line = sentence
            for token, tag in ner_result:
                if tag == 'DATE' or tag == 'TIME':
                    if token.isdigit():
                        new_token = '^'.join(token)
                        line = line.replace(token, new_token)
            if len(line.split()) == 0:
                continue
            
            # 抽取句子line中的aspect
            result = infer_aspect(sess_as, model_as, line)
            # result = model.evaluate_line(sess, input_from_line(line, char_to_id, character_to_id, tag_to_id, FLAGS.lower), id_to_tag)
            # aspect_list = [aspect['word'] for aspect in result['entities']]
            # aspect_dict = {}
            # aspect_dict['text'] = line
            # aspect_dict['aspects'] = aspect_list 
            # aspects.append(aspect_dict)

            results.append({"string":result["string"], "entities":result["entities"]})
            aspect_results_by_doc[str(doc_id)] = results
            with open("data/aspect_results_by_doc.json", "w", encoding="utf-8") as f:
                json.dump(aspect_results_by_doc, f)
            
            values = get_value_by_aspect(result, line)
            for value in values:
                value['text_index'] = sentences.index(value['text'])
            aspects += values

    return aspects

def get_value_by_aspect(aspect_result, text):
    values = []
    for aspect in aspect_result['entities']:
        aspect_tags = [0]*len(aspect_result['string'])
        for i in range(aspect['start'],aspect['end']):
            aspect_tags[i] = 2
        aspect_tags[aspect['start']] = 1
        #get values
        line = {}
        line['text'] = text
        line['aspect'] = aspect['word']
        # if len(aspect_result['string']) >= model_as.max_len:
        if 0 not in aspect_result['string']:
            sent_length = 300
        else:
            sent_length = aspect_result['string'].index(0)
        line['tokenize'] = aspect_result['string'][:sent_length]
        line['aspect_tags'] = aspect_tags[:sent_length]
        result = infer_value(sess_v, model_v, line)
        # result = model.evaluate_line(sess, input_from_line(line, char_to_id, character_to_id, tag_to_id, FLAGS.lower), id_to_tag)
        # build return value
        value_list = [value['word'] for value in result['entities']]
        value_indexs = []
        for value in result['entities']:
            value_index = [index for index in range(value['start'],value['end'])]
            value_indexs.append(value_index)
        # if len(value_list) > 0:
        value_dict = {}
        value_dict['text'] = text
        value_dict['aspect'] = aspect['word']
        value_dict['aspect_index'] = [index for index in range(aspect['start'],aspect['end'])]
        value_dict['value'] = value_list
        value_dict['value_index'] = value_indexs
        # restore the text and tokes
        for token in line['tokenize']:
            # print(token)
            if '^' in token:
                # if token.replace('^', '').isdigit():
                    new_token = token.replace('^', '')
                    value_dict['text'] = value_dict['text'].replace(token, new_token)
                    value_dict['aspect'] = value_dict['aspect'].replace(token, new_token)
                    for value in value_dict['value']:
                        value = value.replace(token, new_token)
        values.append(value_dict)

    return values

def get_value_from_file(aspect_result, text, doc_id, sent_id):
    values = []
    results = value_results[doc_id][sent_id]
    for aspect, result in zip(aspect_result['entities'], results):
        aspect_tags = [0]*len(aspect_result['string'])
        for i in range(aspect['start'],aspect['end']):
            aspect_tags[i] = 2
        aspect_tags[aspect['start']] = 1
        #get values
        line = {}
        line['text'] = text
        line['aspect'] = aspect['word']
        # if len(aspect_result['string']) >= model_as.max_len:
        if 0 not in aspect_result['string']:
            sent_length = 300
        else:
            sent_length = aspect_result['string'].index(0)
        line['tokenize'] = aspect_result['string'][:sent_length]
        line['aspect_tags'] = aspect_tags[:sent_length]
        # result = infer_value(sess_v, model_v, line)
        # result = model.evaluate_line(sess, input_from_line(line, char_to_id, character_to_id, tag_to_id, FLAGS.lower), id_to_tag)
        # build return value
        value_list = [value['word'] for value in result['entities']]
        value_indexs = []
        for value in result['entities']:
            value_index = [index for index in range(value['start'],value['end'])]
            value_indexs.append(value_index)
        # if len(value_list) > 0:
        value_dict = {}
        value_dict['text'] = text
        value_dict['aspect'] = aspect['word']
        value_dict['aspect_index'] = [index for index in range(aspect['start'],aspect['end'])]
        value_dict['value'] = value_list
        value_dict['value_index'] = value_indexs
        # restore the text and tokes
        for token in line['tokenize']:
            # print(token)
            if '^' in token:
                # if token.replace('^', '').isdigit():
                    new_token = token.replace('^', '')
                    value_dict['text'] = value_dict['text'].replace(token, new_token)
                    value_dict['aspect'] = value_dict['aspect'].replace(token, new_token)
                    for value in value_dict['value']:
                        value = value.replace(token, new_token)
        values.append(value_dict)

    return values
