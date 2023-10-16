from flask import Flask, jsonify, render_template

app = Flask(__name__)
JOBS = [
    {
        'location': 'india',
        'title': "seo",
        'company': "google",
        'description':'sssss'
    },
    {
        'location': 'us',
        'title': "leo",
        'company': "facebook",
        'description':'sssss'
    },
    {
        'location': 'eu',
        'title': "seraaa",
        'company': "netflix",
        'description':'sssss'
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html',jobs=JOBS)
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__=='__main__':
  
  app.run(host='0.0.0.0', debug=True)