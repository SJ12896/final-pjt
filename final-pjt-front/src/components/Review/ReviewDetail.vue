<template>
  <div>
    <h2>title : {{ review.title }}</h2>
    <p>content : {{ review.content }}</p>
    <p>username: {{ $route.params.username }}</p>
    <button @click="deleteReview">Delete</button>
    <button @click="updateReview">Update</button>
    <CommentList :review="review"/>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
import CommentList from '@/components/Comment/CommentList'

export default {
  name: 'ReviewDetail',
  components: {
    CommentList,
  },
  data: function () {
    return {
      reviewId: this.$route.params.reviewId,
      review: [],
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
    getReview: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/community/review/${this.reviewId}/`,config)
      .then((res) => {
          console.log(res.data)
          this.review = res.data
          })
          .catch((err) => {
          console.log(err)
          })
    },
    deleteReview: function () {
      const config = this.setToken()
      axios.delete(`${SERVER_URL}/community/review/${this.reviewId}/`,config)
      .then((res) => {
          console.log(res)
          this.$router.push({ name: 'MovieDetail', params:{ movieId:this.review.movie}})
          })
          .catch((err) => {
          console.log(err)
          })
    },
    updateReview: function () {
      const reviewItem = {
        'id': this.review.id,
        'title': this.review.title,
        'content': this.review.content,
      }
      this.$router.push({ name: 'UpdateReview', params:{ movieId:this.review.movie , reviewItem:reviewItem}})
    }
  },
  mounted() {
    this.getReview()
  }
}
</script>

<style>

</style>