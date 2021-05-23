<template>
  <div>
    <input @keyup="onInputKeyword" type="text">
  </div>
</template>

<script>

export default {
  name: 'SearchBar',
  data: function () {
    return {
    }
  },
  methods: {
    onInputKeyword: function (event) {
      this.$emit('input-search', event.target.value)
    }
  }
}
</script>

<style>
</style>