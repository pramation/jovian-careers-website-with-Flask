from flask import Flask, render_template,jsonify,request
from database import load_jobs_from_db,get_job_from_db, apply_to_job_db

app= Flask(__name__)

@app.route("/")
def hello_world():
  jobs=load_jobs_from_db()
  return render_template('home.html', jobs=jobs)

@app.route("/api/jobs")
def get_jobs():
  jobs=load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job=get_job_from_db(id)
  if not job:
    return "Job Not Found",404
  return render_template('jobpage.html', job=job)

@app.route("/job/<id>/apply" , methods=['post'])
def  apply_to_job(id):
  data= request.form
  job=get_job_from_db(id)
  apply_to_job_db(id,data)
  return render_template('application_submitted.html',application=data,job=job)
  
if __name__=="__main__":
 app.run(host='0.0.0.0', debug=True)