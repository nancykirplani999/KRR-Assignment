from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS
graph = Graph()
EX = Namespace("http://example.org/kg/")
graph.bind("ex", EX)
graph.bind("rdf", RDF)
graph.bind("rdfs", RDFS)

# Create resources/entities
Ali = EX.Ali
Ahmed = EX.Ahmed
DHA_Suffa_University = EX.DHA_Suffa_University
Computer_Science = EX.Computer_Science
TechSoft = EX.TechSoft

# Create classes
Person = EX.Person
Student = EX.Student
Employee = EX.Employee
University = EX.University
Program = EX.Program
Company = EX.Company

# Create predicates/relationships
studentOf = EX.studentOf
studies = EX.studies
knows = EX.knows
worksAt = EX.worksAt

# Add class/type triples
graph.add((Ali, RDF.type, Person))
graph.add((Ali, RDF.type, Student))

graph.add((Ahmed, RDF.type, Person))
graph.add((Ahmed, RDF.type, Employee))

graph.add((DHA_Suffa_University, RDF.type, University))
graph.add((Computer_Science, RDF.type, Program))
graph.add((TechSoft, RDF.type, Company))

# Add relationship triples
graph.add((Ali, studentOf, DHA_Suffa_University))
graph.add((Ali, studies, Computer_Science))
graph.add((Ali, knows, Ahmed))
graph.add((Ahmed, worksAt, TechSoft))

# Add readable labels
graph.add((Ali, RDFS.label, Literal("Ali")))
graph.add((Ahmed, RDFS.label, Literal("Ahmed")))
graph.add((DHA_Suffa_University, RDFS.label, Literal("DHA Suffa University")))
graph.add((Computer_Science, RDFS.label, Literal("Computer Science")))
graph.add((TechSoft, RDFS.label, Literal("TechSoft")))

# Print total triples
print("RDF Knowledge Graph constructed successfully!")
print("Total triples in graph:", len(graph))

print("\nRDF Graph Triples:")
print("-" * 70)

for subject, predicate, obj in graph:
    print(subject, predicate, obj)