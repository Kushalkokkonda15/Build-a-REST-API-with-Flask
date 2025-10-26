from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = len(users) + 1
    users[user_id] = {
        'id': user_id,
        'name': data.get('name'),
        'email': data.get('email')
    }
    return jsonify(users[user_id]), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    users[user_id].update({
        'name': data.get('name', users[user_id]['name']),
        'email': data.get('email', users[user_id]['email'])
    })
    return jsonify(users[user_id])
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        deleted = users.pop(user_id)
        return jsonify({'message': 'User deleted', 'user': deleted})
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
