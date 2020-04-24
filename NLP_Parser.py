#!/usr/bin/python
# -*- coding: utf-8 -*-
import spacy
import copy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')

questions = ['What is COMP 474 about?',
             'Which courses did Pulkit Ghai take?',
             'Who is familiar with Distributed Computing?',
             'Which courses cover System Analysis?',
             'What does Pulkit Ghai know?', 'tell me about COMP 474?']

pattern = []


def detectQuestionType(doc, ques):
    obj = []
    # print (doc)
    flag = False
    qus = ques
    for token in doc:
        if token.pos_ == 'AUX':
            qus = qus.replace(str(' ' + token.text + ' '), ' ')
        elif token.pos_ == 'PRON':
            qus = qus.replace(str('' + token.text + ' '), ' ')
        elif token.pos_ == 'DET':
            qus = qus.replace(str('' + token.text + ' '), ' ')
        if token.pos_ == 'PROPN':

            # check if it is course name or number
            try:
                if token.nbor().pos_ == 'NUM':
                    obj.append(token.text + ' ' + token.nbor().text)
                    qus = qus.replace(str(' ' + token.text + ' '
                                          + token.nbor().text + ''), ' ')
                elif token.nbor().pos_ == 'PROPN':
                    obj.append(token.text + ' ' + token.nbor().text)
                    qus = qus.replace(str(' ' + token.text + ' '
                                          + token.nbor().text), ' ')
            except:
                continue
        elif token.pos_ == 'ADP' and token.text == 'with' and flag == False:
            flag = True
            o = qus[qus.index('with') + 4:]
            obj.append(o)
            qus = qus.replace(o, '')
        elif token.pos_ == 'NOUN' and flag == False:
            print()
            obj.append(token.text)
            qus = qus.replace(str(' ' + token.text + ''), ' ')
        doc = nlp(qus)

    # print ("Action", qus)
    print ('object is', obj)
    return rules(obj, qus, ques)


def rules(obj, qus, question):
    matcher = Matcher(nlp.vocab)
    matcher.add("rule description", None, [{"Lemma": "about"}], [{"Lemma": "detail"}])
    matcher.add("rule student_course", None, [{"Lemma": "take"}])
    matcher.add("rule topic_course", None, [{"Lemma": "cover"}])
    matcher.add("rule topic_student", None, [{"Lemma": "familiar"}, {"Lemma": "with"}])
    matcher.add("rule student_topic", None, [{"Lemma": "know"}])
    doc = nlp(qus)

    # doc=nlp(question)
    matcher_ques = Matcher(nlp.vocab)
    matcher_ques.add("question rule1", None, [{"POS": "PROPN"}, {"POS": "NUM"}])
    matcher_ques.add("question rule2", None, [{"POS": "PROPN"}, {"POS": "PROPN"},{"POS": "PROPN"}],[{"POS": "PROPN"}, {"POS": "PROPN"}])
    matcher_ques.add("question rule3", None, [{"Lemma": "course"}, {"Lemma": "cover"}])

    doc2 = nlp(question)

    for match_id, start, end in matcher(doc):
        string_id = nlp.vocab.strings[match_id]  # Get string representation
        span = doc[start:end]  # The matched span
        if (string_id == "rule topic_student"):
            return ["q4", obj[0]]

        for match_id2, start2, end2 in matcher_ques(doc2):
            span2 = doc2[start2:end2]
            string_id2 = doc.vocab.strings[match_id2]
            if (string_id == "rule description" and string_id2 == "question rule1"):
                return ["q1", span2.text]
            elif (string_id == "rule student_course" and string_id2 == "question rule2"):
                return ["q2", span2.text]
            elif (string_id == "rule topic_course" and string_id2 == "question rule3"):
                return ["q3", question.split("cover",1)[1]]
            elif (string_id == "rule student_topic" and string_id2 == "question rule2"):
                return ["q5", span2.text]


def parse_question(qus):
    if qus[-1] == '?' or qus[-1] == '.' or qus[-1] == ',':
        doc = nlp(qus[:-1])
        return detectQuestionType(doc, qus[:-1])
    else:
        doc = nlp(qus)
        return detectQuestionType(doc, qus)
