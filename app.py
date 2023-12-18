from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/task', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        'id': len(tasks) + 1,
        'task': data['task'],
        'completed': False
    }
    tasks.append(new_task)
    return jsonify({'message': 'Task created successfully'})


@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            data = request.get_json()
            task['task'] = data.get('task', task['task'])
            task['completed'] = data.get('completed', task['completed'])
            return jsonify({'message': 'Task updated successfully'})
    return jsonify({'message': 'Task not found'}), 404


@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return jsonify({'message': 'Task deleted successfully'})
    return jsonify({'message': 'Task not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
