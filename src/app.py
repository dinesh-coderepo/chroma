from flask import Flask, request, send_from_directory
from flask_cors import CORS
import os
from clients.js.src.ChromaClient import ChromaClient
from clients.js.src.Collection import Collection

app = Flask(__name__, static_folder='../clients/js/examples/browser/dist')
CORS(app)

chroma = ChromaClient(path="http://localhost:8000")

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    collection = chroma.getOrCreateCollection(name="demo-collection")
    collection.uploadFile(file)

    return 'File uploaded successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
