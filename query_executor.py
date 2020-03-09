from platform import node

import rdflib
from rdflib import Namespace
g = rdflib.Graph()
foaf = Namespace("http://xmlns.com/foaf/0.1/")
focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

g.parse("KG.ttl", format='n3')
print (g)

sparql1 = open("q1.txt", "r").read()
sparql2 = open("q2.txt","r").read()
sparql3= open("q3.txt","r").read()
sparql4 = open("q4.txt","r").read()
sparql5 =open("q5.txt","r").read()
sparql6 =open("q6.txt","r").read()


q = g.query(sparql5)
for qS in q:
    print(qS)
