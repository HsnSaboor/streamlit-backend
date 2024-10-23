from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample task storage
tasks = []

@app.route('/task', methods=['POST'])
def create_task():
    task_data = request.json
    tasks.append(task_data)  # Save task
    return jsonify(task_data), 201

@app.route('/task', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

if __name__ == '__main__':
    app.run(port=8080)  # Ensure it's running on port 8080
