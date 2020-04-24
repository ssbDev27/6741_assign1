from platform import node

import rdflib
from rdflib import Namespace

g = rdflib.Graph()
foaf = Namespace("http://xmlns.com/foaf/0.1/")
focu = Namespace("http://focu.io/schema#")
focudata = Namespace("http://focu.io/data#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

g.parse("NewBase.ttl", format='n3')
print(g)

sparql1 = open("q1.txt", "r").read()
sparql2 = open("q2.txt", "r").read()
sparql3 = open("q3.txt", "r").read()
sparql4 = open("q4.txt", "r").read()
sparql5 = open("q5.txt", "r").read()
sparql6 = open("q6.txt", "r").read()
sparqla21 = open("a2q2.txt", "r").read()
sparql = [sparql6]

counter = 1
#
# for query in sparql:
#     results = g.query(query)
#     for row in results:
#         print(row[0])
#         filename = str("q" + str(counter) + "-out.ttl")
#         # with open(filename, mode='a') as file:
#         #     file.write(str(row))
#     counter += 1
#

def runQuery(action, obj):
    Res=""
    if action == "q1":
        Res = "Here we go"+"\n"
        parameter = obj[0].split()
        print(parameter)
        results = g.query("""
        SELECT ?des
 WHERE{
 ?course rdf:type focu:Course .
 ?course focu:Description ?des .
 ?course focu:Course_Subject ?sub .
 ?course focu:Course_number ?num .
 FILTER(?sub = '""" + parameter[0] + """' && ?num = '""" + parameter[1]+"'"+""")

 }
        """)
        for row in results:
            Res = Res+row[0]+"\n"
        Res =Res[:-1]+"."
    elif action =='q2':

        parameter = obj[0].split()
        print(parameter)
        Res= parameter[1]+" "+parameter[0]+" took the following subjects: "
        results = g.query("""
               SELECT ?cname
 WHERE{
 ?student rdf:type focu:Student .
 ?student foaf:familyName ?lname .
 ?student foaf:givenName ?fname .
 ?student focu:student_enrolled ?x .
 ?x foaf:name ?course .
 ?course  foaf:name ?cname .
 FILTER(?lname ='"""+parameter[1]+"""' && ?fname = '""" + parameter[0]+"'"+ """)


 }""")
        for row in results:
            Res = Res+row[0]+"\n"
        Res =Res[:-1]+"."
    elif action =="q3":
        Res="The topic is included in the follow courses: "
        print(obj)
        results = g.query("""
        
        SELECT DISTINCT ?cname

 WHERE{
 ?courses rdf:type focu:Course .
 ?courses foaf:name ?cname .
 ?courses focu:course_topics ?topic .
 ?topic foaf:name ?name .
  FILTER(?name ='"""+obj[0].strip().replace(" ","_").lower()+"'"+""" )

 }
        """)
        for row in results:
            Res = Res+row[0]+"\n"
        Res =Res[:-1]+"."
    elif action == "q4":
        Res = "Below are the students familier with the asked topic: "
        print(obj)
        results = g.query("""
                      SELECT DISTINCT ?lname ?fname
 WHERE{
 ?student rdf:type focu:Student .
 ?student foaf:familyName ?lname .
 ?student foaf:givenName ?fname .
 ?student focu:student_enrolled ?x .
 ?x foaf:name ?course .
 ?courses focu:course_topics ?topic .
 ?topic foaf:name ?name .
 FILTER(?name = '"""+obj[0].strip().replace(" ","_").lower()+"'"+""")


 }""")
        for row in results:
            Res = Res+row[0]+" "+row[1]+"\n"
        Res =Res[:-1]+"."
    elif action =="q5":

        parameter = obj[0].split()
        print(parameter[1],parameter[0])
        Res = parameter[0]+" "+parameter[1]+"knows about the following topics: "
        results = g.query("""
        Select Distinct ?tname
WHERE{
?x rdf:type focu:Student .
?x foaf:givenName ?name .
?x foaf:familyName ?lname .
?x focu:student_enrolled ?y .
?y foaf:name ?course.
?course focu:course_topics ?topic .
?topic foaf:name ?tname .
?y focu:grades_achieved ?grade .
  FILTER(?lname ='"""+parameter[1]+"""' && ?name = '""" + parameter[0]+"'"+ """ && ?grade != "F")
} """)
        flag = True
        for row in results:
            Res = Res+row[0]+","
        Res =Res[:-1]+"."
    return Res
