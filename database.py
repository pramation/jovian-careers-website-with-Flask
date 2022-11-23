from sqlalchemy import create_engine, text
import os
db_connection_string=os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                      connect_args={
                        "ssl":{"ssl_ca":"/etc/ssl/cert.pem"}
                      })



def load_jobs_from_db():
  with engine.connect() as conn:
    result=conn.execute(text("select * from jobs"))
    jobs=[]
    for row in result.all():
      jobs.append(dict(row))

    return jobs

def get_job_from_db(id):
  with engine.connect() as conn:
    result=conn.execute(text("select * from jobs where id=:value1"),value1=id)
    rows=result.all()
    if len(rows)==0:
      return None
    else:
      return(dict(rows[0]))

def apply_to_job_db(job_id,application_data):
  q_text=text("INSERT into applications(job_id,\
                  full_name,\
                  email,\
                  linkedin_url,\
                  education,\
                  work_experience,\
                  resume_url)\
         VALUES ( :job_id,\
                  :full_name,\
                  :email,\
                  :LinkedinURL,\
                  :Education,\
                  :Experience,\
                  :resumeURL)")

  with engine.connect() as conn:
    conn.execute(q_text,job_id=job_id,
                      full_name=application_data['full_name'],
                      email=application_data['email'],
                      LinkedinURL=application_data['LinkedinURL'],
                      Education=application_data['Education'],
                      Experience=application_data['Experience'],
                      resumeURL=application_data['resumeURL'])

    
  
