<template>
  <div>
    <h1>Detail</h1>
    <button @click="goCreateReview">리뷰쓰기</button>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL


export default {
  name: 'MovieDetail',
  data: function () {
    return {
      movieReviews: null,
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
    getMovieReviews: function(movie) {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/community/movie/${movie.id}`,config)
      .then((res) => {
        console.log(res)
        this.movieReviews = res
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goCreateReview: function(review) {
      this.$router.push({ name: 'CreateReview', params: review.id})
    }
  }
}
</script>

<style>

</style>