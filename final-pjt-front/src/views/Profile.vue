<template>
  <div>
    <h3><UserInfo :username="username"/>님의 profile</h3>
    팔로워 :{{ followers.length }}명
    팔로잉 :{{ followings.length }}명
    <button>팔로우</button> 
    <hr>
    <h3>컬렉션 목록</h3>
    <CollectionList :collections="collections" />
    <hr>
    <h3>리뷰 목록</h3>
    <UserReviewList :reviews="reviews"/>
    </div>
</template>

<script>
import axios from 'axios'
import CollectionList from '@/components/Profile/CollectionList.vue'
import UserInfo from '@/components/Profile/UserInfo.vue'
import UserReviewList from '@/components/Profile/UserReviewList.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Profile',
  components: {
    CollectionList,
    UserInfo,
    UserReviewList,
  },
  data: function() {
    return {
      collections : [],
      reviews: [],
      username: '',
      followers: [],
      followings: [],
      myName:'',
    }
  },
  created: function () {
      const user_id = this.$route.params.user_id
      const token = localStorage.getItem('jwt')
      this.myName = localStorage.getItem('myname')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }

      axios.get(`${SERVER_URL}/movies/collection_list/${user_id}/`)
      .then((res) => {
        this.collections = res.data
      })
      .catch((err) => {
        console.log(err)
      })
      
      axios.get(`${SERVER_URL}/accounts/${user_id}/detail/`, config)
      .then((res) => {
        this.username = res.data.username
        this.followers = res.data.followers
        this.followings = res.data.followings
      })
      .catch((err) => {
        console.log(err)
      })

      axios.get(`${SERVER_URL}/community/${user_id}/reviews/`, config)
      .then((res) => {
        this.reviews = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
</script>

<style>

</style>