<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Start</router-link>|
      <router-link to="/login">Login</router-link>|
      <router-link to="/signup">SignUp</router-link>|
      <router-link to="/main">Main</router-link>|
      <router-link to="/AddPrinter">AddPrinter</router-link>|
      <router-link to="/ListPrinter">ListPrinter</router-link>|
      <router-link to="/ListObject3ds">ListObject3ds</router-link>|
      <router-link to="/addstl">AddSTL</router-link>|
      <router-link to="/directmessage">DirectMessage</router-link>
    </div>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
