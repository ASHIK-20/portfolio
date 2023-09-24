from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('ashikk.html')

@app.route('/contact')
def contact():
    return render_template ('contact.html')

@app.route('/skills')
def homepage():
    return render_template('skills.html')
    
@app.route('/thanks')
def homepage():
    return render_template('thanks.html')


if __name__=='__main__':
    app.run(debug = False,host='0.0.0.0')
