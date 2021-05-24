<template>
  <div>
    <div>
      <span @click="selectMovie(movie)">
        {{ movie.title }}
      </span>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'MovieItem',
  props: {
    movie: Object,
  },
  methods: {
    ...mapActions([
      'selectMovie',
    ])
  }
}
</script>

<style>

</style>