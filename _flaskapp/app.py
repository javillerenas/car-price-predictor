from flask import Flask, session, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from forms import CarForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Super extra secret key'
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CarForm()
    form.make.choices = [('uno','uno'), ('dos','dos'), ('tres','tres')]
    if form.validate_on_submit():
       car_name  = form.make.data
       car_price = 22_000 # make api call
    #    return redirect(url_for('index'))
       return render_template('priced.html', car_name=car_name, car_price=car_price)
    return render_template('index.html', form=form)

# @app.route('/priced')
# def present_price():
#     return render_template('priced.html')

if __name__ == "__main__":
    app.run(debug=True)