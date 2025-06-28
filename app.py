from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/evaluate', methods=['POST'])
def evaluate_transcript():
    data = request.json
    transcript = data.get("transcript")
    rubric = data.get("rubric")
    questions = data.get("questions")

    # Simulate evaluation logic
    feedback = f"Transcript reviewed. Key answers found for {len(questions)} questions."
    grade = "Pass" if "geometry" in transcript.lower() else "Needs Review"

    return jsonify({
        "grade": grade,
        "feedback": feedback
    })

@app.route('/')
def home():
    return "Agentic AI Grader is running."

if __name__ == '__main__':
    app.run(debug=True)
