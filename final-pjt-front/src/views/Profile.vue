<template>
  <div></div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Profile',
  methods: {
    getUserCollections: function (user) {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/movies/collection_list/${user.id}/`, config)
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>