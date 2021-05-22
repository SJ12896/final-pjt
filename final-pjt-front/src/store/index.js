import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

Vue.use(Vuex)

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default new Vuex.Store({
  state: {
    movies: null,
    config: null,
  },
  mutations: {
    SET_TOKEN: function(state, config) {
      state.config = config
      console.log(config)
    },
    GET_MOVIES: function(state, movies) {
      state.movies = movies
      console.log(movies)
    },
  },
  actions: {
    setToken: function({commit} ) {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      commit('SET_TOKEN', config)
    },
    getMovies: function ({commit}) {
      const config = this.settoken()
      axios.get(`${SERVER_URL}/movies/movie/`,config)
      .then((res) => {
        console.log(res)
        commit('GET_MOVIES', res)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  modules: {
  },
  getters: {

  }
})
