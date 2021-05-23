<template>
  <div v-if="isSamePerson === false">
    <div v-if="isFollow === false">
      <button @click="follow">
        팔로우
      </button>
    </div>
    <div v-else>
      <button @click="unfollow">
        언팔로우
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Follow',
  props: {
    isFollow: Boolean,
    isSamePerson: Boolean,
  },
  methods: {
    follow: function() {
      this.$emit('follow')
    },
    unfollow: function() {
      this.$emit('unfollow')
    }
  }
}
</script>

<style>

</style>