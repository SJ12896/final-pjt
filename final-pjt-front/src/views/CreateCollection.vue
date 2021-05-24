<template>
  <div class="container">
    <div>
      <h3>search</h3>
      <SearchBar @input-search="onInputSearch"/>
      <MovieList :movies="movies" />
    </div>
    <div>
      <h3>collection</h3>
        <div v-if="check === create">
          {{ selectedMovies }}
        </div>
        <div v-else>
          {{ updatedMovies }}
        </div>
        <div>
          <input type="text" v-model="data.title">
        </div>
        <div>
          <textarea v-model="data.info"></textarea>
        </div>
        <div v-if="check === create">
          <button @click="saveCollection(data); clear();">저장</button>
        </div>
        <div v-else>
          <button>저장</button>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState, mapActions } from 'vuex'
import SearchBar from '@/components/Collection/SearchBar'
import MovieList from '@/components/Collection/MovieList'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateCollection',
  components: {
    SearchBar,
    MovieList,
  },
  data: function () {
    return {
      inputValue: '',
      searchVal: '',
      movies: [],
      data: {
        title: '',
        info: '',
      },
      updatedMovies: [],
      collection_id: '',
      check: 'create',
    }
  },
  props: {
    collection : Object,
  },
  methods: {
   onInputSearch: function (inputText) {
      this.searchVal = inputText
      const token = localStorage.getItem('jwt')
      let form = new FormData()
      form.append('searchVal', this.searchVal)
      axios({
        method: 'post',
        url: `${SERVER_URL}/movies/search/`,
        data: form,
        headers: {
          Authorization: `JWT ${token}`
          }
        })
        .then((res) => {
          this.movies = res.data
        })
        .catch((err) => {
          console.log(err)
        })
      },
      ...mapActions([
        'saveCollection',
      ]),
      clear: function () {
        this.data.title = ''
        this.data.info = ''
      },
      // updateCollection: function () {
      // const token = localStorage.getItem('jwt')
      // let form = new FormData()
      // form.append('searchVal', this.searchVal)
      // axios({
      //   method: 'post',
      //   url: `${SERVER_URL}/movies/search/`,
      //   data: form,
      //   headers: {
      //     Authorization: `JWT ${token}`
      //     }
      //   })
      //   .then((res) => {
      //     this.movies = res.data
      //   })
      //   .catch((err) => {
      //     console.log(err)
      //   })
      // }
    },
  computed: {
    ...mapState([
      'selectedMovies',
    ])
  },
  created: function () {
    if (this.$route.path.includes('update')) {
      this.updatedMovies = this.$route.params['collection']['movies']
      this.data.title = this.$route.params['collection']['title']
      this.data.info = this.$route.params['collection']['info']
      this.collection_id = this.$route.params['collection']['id']
      this.check = 'update'
    }
  }
}
</script>

<style scoped>
  .container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
</style>