<template>
  <div>
    <h3><UserInfo :username="username"/>님의 profile</h3>
    팔로워 :{{ followers.length }}명
    팔로잉 :{{ followings.length }}명
    <div>
    <Follow :isFollow="isFollow" :isSamePerson="isSamePerson" @follow="follow" @unfollow="unfollow"/>
    </div>
    <hr>
    <h3>컬렉션 목록</h3>
    <div>
    <CollectionNew :isSamePerson="isSamePerson"/>
    </div>
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
import Follow from '@/components/Profile/Follow.vue'
import CollectionNew from '@/components/Profile/CollectionNew.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Profile',
  components: {
    CollectionList,
    UserInfo,
    UserReviewList,
    Follow,
    CollectionNew,
  },
  data: function() {
    return {
      collections : [],
      reviews: [],
      username: '',
      followers: [],
      followings: [],
      myName:'',
      isFollow: false,
      isSamePerson: false,
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
        this.followingCount = res.data.followingCount
        this.followerCount = res.data.followerCount
        if (this.followings.includes(user_id)) {
          this.isFollow = true
        }
        if (this.myName === this.username) {
          this.isSamePerson = true
        }
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
    methods: {
      follow: function() {
        const user_id = this.$route.params.user_id
        const token = localStorage.getItem('jwt')
        axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/${user_id}/detail/`,
        headers: {
          Authorization: `JWT ${token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.isFollow = true
        this.followers.push(this.myName)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    unfollow: function() {
      const user_id = this.$route.params.user_id
      const token = localStorage.getItem('jwt')
      axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/${user_id}/detail/`,
        headers: {
          Authorization: `JWT ${token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.isFollow = false
        let idx = this.followers.indexOf(this.myName)
        this.followers.splice(idx, 1)
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