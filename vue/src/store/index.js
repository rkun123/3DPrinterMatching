<<<<<<< Updated upstream
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    key: ""
  },
  mutations: {
    setKey(state, payload) {
      this.key = payload;
      console.log(this.key)
    }
  },
  actions: {
    setUserKey({
      commit,
    }, {
      key
    }) {
      commit('setKey', key)
    },
  },
  modules: {}
})
=======
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const state = {
    setUserKey: ""
};

const store = new Vuex.Store({
    state
});

export default store;
>>>>>>> Stashed changes
