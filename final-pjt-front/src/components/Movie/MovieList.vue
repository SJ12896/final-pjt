<template>
  <div>
    <h2>MovieList</h2>
    <h1 v-for="(movie,idx) in movies" :key="idx" movie="movie" >
      {{ movie.title }}
    </h1>
  </div>
</template>

<script>
// import { mapState } from 'vuex'

export default {
  name:'MovieList',
  props: {
    movies: Array,
  }
}
</script>

<style>

</style>