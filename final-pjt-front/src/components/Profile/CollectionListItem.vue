<template>
  <div>
    {{ collection.title }}
    {{ collection.info }}
    <span style="display: flex; justify-content: space-between;">
      <CollectionMovieList v-for="(movie, idx) in movies" :key="idx" :movie="movie" />
    </span>
  </div>
</template>

<script>
import CollectionMovieList from '@/components/Profile/CollectionMovieList.vue'
export default {
  name: 'CollctionListItem',
  components: {
    CollectionMovieList,
  },
  data: function() {
    return {
      movies: null,
  }},
  props: {
    collection: {
      type: Object,
    }
  },
  created: function () {
    this.movies = this.collection.movies.length !== 0 ? this.collection.movies : [0]
  }
}
</script>

<style>

</style>