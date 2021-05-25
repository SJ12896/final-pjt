<template>
  <div>
    <img @click="goMovieDetail(movie.id)" :src="movieImage" alt="movie_image">
  </div>
</template>

<script>

export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  },
  methods:{
    goMovieDetail: function (movieId) {
      this.$router.push({ name: 'MovieDetail', params: { movieId: movieId}})
    }
  },
  computed: {
    movieImage: function () {
      return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
      }
  },
}
</script>

<style>

</style>