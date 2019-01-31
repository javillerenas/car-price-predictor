/* eslint-disable import/no-extraneous-dependencies */
import { storiesOf } from "@storybook/vue";
import { action } from "@storybook/addon-actions";
import { linkTo } from "@storybook/addon-links";

import MyButton from "../components/MyButton.vue";
import PredictForm from "../components/PredictForm.vue";
import PredictedCard from "../components/PredictedCard.vue";
import HeroComponent from "../components/HeroComponent.vue";

storiesOf("Button", module)
  .add("with text", () => ({
    components: { MyButton },
    template: '<my-button @click="action">Hello Button</my-button>',
    methods: { action: action("clicked") }
  }))
  .add("with JSX", () => ({
    components: { MyButton },
    render() {
      return <my-button onClick={this.action}>With JSX</my-button>;
    },
    methods: { action: linkTo("Button", "with some emoji") }
  }))
  .add("with some emoji", () => ({
    components: { MyButton },
    template: '<my-button @click="action">😀 😎 👍 💯</my-button>',
    methods: { action: action("clicked") }
  }));

storiesOf("PredictForm", module)
  .add("default form", () => ({
    components: { PredictForm },
    template: '<PredictForm />',
  }))
  .add("with Hero Component", () => ({
    components: { 
      PredictForm,
      HeroComponent
    },
    template: '<HeroComponent><PredictForm /></HeroComponent>',
  }))
  
storiesOf("PredictedCard", module)
  .add("default form", () => ({
    components: { PredictedCard },
    template: '<PredictedCard />',
  }))
  .add("with Hero Component", () => ({
    components: { 
      PredictedCard,
      HeroComponent
    },
    template: '<HeroComponent><PredictedCard price="12000" carName="bwm" /></HeroComponent>',
  }))