<template>
  <div class="about">
    <PredictedCard :price="price" :carName="name" />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import PredictedCard from "../components/PredictedCard.vue";

@Component({
  components: {
    PredictedCard,
  },
  computed: {
    price () {
      return this.$store.getters.getPrice;
    },
    name () {
      return this.$store.getters.getCarName;
    }
  }
})
export default class App extends Vue {}
</script>