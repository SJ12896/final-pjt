<template>
  <div class="container">
    <div class="search">
      <h3>search</h3>
      <SearchBar @input-search="onInputSearch"/>
      <MovieList :movies="movies" />
    </div>
    <div class="myCollection">
      <h3>collection</h3>
        <selectedMovieItem v-for="(movie, idx) in selectedMovies" :key="idx" :movie="movie" />
          <div>
            <input class="mt-3" type="text" placeholder="collection 제목" v-model="data.title" >
          </div>
          <div>
            <textarea v-model="data.info" class="mt-5" placeholder="collection 설명"></textarea>
          </div>
            <button @click="saveCollection(data); clear();" class="btn btn-outline-success mt-3">저장</button> 
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState, mapActions } from 'vuex'
import SearchBar from '@/components/Collection/SearchBar'
import MovieList from '@/components/Collection/MovieList'
import selectedMovieItem from '@/components/Collection/selectedMovieItem'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateCollection',
  components: {
    SearchBar,
    MovieList,
    selectedMovieItem,
  },
  data: function () {
    return {
      inputValue: '',
      searchVal: '',
      movies: [],
      data: {
        title: '',
        info: '',
        myId: '',
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
        this.$router.push('/accounts/'+`${this.myId}`+'/detail')
      },
    },
  computed: {
    ...mapState([
      'selectedMovies',
    ]),
  },
  created: function () {
    const myId = localStorage.getItem('myId')
    this.myId = myId
  }
}
</script>

<style scoped>
.container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin-top: 30px;
  }
.search {
  width: 500px;
}
.myCollection {
  width: 500px;
  display: block;
}
input, textarea {
  width: 350px;
  display: block;
  margin: 0 auto;
  border-bottom: teal 1.5px solid;
  border-left: medium none;
  border-right: medium none;
  border-top: medium none;
  outline: none;
}
textarea {
  height: 150px;
}
</style>