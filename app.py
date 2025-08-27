from flask import Flask, request, render_template
app = Flask(__name__)

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/")
def home():
    return render_template("index.html", result=None)

@app.post("/calc")
def calc():
    a = float(request.form.get("a", 0))
    b = float(request.form.get("b", 0))
    return render_template("index.html", result={"sum": a+b, "diff": a-b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
