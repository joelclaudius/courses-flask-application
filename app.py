from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'company': 'Google',
        'location': 'Mountain View, CA',
        'salary': '$150,000 - $200,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'company': 'Facebook',
        'location': 'Menlo Park, CA',
        'salary': '$140,000 - $180,000'
    },
    {
        'id': 3,
        'title': 'Product Manager',
        'company': 'Apple',
        'location': 'Cupertino, CA',
        'salary': '$160,000 - $200,000'
    },
    {
        'id': 4,
        'title': 'Software Engineer',
        'company': 'Amazon',
        'location': 'Seattle, WA',
        'salary': '$130,000 - $170,000'
    },
    {
        'id': 5,
        'title': 'Data Scientist',
        'company': 'Netflix',
        'location': 'Los Gatos, CA',
        'salary': '$150,000 - $190,000'
    },
    {
        'id': 6,
        'title': 'Product Manager',
        'company': 'Tesla',
        'location': 'Palo Alto, CA',
        'salary': '$170,000 - $210,000'
    }

]

@app.route('/')
def index():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)




if __name__ == '__main__':
    app.run(debug=True)