<template>
  <div>
    {{ review.id }}
    {{ review.title }}
    {{ review.content }}
    {{ review.star_rating }}
    {{ review.created_at }}
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

<style scoped>
div {
  margin-top: 20px;
}
</style>