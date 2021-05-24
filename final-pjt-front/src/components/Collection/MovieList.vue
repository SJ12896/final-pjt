<template>
  <div>
      <div v-if="movies.length === 0">
        찾는 영화가 없습니다.
      </div>
    <div>
      <MovieItem v-for="(movie, idx) in movies" :key="idx" :movie="movie" />
    </div>
  </div>
</template>

<script>
import MovieItem from '@/components/Collection/MovieItem'
export default {
  name: 'MovieList',
  props: {
    movies: Array,
  },
  components: {
    MovieItem,
  },
}
</script>

<style>

</style>