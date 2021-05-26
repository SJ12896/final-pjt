<template>
  <li class="d-flex justify-content-center">
    <div v-if="update">
      {{ comment.content }}
      <div v-if=" requestUsername == comment.user">
      <button @click="deleteComment(comment,idx)">Delete</button>
      </div>
    </div>
    <div v-else >
      <input type="text" v-model.trim="comment.content">
    </div>
    <div v-if="update">
      <button @click="updateComment">Update</button>
    </div>
    <div v-else>
      <button @click="updateComplete(comment)">Update완료</button>
    </div>
  </li>
</template>

<script>
import axios from 'axios'
// import _ from 'lodash'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name:'CommentListItem',
  props: {
    comment: {
      type: [Array, Object],
    },
    idx: Number,
    review: {
      type: [Array, Object]
    }
  },
  data: function () {
    return {
      update: true,
      requestUsername: localStorage.getItem('id'),
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
    deleteComment: function (comment,idx) {
      const config = this.setToken()
      const newComments = this.review.comment_set
      const commentIdx = idx
      axios.delete(`${SERVER_URL}/community/comment/${comment.id}/`,config)
      .then((res) => {
          console.log(res)
          newComments.splice(commentIdx,1)
          })
          .catch((err) => {
          console.log(err)
          })
         this.comments = newComments

    },
    updateComment: function () {
      this.update = false
    },
    updateComplete: function (comment) {
      const config = this.setToken()
      const commentItem = {
        'content': this.comment.content,
      }
      axios.put(`${SERVER_URL}/community/comment/${comment.id}/`,commentItem, config)
      .then((res) => {
          console.log(res)
          this.update = true
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