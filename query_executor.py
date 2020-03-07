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

sparql1 = """SELECT ?description WHERE {
?name focu:student_enrolled ?x .
?x  focu:course_name_is ?course .
?course focu:course_description ?description
}"""

# Infer the terms of subject in which NLP was offered
sparql2 ="""
Select ?terms WHERE{

}
"""
q = g.query(sparql1)
for qS in q:
    print(qS)
