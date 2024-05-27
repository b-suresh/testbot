# app.py
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message')
    response = generate_response(user_input)
    return jsonify({"response": response})

def generate_response(user_input):
    client = OpenAI(
        # This is the default and can be omitted
        api_key='',
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    app.run(debug=True)