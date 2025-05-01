from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for items
categories = {
    "1": {"name": "Food", "items": {"1": "Pizza", "2": "Burger"}},
    "2": {"name": "Groceries", "items": {"1": "Rice", "2": "Sugar"}},
    "3": {"name": "Fruits", "items": {"1": "Apple", "2": "Banana"}},
}

cart = {}

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>USSD Simulator</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    padding: 30px;
                }
                h2 {
                    color: #333;
                }
                form {
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    max-width: 400px;
                    margin: auto;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }
                input[type="text"] {
                    width: 100%;
                    padding: 8px;
                    margin: 10px 0;
                    box-sizing: border-box;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                input[type="submit"] {
                    background-color: #28a745;
                    color: white;
                    padding: 10px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    width: 100%;
                }
                input[type="submit"]:hover {
                    background-color: #218838;
                }
            </style>
        </head>
        <body>
            <h2>Simulate USSD Request</h2>
            <form method="POST" action="/ussd">
                Session ID:<br>
                <input type="text" name="sessionId" value="12345"><br>
                Service Code:<br>
                <input type="text" name="serviceCode" value="*123#"><br>
                Phone Number:<br>
                <input type="text" name="phoneNumber" value="+1234567890"><br>
                USSD Text:<br>
                <input type="text" name="text"><br>
                <input type="submit" value="Send USSD Request">
            </form>
        </body>
        </html>
    ''')

@app.route('/ussd', methods=['POST'])
def ussd():
    session_id = request.form.get('sessionId')
    service_code = request.form.get('serviceCode')
    phone_number = request.form.get('phoneNumber')
    text = request.form.get('text')

    if text == "":
        # Initial menu
        response = "Customer Welcome to Food & Grocery Delivery:\n"
        response += "1. Food\n"
        response += "2. Groceries\n"
        response += "3. Fruits\n"
        return response

    inputs = text.split(" ")
    
    if len(inputs) == 1:
        # Select category
        selected = inputs[0]
        if selected in categories:
            items = categories[selected]["items"]
            response = f"Customer Select an item from {categories[selected]['name']}:\n"
            for key, value in items.items():
                response += f"{key}. {value}\n"
            return response
        else:
            return "END Invalid selection. Try again."

    elif len(inputs) == 2:
        # Add item to cart
        category = inputs[0]
        item_id = inputs[1]
        if category in categories and item_id in categories[category]["items"]:
            item_name = categories[category]["items"][item_id]
            cart[phone_number] = cart.get(phone_number, []) + [item_name]
            return f"END {item_name} added to your cart. Thank you for using our service!"
        else:
            return "END Invalid item selection. Try again."
    
    if len(inputs) == 3:
        # Select category
        selected = inputs[0]
        if selected in categories:
            items = categories[selected]["items"]
            response = f"Customer Select an item from {categories[selected]['name']}:\n"
            for key, value in items.items():
                response += f"{key}. {value}\n"
            return response
        else:
            return "END Invalid selection. Try again."

    else:
        return "END Invalid input. Start again."

if __name__ == "__main__":
    app.run(debug=True)
