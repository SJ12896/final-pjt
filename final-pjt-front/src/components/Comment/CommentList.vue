<template>
  <div>
    <ul>
      <li v-for="(comment, idx) in review.comment_set" v-bind:key="idx" :comment="comment">
        {{ comment.content }}
        <button @click="deleteComment(comment.id)">Delete</button>
      </li>
    </ul>
    <div>
      <label for="content">댓글 : </label>
      <input type="text" id="content" v-model.trim="comment.content" @keypress.enter="createComment">
      <button @click="createComment" >작성</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CommentList',

  props: {
    review: {
      type: [Array, Object],
    }
  },
  data: function () {
    return {
      comments: this.review.comment_set,
      comment: {
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
    createComment: function() {
      const config = this.setToken()
      const commentItem = {
        content: this.comment.content,
      }
      const newComments = this.review.comment_set
      // console.log(this.comment.content)
      axios.post(`${SERVER_URL}/community/review/${this.review.id}/comment`,commentItem, config)
      .then((res) => {
        console.log(res.data)
        newComments.push(res.data)
        })
        .catch((err) => {
         console.log(err)
         })
         this.comments = newComments
    },
    deleteComment: function (commentId) {
      const config = this.setToken()
      const newComments = this.review.comment_set
      // const commentId = commentId
      console.log(commentId)
      axios.delete(`${SERVER_URL}/community/comment/${commentId}/`,config)
      .then((res) => {
          console.log(res)
          // const targetCommentIdx = newComments.findIndex((comment) => {
          //   return comment.id === res.data.id
          // })
          console.log(commentId)
          newComments.splice(commentId,1)
          })
          .catch((err) => {
          console.log(err)
          })
         this.comments = newComments

    },
  },
}
</script>

<style>

</style>