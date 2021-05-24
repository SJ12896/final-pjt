<template>
  <li @click="goReviewDetail(review.id)">
    {{ review.title }}
    {{ username }}
  </li>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewListItem',
  props: {
    review: {
      type: [Array, Object],
    }
  },
  data: function (){
      return {
        username: null,
      }
  },
  methods: {
    setToken: function() {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    goReviewDetail: function (reviewId) {
      this.$router.push({ name: 'ReviewDetail', params: {reviewId: reviewId, username:this.username}})
    },
    getUsername: function() {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/accounts/${this.review.user}/detail/`, config)
        .then((res) => {
          console.log(res)
          this.username = res.data.username
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  mounted() {
    this.getUsername()
  }
}
</script>

<style>

</style>