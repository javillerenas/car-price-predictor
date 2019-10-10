import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    price: 0,
    carName: ''
  },
  mutations: {
    setPrice (state, price) {
      state.price = price;
    },
    setCarName (state, name) {
      state.carName = name;
    }
  },
  getters: {
    getPrice: state => state.price,
    getCarName: state => state.carName
  },
  actions: {}
});
