from flask import Flask, request, jsonify
from model.gpt2_caption_generator import CaptionGenerator

app = Flask(__name__)
caption_generator = CaptionGenerator()

@app.route("/generate", methods=["POST"])
def generate_caption():
    data = request.get_json()
    prompt = data.get("prompt", "")
    style = data.get("style", "default")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    caption = caption_generator.generate_caption(prompt, style)
    return jsonify({"caption": caption})

if __name__ == "__main__":
    app.run(debug=True)
