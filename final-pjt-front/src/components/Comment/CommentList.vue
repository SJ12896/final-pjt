<template>
  <div>
    <CommentListItem v-for="(comment, idx) in this.review.comment_set" v-bind:key="idx" :idx="idx" :comment="comment" :review="review"/>
    <div>
      <label for="content">댓글 : </label>
      <input type="text" id="content" v-model.trim="comment.content" @keypress.enter="createComment">
      <button @click="createComment" >작성</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import _ from 'lodash'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
import CommentListItem from '@/components/Comment/CommentListItem'

export default {
  name: 'CommentList',
  components: {
    CommentListItem,
  },
  props: {
    review: {
      type: [Array, Object],
    }
  },
  data: function () {
    return {
      update: true,
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
      axios.post(`${SERVER_URL}/community/review/${this.review.id}/comment/`,commentItem, config)
      .then((res) => {
        console.log(res.data)
        newComments.push(res.data)
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