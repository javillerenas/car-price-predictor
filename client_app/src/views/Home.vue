<template>
  <div class="home">
    <PredictForm />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import PredictForm from "../components/PredictForm.vue";

@Component({
  components: {
    PredictForm
  }
})
export default class Home extends Vue {}
</script>
