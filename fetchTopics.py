import csv
import pandas as pd
import numpy as np
from rdflib import Graph, URIRef, Namespace, Literal, BNode

foaf = Namespace("http://xmlns.com/foaf/0.1/")
focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
g =Graph()

data = pd.read_csv('TopicsExtracted2.csv',delimiter=',')
data = np.array(data)
g.parse('KG.ttl',format='n3')
for i in range(len(data)):

    course_name = URIRef("http://focu.io/data#"+str(data[i][0]).replace(" ","%"))
    g.add((course_name, rdf.type, focu.course_name))
    for r in range(len(data)):
        if data[i][0]==data[r][0]:
            topic_generated = URIRef("http://focu.io/data#" + str(data[r][1]).replace(" ", "_"))
            print(topic_generated)
            topic_generated_link = data[r][2]
            topic = URIRef(topic_generated_link)
            g.add((topic_generated, rdf.type, focu.Topic))
            g.add((topic_generated, rdf.seeAlso, topic))
            g.add((course_name, focu.course_topics, topic_generated))
    i = r;
g.serialize('KG.ttl',format='turtle')
