import rdflib

g = rdflib.Graph()


g.parse("KG.ttl", format='n3')

qres = g.query("SELECT DISTINCT ?name WHERE { ?sub foaf:LastName ?name.}")

for row in qres:
    print(row)