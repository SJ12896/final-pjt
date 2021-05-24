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
        <div>
      <label for="star_rating">별점</label>
      <input type="number" id="star_rating" v-model="review.star_rating" min="0" max="5">
    </div>
    <button @click="createReview">제출</button>
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
        star_rating: '',
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
    createReview: function() {
      const config = this.setToken()
      const reviewItem = {
        title: this.review.title,
        content: this.review.content,
        star_rating: this.review.star_rating,
      }
      axios.post(`${SERVER_URL}/community/movie/${this.movieId}/`,reviewItem, config)
      .then((res) => {
        // console.log(res)  
        this.$router.push({ name  :'ReviewDetail', params:{ reviewId:res.data.id }})
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