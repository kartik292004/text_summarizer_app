from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)
summarizer = pipeline("summarization")

@app.route("/", methods=["GET", "POST"])
def summarize():
    summary = ""
    if request.method == "POST":
        text = request.form["text"]
        if text:
            summary_output = summarizer(text, max_length=130, min_length=30, do_sample=False)
            summary = summary_output[0]["summary_text"]
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
