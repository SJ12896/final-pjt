<template>
  <div v-if="title">
    {{ title }}
    <img :src="movieImage" :alt="title" style="{ width : 150px; height: 150px; }">
  </div>
  <div v-else>
    컬렉션에 저장된 영화가 없습니다.
  </div>
</template>

<script>
export default {
  name: 'CollectionMovieDetail',
  props: {
    title: [String, null],
    poster_path: [String, null]
  },
  computed: {
    movieImage: function () {
      if (this.poster_path) {
        return `https://image.tmdb.org/t/p/w500/${this.poster_path}`
      }
      return false
      }
  },
}
</script>

<style>

</style>