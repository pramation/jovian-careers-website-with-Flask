from flask import Flask, render_template,jsonify
print("Hello")

app= Flask(__name__)

JOBS=[
  {'id':1,"title":"Data Analyst","location":"Delhi, India","salary":"Rs. 70,00,000"},
  {'id':2,"title":"Data Scientist","location":"Pune, India"},
  {'id':3,"title":"Data Engineer","location":"Dallas, USA","salary":"$ 120,000"}
  
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def get_jobs():
  return jsonify(JOBS)

if __name__=="__main__":
 app.run(host='0.0.0.0', debug=True)