<template>
  <div>
    <h1>{{ movieId }}</h1>
    <div>
      <ul>
        <li v-for="(review) in movieReviews" v-bind:key="review">
        <p @click="goReviewDetail(review.id)">{{ review }}</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieReviews',
  props: {
    movieId: Object,
  },
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
    getMovieReviews: function() {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/community/movie/${this.movieId}`,config)
      .then((res) => {
        console.log(res)
        this.movieReviews = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goReviewDetail: function (reviewId) {
      this.$router.push({ name: 'ReviewDetail', params: {reviewId: reviewId}})
    }
  },
  mounted() {
    this.getMovieReviews()
  }
}
</script>

<style>

</style>