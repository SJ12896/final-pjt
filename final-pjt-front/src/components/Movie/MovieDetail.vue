<template>
<div id="movieDetailBox">
  <div class="card">
    <!-- {{ movieDetail }} -->
    <div class="card_left">
        <img class="" :src="movieImage" alt="movie_image"> 
    </div>
    <div id="contentBox" class="card_right">
      <h1>{{ movieDetail.title }}</h1>
      <div class="card_right_details">
        <ul id="card_right_details_ul">
          <li>개봉일 : {{ movieDetail.release_date }}</li>
          <li>장르 : </li>
        </ul>
        <div id="card_right_rating">
          <div class="card_right_rating_stars">
            <fieldset id="ration" class='rating'>
              <input id='star10' name='rating' type='radio' value='10'>
              <label class='full' for='star10' title='10 stars'></label>
              <input id='star9half' name='rating' type='radio' value='9 and a half'>
              <label class='half' for='star9half' title='9.5 stars'></label>
           </fieldset>
          </div>
        </div>
        <div id="card_right_overview">
          <p>{{ movieDetail.overview}}</p>
        </div>
      </div>
    </div>
  </div>
  <div>
    <MovieReviews :movieId="movieId"/>
    <button @click="goCreateReview" >리뷰쓰기</button>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import {mapState} from 'vuex'
import MovieReviews from '@/components/Movie/MovieReviews'

// const api = axios.create({
//   baseUrl:'https://api.themoviedb.org/3/movie/',
//   params: { 
//     apikey: "3dbbe66dede6e1bfdc61c7773b51e2ee",
//     language: "ko-KR"
//   }
// })

export default {
  name: 'MovieDetail',
  components: {
    MovieReviews,
  },
  data: function () {
    return {
      movieId: this.$route.params.movieId,
    }
  },
   methods: {
    goCreateReview: function() {
      this.$router.push({ name: 'CreateReview'})
    },
    getMovieImages: function() {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.movieId}/images`,
        params: {
          api_key: "3dbbe66dede6e1bfdc61c7773b51e2ee",
          language: "ko-KR",
        }
      })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  computed: {
    movieImage: function () {
      return `https://image.tmdb.org/t/p/w500/${this.movieDetail.poster_path}`
    },
    ...mapState([
      'movieDetail',
    ])
  },
  mounted() {
    this.getMovieImages()
  }
}
</script>

<style>
@import url(https://fonts.googleapis.com/css?family=Montserrat:400,700);
@import url(//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css);

/* #movieDetailBox {
  background: #e2e2e2;
  width: 98%;
  height: 100vh;
  margin-top: 60px;
} */
.card {
  width: 800px;
  height: 450px;
  background: transparent;
  position: absolute;
  display: inline-block;
  left: 0;
  right: 0;
  margin: auto;
  top: 0;
  bottom: 0;
  border-radius: 10px;
  -webkit-border-radius: 10px;
  -moz-border-radius: 10px;
  box-shadow: 0px 20px 30px 3px rgba(0, 0, 0, 0.55);
}
.card_left {
  width: 40%;
  height: 450px;
  float: left;
  overflow: hidden;
  background: transparent;
}
.card_left img {
  width: 100%;
  height: auto;
  border-radius: 10px 0 0 10px;
  -webkit-border-radius: 10px 0 0 10px;
  -moz-border-radius: 10px 0 0 10px;
  position: relative;
}

.card_right {
  width: 60%;
  float: left;
  background: #000000;
  height: 450px;
  border-radius: 0 10px 10px 0;
  -webkit-border-radius: 0 10px 10px 0;
  -moz-border-radius: 0 10px 10px 0;
}
.card_right h1 {
  color: white;
  font-family: "Montserrat", sans-serif;
  font-weight: 400;
  text-align: left;
  font-size: 40px;
  margin: 40px 0 40px 0;
  padding: 0 0 0 0;
  text-align: center;
  letter-spacing: 1px;
}

.card_right_details ul {
  list-style-type: none;
  padding: 0 0 0 40px;
  margin: 10px 0 0 0;
}

#card_right_details_ul li {
  /* display: inline; */
  color: #e3e3e3;
      /* font-family: "Montserrat", sans-serif; */
  font-weight: 400;
  font-size: 14px;
  margin: 0 0 10px 0;
  padding: 0 40px 0 0;
}

/* .card_right_rating_stars{
  position: relative;
  right: 160px;
  margin: 10px 0 10px 0;
} */

/* .card_right_rating_stars label{
  margin: 0;
  padding: 0;
}

.card_right_rating_stars fieldset{
  margin: 0;
  padding: 0;
}

#card_right_rating {
  border: none;
}

#card_right_rating > input {
  display: none;
}
#card_right_rating > label:before {
  margin: 5px;
  font-size: 1.25em;
  display: inline-block;
  content: "\f005";
  font-family: FontAwesome;
}

#card_right_rating > .half:before {
  content: "\f089";
  position: absolute;
}

#card_right_rating > label {
  color: #ddd;
  float: right;
}


#card_right_rating > input:checked ~ label,
#card_right_rating:not(:checked) > label:hover, 
#card_right_rating:not(:checked) > label:hover ~ label {
            color: #ffd700;
          }

#card_right_rating > input:checked + label:hover, 
#card_right_rating > input:checked ~ label:hover,
#card_right_rating > label:hover ~ input:checked ~ label
#card_right_rating > input:checked ~ label:hover ~ label {
            color: #ffed85;
          } */

#card_right_overview p{
  color: white;
  font-family: "Montserrat", sans-serif;
  font-size: 15px;
  padding: 0 40px 0 40px;
  letter-spacing: 1px;
  margin: 40px 0 10px 0;
  line-height: 20px;
}

/* #card_right_overview a {
  text-decoration: none;
  font-family: "Montserrat", sans-serif;
  font-size: 14px;
  padding: 0 0 0 40px;
  color: #ffda00;
  margin: 0;
} */

      /* &_button {
        a {
          color: #ffda00;
          text-decoration: none;
          font-family: "Montserrat", sans-serif;
          border: 2px solid #ffda00;
          padding: 10px 10px 10px 40px;
          font-size: 12px;
          background: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/343086/COMdoWZ.png);
          background-size: 12px 12px;
          background-repeat: no-repeat;
          background-position: 7% 50%;
          border-radius: 5px;
          -webkit-transition-property: all;
          transition-property: all;
          -webkit-transition-duration: 0.5s;
          transition-duration: 0.5s;
        }
        a:hover {
          color: #000000;
          background-color: #ffda00;
          background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/343086/rFQ5dHA.png);
          background-size: 12px 12px;
          background-repeat: no-repeat;
          background-position: 10% 50%;
          cursor: pointer;
          -webkit-transition-property: all;
          transition-property: all;
          -webkit-transition-duration: 0.5s;
          transition-duration: 0.5s;
        }
        padding: 0 0 0 40px;
        margin: 30px 0 0 0;
      } */


/* #contentBox {
  width: 450px;
  padding: 20px;
}

#contentBox div {
  width: 100%;
}

#movieDetailBox {
  margin-top: 55px;
  width: 100%;
  margin-left: 0px;
  margin-right: 0px;
}

#imageContainer {
  width: 100%;
  height: 300px;
  background-color: black;
} */

</style>