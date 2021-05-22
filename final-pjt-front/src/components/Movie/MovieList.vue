<template>
  <div>
    <MovieListItem v-for="(movie,idx) in movies" :key="idx" :movie="movie" />
  </div>
</template>

<script>
// import _ from 'lodash'
import MovieListItem from '@/components/Movie/MovieListItem'

export default {
  name:'MovieList',
  components: {
    MovieListItem,
  },
  props: {
    movies: Array,
  }
}
</script>

<style>

</style>