# task.py
import robyn
import json
from robyn import Robyn

# Create an instance of the Robyn app
app = Robyn(file_object=None)

tasks = []

@app.route('/task', methods=['GET', 'POST'])
async def handle_tasks(request):
    if request.method == 'GET':
        return json.dumps(tasks)

    elif request.method == 'POST':
        task_data = await request.json()
        task_name = task_data.get('name', None)
        if task_name:
            task = {'name': task_name}
            tasks.append(task)
            return json.dumps(task), 201
        return {'error': 'Task name is required'}, 400

if __name__ == '__main__':
    app.run()
