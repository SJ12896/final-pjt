<template>
  <div class="container">
    <div>
      <h3>search</h3>
      <SearchBar @input-search="onInputSearch"/>
      <MovieList :movies="movies" />
    </div>
    <div>
      <h3>collection</h3>
        <div>
          <input type="text" v-model="title">
        </div>
        <div>
          <textarea v-model="info"></textarea>
        </div>
        <button>저장</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
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
      title: '',
      info: '',
      searchVal: '',
      movies: [],
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
},
}
</script>

<style scoped>
  .container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
</style>