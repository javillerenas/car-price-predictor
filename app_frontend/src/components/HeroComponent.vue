<template>
  <div class="hero">
    <slot></slot>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
@Component({
  components: {
  }
})
export default class HeroComponent extends Vue {
}
</script>

<style lang="scss" scoped>
.hero {
  width: 100vw;
  height: 100vh; 
  display: flex;
  align-items: center;
  justify-content: center;
  background: #a64bf4;
  /* background: -webkit-linear-gradient(45deg, #00dbde, #fc00ff);
  background: -o-linear-gradient(45deg, #00dbde, #fc00ff);
  background: -moz-linear-gradient(45deg, #00dbde, #fc00ff); */
  background: linear-gradient(45deg, #00dbde, #fc00ff);
}
</style>
