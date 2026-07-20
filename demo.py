import ottr

# an OttrGenerator is used to load templates and expand instances -
# load a simple OTTR template definition

template: str = """
@prefix ex: <http://example.org#> .

ex:FirstName [ ottr:IRI ?uri, ?firstName ] :: {
  ottr:Triple ( ?uri, foaf:firstName, ?firstName )
} .

ex:Person[ ?firstName ] :: {
  ottr:Triple ( _:person, rdf:type, foaf:Person ),
  ex:FirstName ( _:person, ?firstName )
} .
""".strip()

generator: ottr.OttrGenerator = ottr.OttrGenerator()
generator.load_templates(template)

# parse and prepare an instance for execution

rdf_data: str = """
@prefix ex: <http://example.org#> .

ex:Person("Ann") .
""".strip()

instances: ottr.generator.OttrInstances = generator.instanciate(rdf_data)

# execute the instance, which yield RDF triples
# the following prints (_:person0, rdf:type, foaf:Person) and (_:person0, foaf:firstName, "Ann")

for s, p, o in instances.execute(as_nt = True):
    print("# ----- RDF triple ----- #")
    print(s, p, o)
