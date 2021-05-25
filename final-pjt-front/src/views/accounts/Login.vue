<template>
  <div id="formBackGround">
      <div class="clearfix">
        <p class="loginbox text-light text-center ">
          Login
          <input class="px-1 mt-2" type="text" id="username" placeholder="ID" v-model="credentials.username">
          <input class="px-1" type="text" id="password" placeholder="Password" v-model="credentials.password"
        @keypress.enter="login">
        <button class="mt-2 p-0" type="submit" @click="login"><p class="mb-0 ">Login</p></button>
        </p>
      </div>
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
#formBackGround {
  margin: auto;
  height: 100vh;
  background-repeat:no-repeat;
  background-position: center;
  background-size: cover;
  background-image:linear-gradient( rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.5) ), url('../../assets/sky.jpg');
}
.clearfix {
  position: absolute;
  width: 250px;
  height: 150px;
  top: 50%;
  left: 50%;
  margin-left: -125px;
  margin-top: -75px;
  background: rgba(255,255,255,0.05);
  backdrop-filter: blur(10px);
  border-top: 1px solid rgba(255,255,255,0.1);
  border-left: 1px solid rgba(255,255,255,0.1);
  box-shadow: 5px 5px 30px rgba(0,0,0,0.2);
  border-radius: 3px;
}
.loginbox button {
  position: relative;
  color: white;
  width: 100%;
  border-radius: 8px;
  background: rgba(255,255,255,0.05);
  border-top: 1px solid rgba(255,255,255,0.1);
  border-left: 1px solid rgba(255,255,255,0.1);
  box-shadow: 5px 5px 30px rgba(0,0,0,0.2);
  font-size: 13px;
}
.loginbox {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}
.loginbox input {
  position: relative;
  border-radius: 8px;
  border: none;
  background: rgba(255,255,255,0.05);
  backdrop-filter: blur(10px);
  border-top: 1px;
  border-left: 1px;
  box-shadow: 5px 5px 30px rgba(0,0,0,0.2);
  color: rgb(255, 255, 255);
  transition: color 0.3s ease-out;
}
input::placeholder {
  color: rgba(255,255,255,0.6);
  font-size: 12px;
}
</style>