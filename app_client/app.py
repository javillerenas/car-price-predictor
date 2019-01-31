## *****************************
##
##     ___ _ _            _   
##    / __\ (_) ___ _ __ | |_ 
##   / /  | | |/ _ \ '_ \| __|
##  / /___| | |  __/ | | | |_ 
##  \____/|_|_|\___|_| |_|\__|
##
## *****************************

from flask import Flask, session, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from forms import CarForm
import requests, json   # for post request to predictor

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Super extra secret key'
bootstrap = Bootstrap(app)

PREDICTOR_URL = "http://127.0.0.1:8080/api"

## ===== Data =======
##
MARKS = ['Peugeot', 'Renault', 'Citroen', 'Mercedes-Benz', 'Ford', 'Nissan',
       'Fiat', 'Skoda', 'Hyundai', 'Kia', 'Dacia', 'Opel', 'Volkswagen',
       'mini', 'Seat', 'Isuzu', 'Honda', 'Mitsubishi', 'Toyota', 'BMW',
       'Chevrolet', 'Audi', 'Suzuki', 'Ssangyong', 'lancia', 'Jaguar',
       'Volvo', 'Autres', 'BYD', 'Daihatsu', 'Land Rover', 'Jeep',
       'Chery', 'Alfa Romeo', 'Bentley', 'Daewoo', 'Hummer', 'Mazda',
       'Chrysler', 'Maserati', 'Cadillac', 'Dodge', 'Rover', 'Porsche',
       'GMC', 'Infiniti', 'Changhe', 'Geely', 'Zotye', 'UFO', 'Foton',
       'Pontiac', 'Acura', 'Lexus'
]

FUEL_TYPE = ['Diesel', 'Essence', 'Electrique', 'LPG']

marks     = [(x,x) for x in MARKS]
fuel_type = [(x,x) for x in FUEL_TYPE] 
## ===== ==== =====


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CarForm()
    form.make.choices      = marks 
    form.fuel_type.choices = fuel_type

    if form.validate_on_submit():

        ## make api call to predictor
        car_make = form.make.data
        data = json.dumps({
            'year_model':   form.year.data, 
            'mileage':      form.miles.data,
            'fiscal_power': form.fiscal_pow.data, 
            'fuel_type':    form.fuel_type.data, 
            'mark':         car_make
        })
        r = requests.post(PREDICTOR_URL, data)
        car_price = float( r.json()['price'] * 0.27 )
        return render_template('priced.html', car_make=car_make, car_price=car_price, make='AAA')
    
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)