import warnings

import requests
from bs4 import BeautifulSoup
import csv

from rdflib import Graph, URIRef, Namespace, Literal, BNode

foaf = Namespace("http://xmlns.com/foaf/0.1/")
focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
g =Graph()

g.parse('KG.ttl',format='n3')
with open('TopicsExtracted2.csv',"r") as topic_file:
    TopicsExtracted = csv.reader(topic_file, delimiter=',')
    counter = 0
    prev_course=str(next(TopicsExtracted)[0])
    # first_course = URIRef("http://focu.io/data#" + prev_course.replace(" ", "_"))
    # g.add((first_course, rdf.type, focu.course_name))

    for topic in TopicsExtracted:
        next_course=str(topic[0])
        course_name = URIRef("http://focu.io/data#" + str(topic[0]).replace(" ", "_"))
        topic_generated = URIRef("http://focu.io/data#" + str(topic[1]).replace(" ", "_"))
        topic_generated_link = URIRef(topic[2])

        g.add((topic_generated, rdf.type, focu.Topic))
        g.add((topic_generated, focu.generated_topic_link, topic_generated_link))
        g.add((topic_generated, rdfs.seeAlso, course_name))

        # if (prev_course==next_course):
        #     g.add((course_name, focu.generated_topic, topic_generated))
        #     g.add((topic_generated, focu.generated_topic_link, Literal(topic_generated_link)))
        # else:
        #
        # prev_course = str(topic[0])

g.serialize('topic.ttl',format='turtle')
for items in g:
    print(items)