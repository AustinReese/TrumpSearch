from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import Form, StringField, validators
from wtforms.validators import Length, ValidationError, DataRequired
from fetch_data import fetch_data
from os import environ


app = Flask(__name__)
app.config['SECRET_KEY'] = "titanic_data_storage"
bootstrap = Bootstrap(app)

class FilterForm(FlaskForm):    
    
    mentioned = StringField("Mentioned users (omit @)", validators = [Length(max=60)])
    hashtag = StringField("Hashtags used (omit #)", validators = [Length(max=60)])
    keystring = StringField("Search Keystring", validators = [Length(max=60)])
    

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FilterForm()
    success = True
    if form.is_submitted():
        data, headers = fetch_data(form)
        if len(data) != 0:
            return render_template("search.html", data = data, headers = headers)
        else:
            success = False
    return render_template("index.html", form = form, success = success)

if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port = port, debug = True)
