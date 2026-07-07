from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "The Backend API is running successfully!"

@app.route('/add-item', methods=['POST'])
def add_item():
    item_name = request.form.get('item_name')
    quantity = request.form.get('quantity')
    expiry = request.form.get('expiry')
    item_data = {
        "name": item_name,
        "quantity": quantity,
        "expiry": expiry,
        "status": "available", 
        "message": "Item added successfully!"
    }
    return jsonify(item_data), 201

@app.route('/reserve-item', methods=['POST'])
def reserve_item():
    item_id = request.form.get('item_id')
    # TODO: Link MongoDB queries
    return jsonify(message="Item reserved successfully!"), 200

if __name__ == '__main__':
    app.run(debug=True)

