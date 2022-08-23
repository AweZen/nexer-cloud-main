<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <PostViewer />
</template>

<script>
import PostViewer from './components/PostViewer.vue'

export default {
  name: 'App',
  components: {
    PostViewer
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
  margin-top: 60px;
}
</style>
