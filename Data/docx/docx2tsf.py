# -*- encoding: utf-8 -*-
'''
@File    :   docx2tsf.py
@Time    :   2022/01/23 11:17:15
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   convert doc to tsf
'''
from operator import imod
from docx import Document as D


def get_qa(line):
    # import pdb; pdb.set_trace()
    if line and "->" in line:
        split_line = line.split('->')
        split_line = [part.strip() for part in split_line if part.strip()]
        if len(split_line) != 2:
            return None
        else:
            return split_line
    
def question_format(question):
    question = question.strip().replace(' ', '')
    question = question.replace("（多选）", '')
    return question

def answer_format(answer):
    # answer = answer.strip().replace('，', '')
    if answer[-1] == ",":
        answer = answer[:-1]
    # answer = answer.replace(',', '')
    return answer

def main(target_path, output_path):
    doc = D(target_path)

    data_list = []
    for line in doc.paragraphs:
        try:
            text = line.text
            question, answer = get_qa(text)
            question = question_format(question)
            answer = answer_format(answer)
            data_list.append((question, answer))
        except (TypeError, ValueError):
            continue
            
    print(f"length : {len(data_list)}")
    f = open(output, 'w', encoding='utf-8')
    for line in data_list:
        line = '\t'.join(line) + '\n'
        f.write(line)
    f.close()




if __name__ == "__main__":
    target = "./demo.docx"
    output = "./formated_doc.tsf"
    main(target, output)