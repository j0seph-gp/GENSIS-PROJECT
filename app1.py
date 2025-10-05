from flask import Flask, request, jsonify

app = Flask(__name__)

# This is a FAKE database of NASA studies for the demo
fake_nasa_data = {
    "radiation": [
        {"id": "GLDS-194", "title": "Study on DNA repair in mice under simulated cosmic radiation", "relevance": 0.9},
        {"id": "GLDS-205", "title": "Effects of radiation on plant germination", "relevance": 0.8}
    ],
    "microgravity": [
        {"id": "GLDS-168", "title": "Rodent muscle atrophy in long-duration microgravity", "relevance": 0.95},
        {"id": "GLDS-48", "title": "Cardiovascular deconditioning in mice aboard the ISS", "relevance": 0.85}
    ],
    "plant": [
        {"id": "GLDS-205", "title": "Effects of radiation on plant germination", "relevance": 0.8},
        {"id": "GLDS-123", "title": "Root growth patterns in microgravity", "relevance": 0.7}
    ]
}

@app.route("/")
def index():
    return """
    <h1>GeneSIS Project Demo</h1>
    <p>This is a simplified demo for the NASA Space Apps Challenge.</p>
    <p>Use /search?q=your_query to test.</p>
    <p>Example: <a href="/search?q=radiation">/search?q=radiation</a></p>
    <p>Example: <a href="/search?q=microgravity">/search?q=microgravity</a></p>
    """

@app.route("/search")
def search():
    query = request.args.get('q', '').lower()
    results = []

    # Simple keyword matching to simulate AI search
    for keyword, studies in fake_nasa_data.items():
        if keyword in query:
            results.extend(studies)

    if not results:
        return jsonify({"message": "No results found for your query.", "query": query})

    # Sort results by relevance
    sorted_results = sorted(results, key=lambda x: x['relevance'], reverse=True)
    return jsonify({"query": query, "results": sorted_results})

if __name__ == "__main__":
    app.run(debug=True)
