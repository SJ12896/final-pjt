import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default new Vuex.Store({
  state: {
    movies: null,
    config: null,
    selectedMovies : [],
  },
  mutations: {
    SET_TOKEN: function(state, config) {
      state.config = config
    },
    GET_MOVIES: function(state, movies) {
      state.movies = movies
    },
    SELECT_MOVIE : function (state, movieItem) {
          const idx = state.selectedMovies.indexOf(movieItem)
          if (idx === -1) {
            state.selectedMovies.push(movieItem)
          } else {
            state.selectedMovies.splice(idx, 1)
          }
      },
      COLLECTION_RESET : function (state) {
        state.selectedMovies = [];
      }
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
    },
    selectMovie: function ({ commit }, movieItem) {
      commit('SELECT_MOVIE', movieItem)
    },
    saveCollection: function ({ commit }, data) {
      const token = localStorage.getItem('jwt')
      let form = new FormData()
      let movies = []
      for (let i = 0; i < this.state.selectedMovies.length; i++ ) {
        movies.push(this.state.selectedMovies[i]['id'])
      }
      form.append('movies', movies)
      form.append('title', data.title)
      form.append('info', data.info)
      axios({
        method: 'post',
        url: `${SERVER_URL}/movies/collections_all/`,
        data: form,
        headers: {
          Authorization: `JWT ${token}`
          }
        })
        .then (() => {
          commit('COLLECTION_RESET')
        })
        .catch((err) => {
          console.log(err)
        })
  },
},
  modules: {
  },
  getters: {

  }
})
