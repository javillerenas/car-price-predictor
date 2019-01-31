<template>
  <div id="app">
    <HeroComponent>
      <PredictForm />
    </HeroComponent>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import PredictForm from "./components/PredictForm.vue";
import HeroComponent from "./components/HeroComponent.vue";

@Component({
  components: {
    PredictForm,
    HeroComponent
  }
})
export default class App extends Vue {}
</script>

<style lang="scss">
#app {
  font-size: 10px;
}
</style>
