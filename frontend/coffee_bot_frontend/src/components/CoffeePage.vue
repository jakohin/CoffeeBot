<template>
  <button class="coffee-circle circle" @click="orderCoffee">Get Coffee<div class="coffee"></div></button>
</template>

<script>
import axios from 'axios'

export default {
  name: "CoffeePage",
  methods: {
    getRoom: function () {
      return 5
    },
    orderCoffee: function () {
      axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
      axios
          .post(`http://127.0.0.1:8000/get_coffee/${this.getRoom()}`)
          .then((response) => {
            console.log(response)
          }, (error) => {
            console.log(error)
          })
    }
  }
}
</script>

<style scoped>
.coffee-circle {
  width: 200px;
  height: 200px;
  border: #C6AF71 solid 1px;
  color: whitesmoke;
  font-size: 50px;
  background-color: #ECD79E;
}
.coffee-circle:hover {
  color: white;
  background-color: #FFECB5;
  border-color: #C6AF71;
}

.circle {
  border-radius: 50%;
}
</style>