<template>
  <div>
    <h1>Signup</h1>
      <label for=""></label>
      <input type="text" id="username" placeholder="아이디" v-model="credentials.username">
      <br>
      <label for=""></label>
      <input type="type" id="password" placeholder="비밀번호" v-model="credentials.password">
      <br>
      <label for=""></label>
      <input type="text" id="passwordConfirmation" placeholder="비밀번호 확인" v-model="credentials.passwordConfirmation"
      @keypress.enter="signup(credentials)">
      <br>
      <button @click="signup(credentials)">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
      }
    }
  },
  methods: {
    signup: function (credentials) {
      console.log(credentials)
      axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/user/`,
        data: this.credentials,
      })
      .then((res) => {
        console.log(res)
        this.$router.push({ name: 'Login' })
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