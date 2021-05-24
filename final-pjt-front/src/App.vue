<template>
  <div id="app">
    <div id="nav">
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <div v-if="login">
            <a class="navbar-brand" href="/home/">Navbar</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
          </div>
          <div v-else>
            <a class="navbar-brand" href="/">Navbar</a>
          </div>
          <div v-if="login" class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" >영화1</a>
              </li>        
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" >영화2</a>
              </li>
            </ul>
          </div>
          <form v-if="login" class="d-flex">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
          <div class="nav-item dropdown">
            <span v-if="login">
              <a class="nav-link dropdown-toggle text-dark" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropdown
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" @click="logout">Logout</a></li>
                <li><a class="dropdown-item" ><router-link :to="{ path: '/accounts/'+`${myId}`+'/detail'}">Profile</router-link></a></li>
                <li><hr class="dropdown-divider"></li>
              </ul>
            </span>
            <span v-else>
              <span v-if="clickLogin" @click="clickSignUpLink">
              <router-link :to="{ name: 'Signup' }">Signup</router-link> |
              </span>
              <span v-else @click="clickLoginLink">
              <router-link :to="{ name: 'Login' }">Login</router-link>
              </span>
            </span>
          </div>
        </div>
      </nav>
    </div>
    <router-view @login="login = true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      clickLogin: false,
      login: false,
      username: '',
      myId: '',
    }
  },
  methods: {
    clickLoginLink: function(){
      this.clickLogin = true
      console.log(this.clickLogin)
    },
    clickSignUpLink: function(){
      this.clickLogin = false
    },
    logout: function () {
      console.log('logout 됨')
      this.login = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    const myId = localStorage.getItem('myId')
    if (token) {
      this.login = true
      this.myId = myId
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
