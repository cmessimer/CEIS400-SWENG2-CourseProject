from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.get_json()
    user_id = data.get('user_id')
    equipment_id = data.get('equipment_id')
    # Simulate equipment checkout logic
    response = {
        "message": f"User {user_id} checked out equipment {equipment_id}."
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
