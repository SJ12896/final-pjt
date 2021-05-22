<template>
  <div>
    <div>
      <label for="title">제목</label>
      <input type="text" id="title" v-model.trim="review.title" >
    </div>
    <div>
      <label for="content">내용</label>
      <textarea type="text" id="content" v-model.trim="review.content" ></textarea>
    </div>
    <button @click="createRevie">제출</button>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name:'CreateReview',
  data: function () {
    return {
      review: {
        title: '',
        content: '',
      }
    }
  },
  methods: {
    setToken: function( ) {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    createReview: function(review) {
      const config = this.setToken()
      const reviewItem = {
        title: this.review.title,
        content: this.review.content,
      }
      axios.post(`${SERVER_URL}/community/review/${review.id}/`,reviewItem, config)
      .then((res) => {
        console.log(res)
        this.$router.push({ name:'ReviewDetail' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}
</script>

<style>

</style>