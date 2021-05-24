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
    <button @click="updateReview">제출</button>
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
        id: this.$route.params.reviewItem.id,
        title: this.$route.params.reviewItem.title,
        content: this.$route.params.reviewItem.content,
      },
      movieId: this.$route.params.movieId,
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
    updateReview: function () {
      const config = this.setToken()
      const reviewItem = {
        'title': this.review.title,
        'content': this.review.content,
      }
      axios.put(`${SERVER_URL}/community/review/${this.review.id}/`,reviewItem, config)
      .then((res) => {
          console.log(res)
          this.$router.push({ name  :'ReviewDetail', params:{ reviewId:res.data.id , username: localStorage.getItem('myname') }})
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