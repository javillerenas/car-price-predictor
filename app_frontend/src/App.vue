<template>
  <div id="app">
    <HeroComponent>
      <router-view></router-view>
      <!-- <PredictForm />
      <PredictedCard :price="50000" carName="bmw" /> -->
    </HeroComponent>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import PredictForm from "./components/PredictForm.vue";
import PredictedCard from "./components/PredictedCard.vue";
import HeroComponent from "./components/HeroComponent.vue";

@Component({
  components: {
    PredictForm,
    PredictedCard,
    HeroComponent
  }
})
export default class App extends Vue {}
</script>

<style lang="scss">
html {
  width: 100%;
  height: 100%;
}

body {
  padding: 0;
  margin: 0;
}

#app {
  font-size: 10px;
}
</style>