
<template>
  <div class="card">
    <figure class="card__img">
      <img src="https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/vdat/submodels/bmw_m8-gran-coupe_bmw-concept-m8-gran-coupe_2018-1532968589970.jpg" alt="bmw">
    </figure>
    <h1 class="card__title">Price for {{carName}}:</h1>
    <div class="btn card__price">$ {{price}} USD</div>
    <div class="btn card__return" @click="goHome()">🔙 return</div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component({
  props: {
    price: Number,
    carName: String
  }
})
export default class PredictedCard extends Vue {
  goHome () {
    this.$router.go(-1);
  }
}
</script>

<style lang="scss">

$grey: #ccc;
$blue: #448bc9;
$green: #0DFFDF;
$input-border: 1px solid $grey;

.btn {
  text-align: center;
  border: $input-border;
  padding: 0.3rem 1rem;
  margin: 0.3rem;
  font-size: 1.2rem;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.card {
  max-width: 25rem;
  padding: 2rem 3rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  background-color: white;
  box-shadow: 0px 0px 2px #555;
  font-family: 'Poppins', sans-serif;
  color: #333333;

  &__title {
    font-size: 2rem;
    margin: 0 0 0.5rem;
  }

  &__img {
    width: 80%;
    margin-bottom: 0;
    img {
      width: 100%;
      border-radius: 10px;
    }
  }

  &__price {
    font-size: 2.5rem;
    color: $green;
    border: 1px solid $green;
  }

  &__return{
    margin-top: 3rem;

    &:hover {
      height: 2rem;
      width: 6rem;
      box-shadow: 0px 0px 10px lighten($blue, 0.5);
    }
  }
}

</style>

