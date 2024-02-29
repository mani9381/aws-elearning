from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def ind():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/404')
def four():
    return render_template('404.html')
@app.route('/courses')
def course():
    return render_template('courses.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/testimonial')
def testmonial():
    return render_template('testimonial.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")