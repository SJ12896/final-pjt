<template>
  <div>
    <!-- {{ comments }}  -->
    <ul>
      <li v-for="(comment) in comments" v-bind:key="comment">
        {{ comment.content }}
      </li>
    </ul>
    <div>
      <label for="content">댓글 : </label>
      <input type="text" id="content" v-model.trim="comment.content">
      <button @click="createComment">작성</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CommentList',
  data: function () {
    return {
      comments: this.review.comment_set,
      comment: {
        content: '',
      }
    }
  },
  props: {
    review: Array,
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
    createComment: function() {
      const config = this.setToken()
      const commentItem = {
        content: this.comment.content,
      }
      axios.post(`${SERVER_URL}/community/review/${this.review.id}/comment`,commentItem, config)
      .then((res) => {
        console.log(res)
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