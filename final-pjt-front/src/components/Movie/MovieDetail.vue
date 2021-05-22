<template>
  <div>
    <h1>Detail</h1>
    <MovieReviews :movieId="movieId"/>
    <button @click="goCreateReview" >리뷰쓰기</button>
  </div>
</template>

<script>
import MovieReviews from '@/components/Movie/MovieReviews'

export default {
  name: 'MovieDetail',
  components: {
    MovieReviews,
  },
  data: function () {
    return {
      movieId: this.$route.params.movieId,
    }
  },
   methods: {
    goCreateReview: function() {
      this.$router.push({ name: 'CreateReview'})
    }
  }
}
</script>

<style>

</style>