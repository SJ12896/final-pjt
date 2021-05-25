<template>
  <div id="app">
    <div id="nav">
      <nav class="navbar navbar-expand-lg bg-transparent">
        <div class="container-fluid ms-3">
          <div v-if="login">
            <a class="navbar-brand text-decoration-none" href="/home/">Home</a>
          </div>
          <div v-else>
            <a class="navbar-brand text-decoration-none" href="/">Home</a>
          </div>

        <Dropdown
            :options="allMovie"
            v-on:selected="validateSelection"
            :disabled="false"
            placeholder="찾고싶은 영화를 검색해보세요"
            >
        </Dropdown>

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
              <router-link :to="{ name: 'Signup' }" class="text-decoration-none text-light">Signup</router-link> |
              </span>
              <span v-else @click="clickLoginLink">
              <router-link :to="{ name: 'Login' }" class="text-decoration-none text-light me-3">Login</router-link>
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
import Dropdown from 'vue-simple-search-dropdown';
import{ mapActions, mapState } from 'vuex'

export default {
  name: 'App',
  data: function () {
    return {
      clickLogin: false,
      login: false,
      username: '',
      myId: '',
      searchVal: '',
      allMovie: [],
      selected: { name: null, id: null },
    }
  },
  components: {
    Dropdown,
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
    },
      ...mapActions({
      init: 'getMovies'
    }),
     validateSelection(selection) {
        this.selected = selection;
        console.log(selection.id)
        if (selection.id !== undefined) {
          this.$router.push({ name: 'MovieDetail', params: { movieId: selection.id}})
        }
      },
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    const myId = localStorage.getItem('myId')
    if (token) {
      this.login = true
      this.myId = myId
    }
  },
    computed:{
    ...mapState({
      movies: 'movies',
    })
  },
    mounted() {
    this.init()
    },
    watch: {
      movies (newMovies) {
        this.allMovie = [];
        for (let i = 0; this.movies.length > i; i++){
          this.allMovie.push({id: newMovies[i].id, name: newMovies[i].title}
            )
          }
      }
    }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans&display=swap');

#app {
  font-family: 'Noto Sans', sans-serif;
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
