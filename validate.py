from lxml import etree
try:
   
    xml_doc = etree.parse("graph.xml")
    xsd_doc = etree.parse("schema.xsd")
    
   
    schema = etree.XMLSchema(xsd_doc)
    if schema.validate(xml_doc):
        print("Mubarak ho! XML file XSD ke mutabiq bilkul VALID hai.")
    else:
        print("Validation Failed! XML file schema se match nahi kar rahi.")
        print(schema.error_log)

except Exception as e:
    print("Error:", e)