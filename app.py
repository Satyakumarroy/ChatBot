from flask import Flask, request, render_template
from indexer import search_docs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}
    query = ""
    
    if request.method == "POST":
        query = request.form["query"]
        results = search_docs(query)
    
    return render_template("index.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
