<template>
  <div>
    <div>
    {{ movie.title }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieItem',
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>