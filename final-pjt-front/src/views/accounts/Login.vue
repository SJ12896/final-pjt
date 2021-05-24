<template>
  <div>
    <h1>Login</h1>
      <label for=""></label>
      <input type="text" id="username" placeholder="ID" v-model="credentials.username">
      <br>
      <label for=""></label>
      <input type="text" id="password" placeholder="password" v-model="credentials.password"
      @keypress.enter="login">
      <br>
      <button type="submit" @click="login">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/api-token-auth/`,
        data: this.credentials,
      })
      .then((res) => {
        localStorage.setItem('jwt', res.data.token)
        const myname = this.credentials.username
        localStorage.setItem('myname', myname)
        this.$emit('login')
        this.$router.push({ name: 'Home' })
        return axios.get(`${SERVER_URL}/accounts/id/${this.credentials.username}/`)
      .then((res) => {
        localStorage.setItem('myId', res.data.id)
      })
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