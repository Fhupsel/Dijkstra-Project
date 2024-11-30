from flask import Flask, render_template, request, jsonify
from dijkstra import dijkstra

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    graph = data['graph']
    start = data['start']
    
    result = dijkstra(graph, start)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
