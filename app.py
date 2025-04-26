from flask import Flask, request, jsonify
import os

app = Flask(__name__)
CODE_DIR = 'codes'

if not os.path.exists(CODE_DIR):
    os.makedirs(CODE_DIR)

@app.route('/upload', methods=['POST'])
def upload_code():
    data = request.get_json()
    filename = data.get('filename')
    code = data.get('code')
    if filename and code:
        file_path = os.path.join(CODE_DIR, filename)
        with open(file_path, 'w') as f:
            f.write(code)
        return jsonify({'message': 'Code uploaded successfully'}), 200
    return jsonify({'message': 'Invalid request'}), 400

@app.route('/download/<filename>', methods=['GET'])
def download_code(filename):
    file_path = os.path.join(CODE_DIR, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            code = f.read()
        return jsonify({'code': code}), 200
    return jsonify({'message': 'File not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
    