<template>
  <div>
    <h1>Login</h1>
     <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="text" id="password" v-model="credentials.password"
      @keypress.enter="login(credentials)">
    </div>
    <button @click="login(credentials)">로그인</button>
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
        url: `${SERVER_URL}/accounts/login/`,
        data: this.credentials,
      })
      .then((res) => {
        localStorage.setItem('jwt', res.data.token)
        this.$emit('login')
        this.$router.push({ name: 'Home' })
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