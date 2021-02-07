# coding=utf-8
from interface import request, app
import json
from itertools import groupby
# from stanfordcorenlp import StanfordCoreNLP
import requests
# import nltk

with open("data/corpus.json", "r", encoding="utf-8") as f:
    dic = json.load(f)

with open("data/geo.json", "r", encoding="utf-8") as f:
    geobackup = json.load(f)

# nlp = StanfordCoreNLP('http://localhost', port=8999)

with open("data/all_docs_geo_list.json", "r", encoding="utf-8") as f:
    all_docs_geo_list = json.load(f)
# 接口
@app.route('/getloc', methods=['POST'])
def getloc():
    """
    return GeoLists
    # geolist:
    # {
    #     location_1:[
    #           'LONGTITUDE':
    #           'LATITUDE':
    #           'LOCATION_CHINESE_NAME':
    #           'IN WHICH SENTENCE':
    #     ]
    #     location_2:[
    #           'LONGTITUDE':
    #           'LATITUDE':
    #           'LOCATION_CHINESE_NAME':
    #           'IN WHICH SENTENCE':
    #     ]
    #     ...
    # }

    # GeoLists:
    # [
    #   geolist_1,
    #   geolist_2,
    #   ...
    # ]
    """
    params = json.loads(request.get_data(as_text=True))
    docIDs = list()
    for doc in params['docs']:
        docIDs.append(int(doc["id"]))
    
    GeoLists = list()
    for docID in docIDs:
        # geolist = getCoordinate(getLocation(docID))
        geolist = all_docs_geo_list[str(docID)]
        GeoLists.append(geolist)
    return json.dumps(GeoLists)




# def getLocation(docID):
#     loc_tag = ["CITY", "STATE_OR_PROVINCE", "COUNTRY", "LOCATION"]
#     for item in dic:
#         if item["id"] == docID:
#             doc_content = item["content"]
#             sen_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
#             sentences = sen_tokenizer.tokenize(doc_content)
#             location_list = list()
#             sent_count = -1
#             for sent_content in sentences:
#                 sent_count += 1
#                 netagged_words = nlp.ner(sent_content)
#                 for tag, chunk in groupby(netagged_words, lambda x: x[1]):
#                     if tag in loc_tag:
#                         location = " ".join(w for w, t in chunk)
#                         item_location = dict()
#                         item_location["name"] = location
#                         item_location["type"] = tag
#                         item_location["sent"] = sent_content
#                         item_location["sent_id"] = sent_count
#                         location_list.append(item_location)
#                     elif tag == "ORGANIZATION":
#                         location = " ".join(w for w, t in chunk)
#                         if "base" in location.lower():
#                             item_location = dict()
#                             item_location["name"] = location
#                             item_location["type"] = tag
#                             item_location["sent"] = sent_content
#                             item_location["sent_id"] = sent_count
#                             location_list.append(item_location)
#             # location_list:
#             # <class 'list'>: [{'name': 'OKINAWA', 'type': 'LOCATION'}, {'name': 'Japan', 'type': 'LOCATION'},
#             #                 {'name': 'Marine Corps Air Station Futenma', 'type': 'ORGANIZATION'},
#             #                 {'name': 'U.S.', 'type': 'LOCATION'}, {'name': 'U.S. Marine Corps', 'type': 'ORGANIZATION'},
#             #                 {'name': 'Marine Aircraft Group', 'type': 'ORGANIZATION'},
#             #                 {'name': 'Marine Medium Tiltrotor Squadron', 'type': 'ORGANIZATION'},
#             #                 {'name': 'Marine Medium Tiltrotor Squadron', 'type': 'ORGANIZATION'},
#             #                 {'name': 'Marine Heavy Helicopter Squadron', 'type': 'ORGANIZATION'},
#             #                 {'name': 'Marine Wing Support Squadron', 'type': 'ORGANIZATION'},
#             #                 {'name': 'Marine Air Control Group', 'type': 'ORGANIZATION'},
#             #                 {'name': 'MWSS', 'type': 'ORGANIZATION'},
#             #                 {'name': 'U.S. Marine Corps', 'type': 'ORGANIZATION'},
#             #                 {'name': 'Marine Wing Support Squadron', 'type': 'ORGANIZATION'},
#             #                 {'name': 'MWSS', 'type': 'ORGANIZATION'},
#             #                 {'name': 'U.S. Marine Corps', 'type': 'ORGANIZATION'},
#             #                 {'name': 'Marine Medium Tiltrotor Squadron', 'type': 'ORGANIZATION'},
#             #                 {'name': 'MEF', 'type': 'ORGANIZATION'}, {'name': 'Marine Corps', 'type': 'ORGANIZATION'}]
#             remove_id_set = set()
#             for i in range(len(location_list)):
#                 name = location_list[i]["name"]
#                 for j in range(i + 1, len(location_list)):
#                     name2 = location_list[j]["name"]
#                     if name in name2 and len(name) <= len(name2) and i not in remove_id_set:
#                         remove_id_set.add(i)

#             new_location_list = list()
#             for i in range(len(location_list)):
#                 if i not in remove_id_set:
#                     new_location_list.append(location_list[i])

#             # new_location_list = sorted(set(new_location_list), key=new_location_list.index)
#             print("end")
#             # <class 'list'>: [{'name': 'OKINAWA', 'type': 'LOCATION'}, {'name': 'Japan', 'type': 'LOCATION'}, {'name': 'U.S.', 'type': 'LOCATION'}]
#             return new_location_list


# def getCoordinate(locationList):
#     geolist = dict()
#     for item_location in locationList:
#         loc = item_location["name"]
#         if loc in geobackup:
#             geo = geobackup[loc]
#         else:
#             success = False
#             while success is not True:
#                 try:
#                     resp = json.loads(requests.get(
#                         "https://us1.locationiq.com/v1/search.php?key=c94d0828135b8e&format=json&accept-language=zh&limit=1&q=" + loc,
#                         timeout=2).text)
#                     if "error" in resp:
#                         break
#                     resp = resp[0]
#                     success = True
#                 except:
#                     pass

#             try:
#                 geo = (resp["lat"], resp["lon"], resp["display_name"])
#             except:
#                 geo = list()
#             geobackup[loc] = geo
#             with open("data/geo.json", "w", encoding="utf-8") as f:
#                 json.dump(geobackup, f, indent=4, ensure_ascii=False)
#         try:
#             geolist[loc] = (geo[0], geo[1], geo[2], item_location["sent"], item_location["sent_id"])
#         except:
#             continue

#     # <class 'dict'>: {
#     #                  'OKINAWA': ('26.5707754', '128.0255901', '冲绳县, 日本', 'sent_content', 0), 
#     #                  'Japan': ('36.5748441', '139.2394179', '日本', 'sent_content', 1), 
#     #                  'U.S.': ('45.1895845', '-88.73215845', 'U.S., 'sent_content', 2)
#     #                 }
#     return geolist

if __name__ == "__main__":
    # loclist = getLocation(1)
    # getCoordinate(loclist)
    ss = getloc(1)
    print("end")