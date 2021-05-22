import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '@/views/accounts/Login'
import Signup from '@/views/accounts/Signup'
import Home from '@/views/Home'
import Profile from '@/views/Profile'
import MovieDetail from '@/components/Movie/MovieDetail'
import ReviewDetail from '@/components/Review/ReviewDetail'
import CreateReview from '@/components/Review/CreateReview'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/accounts/login/',
    name: 'Login',
    component: Login,
  },
  {
    path: '/accounts/signup/',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/:username/detail/',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/movies/:movieId/detail/',
    name: 'MovieDetail',
    component: MovieDetail,
  },
  {
    path: '/review/:reviewId/detail/',
    name: 'ReviewDetail',
    component: ReviewDetail,
  },
  {
    path: 'community/review/:reviewId/create/',
    name: 'CreateReview',
    component: CreateReview,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
