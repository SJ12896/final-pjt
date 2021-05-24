<template>
  <div>
    <h1>Home</h1>
    <MovieList :movies="movies"/>
  </div>
</template>

<script>
// import _ from 'lodash'
import axios from 'axios'
import MovieList from '@/components/Movie/MovieList'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Home',
  components: {
    MovieList,
  },
  data: function () {
    return {
      movies: null,
    }
  },
  methods: {
    setToken: function( ) {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    getMovies: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/movies/movie/`,config)
      .then((res) => {
        console.log(res.data)
        this.movies = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getCollections: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/movies/collection_all/`, config)
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    }

  },
  mounted() {
    this.getMovies()
    this.getCollections()
  }
}
</script>

<style>

</style>