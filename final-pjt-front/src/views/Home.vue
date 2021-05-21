<template>
  <div>
    <h1>Home</h1> 
    <MovieList :movies="movies"/>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '@/components/MovieList'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Home',
  components: {
    MovieList,
  },
  data: function () {
    return {
      movies: [],
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
  },
  mounted() {
    this.getMovies()
  }
}
</script>

<style>

</style>