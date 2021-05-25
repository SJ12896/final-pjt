<template>
  <div>
      <div @click="selected(); selectMovie(movie);" :class="{ container : container, selected: isSelected }">
          <img :src="movieImage" alt="title">
        <div class="movieTitle">
          <div class="title">
           {{ movie.title }}
           </div>
           <div class="release_date">
           {{ movie.release_date }}
           </div>
           <div class="vote_average">
           {{ movie.vote_average }}
           <br>
           </div>
           {{ movie.overview }}
        </div>
      </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'MovieItem',
  props: {
    movie: Object,
  },
  data: function() {
    return {
      isSelected: false,
      container: true,
    }
  },
  methods: {
    ...mapActions([
      'selectMovie',
    ]),
    selected: function() {
      if (this.isSelected) {
        this.isSelected = false
      } else {
        this.isSelected = true
      }
    }
  },
  computed: {
    movieImage: function () {
      if (this.movie.poster_path) {
        return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
      }
      return false
      }
  },
  watch: {
    movie: function () {
      this.isSelected = false;
    }
  }
}
</script>

<style scoped>
.container {
  margin-top: 20px;
  padding: 20px;
  width : 500px; 
  height: 300px;
  word-break: break-all;
  border: 1px solid black;
}
img {
  float: left;
  border-radius: 7px;
  width : 200px; 
  height: 250px;
  margin-bottom: 10px;
}
.movieTitle {
  display: flex;
  flex-direction: column;
  justify-content: stretch;
  align-items: stretch;
  padding-left: 20px;
  font-size: 13px;
}
.title, .release_date, .vote_average {
  margin-bottom: 3px;
  font-weight: bold;
}
.selected {
  background-color: #4ca1a3;
  color : white;
}
</style>