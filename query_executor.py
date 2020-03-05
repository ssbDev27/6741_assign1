import rdflib
from rdflib import Namespace
g = rdflib.Graph()
foaf = Namespace("http://xmlns.com/foaf/0.1/")
focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

g.parse("KG.ttl", format='n3')
print (g)
qres = g.query("""SELECT DISTINCT ?name WHERE { ?name rdf:type focu:Course .}""")

for q in qres:
    print(q)
