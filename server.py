from flask import Flask, jsonify
from flask_cors import CORS
from neo4j import GraphDatabase
app = Flask(__name__)
CORS(app)
URI = "bolt://3.82.244.124:7687" 
USER = "neo4j"
PASSWORD = "headset-manifests-spiral" 
""
def setup_database():
    query = """
    MERGE (ali:Person {name: 'Ali'})
    MERGE (ahmed:Person {name: 'Ahmed'})
    MERGE (dsu:University {name: 'DHA Suffa University'})
    MERGE (cs:Subject {name: 'Computer Science'})
    MERGE (techsoft:Company {name: 'TechSoft'})
    
    MERGE (ali)-[:IS_STUDENT_OF]->(dsu)
    MERGE (ali)-[:STUDIES]->(cs)
    MERGE (ali)-[:KNOWS]->(ahmed)
    MERGE (ahmed)-[:WORKS_AT]->(techsoft)
    """
    driver = None
    try:
        driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
        with driver.session() as session:
            session.run(query)
            print("\n[SUCCESS] succesfully run.")
    except Exception as e:
        print("\n[DATABASE ERROR] Setup fail", e)
    finally:
        if driver:
            driver.close()
             # task 6
def fetch_data_query():
    query = """
    MATCH (student:Person {name: 'Ali'})-[:IS_STUDENT_OF]->(univ),
          (student)-[:STUDIES]->(sub),
          (student)-[:KNOWS]->(friend),
          (friend)-[:WORKS_AT]->(comp)
    RETURN student.name AS student, univ.name AS university, sub.name AS subject, friend.name AS friend, comp.name AS company
    """
    driver = None
    try:
        driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
        with driver.session() as session:
            result = session.run(query)
            return [dict(record) for record in result]
    except Exception as e:
        print("\n[FETCH ERROR] Data nikalne mein masla:", e)
        return []
    finally:
        if driver:
            driver.close()
@app.route('/api/graph', methods=['GET'])
def get_graph_data():
    data = fetch_data_query()
    if not data:
        return jsonify({"error": "No data found or connection failed"}), 500
    return jsonify(data)
if __name__ == '__main__':
    setup_database()  
    app.run(port=5000)