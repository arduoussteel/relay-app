from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/get_model_details", methods=["GET"])
def get_model_details():
    return jsonify({
        "model_name": "Qwen/Qwen2.5-72B-Instruct",  # Replace with your model
        "api_key": "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"  # Replace with your API key
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
