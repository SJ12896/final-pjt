<template>
  <div class="container">
    <div>
      <h3>search</h3>
      <SearchBar @input-search="onInputSearch"/>
      <MovieList :movies="movies" />
    </div>
    <div>
      <h3>collection</h3>
      {{ selectedMovies }}
        <div>
          <input type="text" v-model="data.title">
        </div>
        <div>
          <textarea v-model="data.info"></textarea>
        </div>
        <button @click="saveCollection(data); clear();">저장</button>
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
    }
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
    },
  computed: {
    ...mapState([
      'selectedMovies',
    ])
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