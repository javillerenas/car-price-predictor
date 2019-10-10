<template>
  <div class="predict-form">
    <h1 class="predict-form__title">Carval</h1>

    <form action="" class="predict-form__form">
      <div class="predict-form__input">
        <p for="" class="predict-form__label">Year</p>
        <input type="text" v-model="year" class="predict-form__input" required>
      </div>
      <div class="predict-form__input">
        <p for="" class="predict-form__label">Mileage</p>
        <input type="text" v-model="mileage" class="predict-form__input" required>
      </div>
      <div class="predict-form__input">
        <p for="" class="predict-form__label">Make</p>
        <select v-model="make" class="predict-form__input">
          <option v-for="m in MAKE_OPTIONS" :key="m">{{m}}</option>
        </select>
      </div>
      <div class="predict-form__input">
        <p for="" class="predict-form__label">Fuel Type</p>
        <div class="select-multiple">
          <button 
            v-for="type in FUEL_TYPE" 
            :key="type" 
            @click.prevent="selectFuelType(type)" 
            :class="{'btn': true, 'btn-active': fuelType === type}">
              {{type}}
          </button>
        </div>
      </div>
      <div class="predict-form__input">
        <p for="" class="predict-form__label">Fiscal Power</p>
        <input type="text" v-model="fiscalPower" class="predict-form__input" required>
      </div>
      <button class="btn predict-form__submit-button" @click.prevent="sendFormData()">
        💸 Predict Price 💸
      </button>
    </form>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import axios from 'axios';

const HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST"
  // "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token"
}

@Component({
  components: {
  }
})
export default class PredictForm extends Vue {
  PREDICTOR_URL = "http://127.0.0.1:8080/api";

  MAKE_OPTIONS = [
    'Peugeot', 'Renault', 'Citroen', 'Mercedes-Benz', 'Ford', 'Nissan',
    'Fiat', 'Skoda', 'Hyundai', 'Kia', 'Dacia', 'Opel', 'Volkswagen',
    'mini', 'Seat', 'Isuzu', 'Honda', 'Mitsubishi', 'Toyota', 'BMW',
    'Chevrolet', 'Audi', 'Suzuki', 'Ssangyong', 'lancia', 'Jaguar',
    'Volvo', 'Autres', 'BYD', 'Daihatsu', 'Land Rover', 'Jeep',
    'Chery', 'Alfa Romeo', 'Bentley', 'Daewoo', 'Hummer', 'Mazda',
    'Chrysler', 'Maserati', 'Cadillac', 'Dodge', 'Rover', 'Porsche',
    'GMC', 'Infiniti', 'Changhe', 'Geely', 'Zotye', 'UFO', 'Foton',
  ]
  FUEL_TYPE = ['Diesel', 'Essence', 'Electrique', 'LPG']

  // vars
  year = 2013;
  mileage = 10000;
  make = this.MAKE_OPTIONS[0];
  fuelType = this.FUEL_TYPE[0];
  fiscalPower = 7;

  selectFuelType(type: any) {
    this.fuelType = type;
  }

  sendFormData() {
    console.log('send info');
    let payload = {
      'year_model':   this.year, 
      'mileage':      this.mileage,
      'fiscal_power': this.fiscalPower, 
      'fuel_type':    this.fuelType, 
      'mark':         this.make
    }
    axios.post(this.PREDICTOR_URL, payload, {headers: HEADERS}).then(res => {
      console.log("price: ", res.data.price);
      this.$store.commit('setPrice', res.data.price);
      this.$store.commit('setCarName', payload.mark);
      this.$router.push('about');
    });
  }
}
</script>

<style lang="scss">

$grey: #ccc;
$blue: #448bc9;
$input-border: 1px solid $grey;

button.btn {
  font-size: 1.2rem;
  border-radius: 5px;
}

.predict-form {
  max-width: 25rem;
  padding: 2rem 3rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  background-color: white;
  box-shadow: 0px 0px 2px #555;

  .predict-form__title {
    text-align: center;
    font-family: 'Poppins', sans-serif;
    font-size: 4rem;
    color: #333333;
    line-height: 1.2;
    margin-bottom: 0.5rem;
  }

  &__form {
    font-family: "poppins";
    display: flex;
    flex-direction: column;
    width: 100%;

    p {
      margin-bottom: 0px;
    }

    .predict-form__label {
      font-weight: 600;
      font-size: 1rem;
    }

    .predict-form__input {
      box-sizing: border-box;
      color: #333;

      input {
        width: 100%;
        border: $input-border;
        border-radius: 5px;
        background-image: none;
        height: 2rem;
        padding: 0.3rem 1rem;
        font-size: 1rem;
      }

      select {
        font-size: 1rem;
        width: 100%;
        height: 2rem;
        padding: 0.3rem 1rem;
        background: white;
        border: $input-border;
      }

      .select-multiple {
        display: flex;

        .btn {
          outline: none;
          flex-basis: 100%;
          color: #333;
          border: $input-border;
          margin: 0.1rem 0.2rem 0;

          &-active {
            color: white;
            border: none;
            background: $blue;
            box-shadow: 0px 0px 1px lighten($blue, 0.5);
          }
        }
      }
    }

    .predict-form__submit-button {
      margin-top: 2rem;
      background-color: $blue;
      color: white;
      margin-left: auto;
      margin-right: auto;
      border-radius: 5px;
      height: 3rem;
      border: none;
      outline: none;
      transition: all 0.2s ease;

      &:hover {
        height: 3.5rem;
        width: 13rem;
        box-shadow: 0px 0px 10px lighten($blue, 0.5);
      }
    }
  }
}
</style>

