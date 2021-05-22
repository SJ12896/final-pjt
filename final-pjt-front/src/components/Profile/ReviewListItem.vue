<template>
  <div>
    {{ review.id }}
    {{ review.title }}
  </div>
</template>

<script>

export default {
  name: 'ReviewListItem',
  props: {
    review: Object,
  }
}
</script>

<style>

</style>