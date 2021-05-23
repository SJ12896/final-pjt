<template>
  <div>
    <div v-if="isSamePerson === true">
      <button @click="CreateNewCollection">
        새로운 컬렉션 생성하기
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CollectionNew',
  props: {
    isSamePerson: Boolean,
  },
  methods: {
    CreateNewCollection: function () {
      this.$router.push({ name: 'CreateCollection' })
    }
  }
}
</script>

<style>

</style>