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

sparql2 = """

SELECT (COUNT(*) as ?Triples) 
WHERE 
      { ?s ?p ?o } 
"""
sparql3= """
Select ?topic ?link
Where{ focudata:Applied_Artificial_Intelligence_ focu:course_topics ?topic .
?topic rdf:seeAlso ?link .
}"""
# Infer the terms of subject in which NLP was offered
sparql4 ="""Select ?course ?grade WHERE{
<http://focu.io/data#Pulkit%Ghai> focu:student_enrolled ?x .
?x focu:course_name_is ?course .
?x focu:grades_achieved ?grade .
}
"""

sparql5 ="""Select Distinct ?students   WHERE{
?students focu:student_enrolled ?x .
?x focu:course_name_is ?course.
?course focu:course_topics focudata:distributed_systems .
?x focu:grades_achieved ?grade .
 FILTER(?grade != "F") .
}
"""

sparql6 ="""Select Distinct ?topic  WHERE{
<http://focu.io/data#Pulkit%Ghai> focu:student_enrolled ?x .
?x focu:course_name_is ?course.
?course focu:course_topics ?topic .
?x focu:grades_achieved ?grade .
 FILTER(?grade != "F") .
}
"""


q = g.query(sparql2)
for qS in q:
    print(qS)
