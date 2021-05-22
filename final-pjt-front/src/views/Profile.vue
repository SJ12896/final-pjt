<template>
  <div><CollectionList :collections="collections" /></div>
</template>

<script>
import axios from 'axios'
import CollectionList from '@/components/Profile/CollectionList.vue'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Profile',
  components: {
    CollectionList,
  },
  data: function() {
    return {
      collections : [],
    }
  },
  created: function () {
      let user_id = window.location.href.split('/')[4];
      const config = this.$store.dispatch('setToken')
      axios.get(`${SERVER_URL}/movies/collection_list/${user_id}`, config)
      .then((res) => {
        this.collections = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
</script>

<style>

</style>