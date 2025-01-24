from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for items
categories = {
    "1": {"name": "Food", "items": {"1": "Pizza", "2": "Burger"}},
    "2": {"name": "Groceries", "items": {"1": "Rice", "2": "Sugar"}},
    "3": {"name": "Fruits", "items": {"1": "Apple", "2": "Banana"}},
}

cart = {}

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
