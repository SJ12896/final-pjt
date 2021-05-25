<template>
  <div>
    <MovieList :movies="movies"/>
  </div>
</template>

<script>
// import _ from 'lodash'
import axios from 'axios'
import{ mapActions, mapState } from 'vuex'
import MovieList from '@/components/Movie/MovieList'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Home',
  components: {
    MovieList,
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
    getCollections: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/movies/collection_all/`, config)
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    ...mapActions({
      init: 'getMovies'
    })
  },
  computed:{
    ...mapState([
      'movies',
    ])
  },
  mounted() {
    this.getCollections()
    this.init()
  }
}
</script>

<style>

</style>