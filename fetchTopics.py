import csv
import pandas as pd
import numpy as np
#import pydbpedia as dbpedia
from rdflib import Graph, URIRef, Namespace, Literal, BNode

foaf = Namespace("http://xmlns.com/foaf/0.1/")
focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
g =Graph()



g.parse('NewBase.ttl',format='n3')
listOfTopics =['UndergradTopics.csv','Grad_topics.csv']
for file in listOfTopics:
    path = file.replace("'",'')
    data = pd.read_csv(path,delimiter=',')
    data = np.array(data)
    for i in range(5):
        course_name = URIRef("http://focu.io/data#"+str(data[i][0]).replace(" ","%"))
        g.add((course_name, rdf.type, focu.Course))
        for r in range(len(data)):
            if data[i][0]==data[r][0]:
                topic_generated = URIRef("http://focu.io/data#" + str(data[r][1]).replace(" ", "_"))
                print(topic_generated)
                topic_generated_link = data[r][2]
                topic = URIRef(topic_generated_link)
                g.add((topic_generated, rdf.type, foaf.topic))
                g.add((topic_generated,foaf.name,Literal(str(data[r][1]).replace(" ", "_"))))
                g.add((topic_generated, rdf.seeAlso, topic))
                g.add((course_name, focu.course_topics, topic_generated))
        i = r;
g.serialize('NewBase.ttl',format='turtle')