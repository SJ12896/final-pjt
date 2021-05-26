<template>
<div @click="goReviewDetail(review.id)">
    <h2 id="">{{ review.title }}</h2>
  <!-- title : {{ review.title }} -->
  username : {{ username }}
</div>
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
      console.log(reviewId)
      this.$router.push({ name: 'ReviewDetail', params: {reviewId: reviewId}})
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
#reviewBox {
  width:250px;
  height:200px;
  background-color: rgb(255, 255, 151);
  margin-left:8px;
  margin-top: 5px;
}
</style>