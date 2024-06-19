from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    user_message = data.get('message', '')
    
    if 'hello' in user_message.lower():
        response_message = "Hi there! How can I help you today?"
    else:
        response_message = "I'm not sure how to respond to that."

    response = {
        'reply': response_message
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)