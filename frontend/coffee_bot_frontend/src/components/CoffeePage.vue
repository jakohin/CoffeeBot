<template>
  <button class="coffee-circle circle" v-bind:class="{animated: coffeeCircleAnimated}" @click="orderCoffee">Coffee's coming!</button>
</template>

<script>
import axios from 'axios'

export default {
  name: "CoffeePage",
  data: function () {
    return {
      coffeeCircleAnimated: false,
    }
  },
  methods: {
    getRoom: function () {
      return 5
    },
    orderCoffee: function () {
      this.coffeeCircleAnimated = true
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
/* Imports Font 'Raleway' from Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@200&display=swap');

@media only screen and (orientation: landscape) {
  .coffee-circle {
    min-width: 10rem;
    min-height: 10rem;
  }
}

:root {
  --coffee-darker: #B39C5B;
  --coffee-dark: #C6AF71;
  --coffee-mid: #D9C387;
  --coffee-light: #ECD79E;
  --coffee-lighter: #FFECB5;
}

.coffee-circle {
  width: 30vh;
  height: 30vh;
  border: #C6AF71 solid 2px;
  background-color: #B39C5B;
  position: relative;
  font-size: 2rem;
  color: white;
  overflow: hidden;
  font-family: 'Raleway', sans-serif;
}


.coffee-circle::after, .coffee-circle:before {
  content: "";
  height: 200%;
  width: 200%;
  position: absolute;
  bottom: -10%;
  left: -50%;
  background: white;
  border-radius: 45%;
}

.coffee-circle:before {
  background: #C6AF71;
  bottom: -35%;
  transform: rotate(45deg);
}


.coffee-circle.animated:after{
  animation: spin 5s ease-in-out forwards;
  animation-iteration-count: 1;
}

.coffee-circle.animated:before {
  animation: spin-less 5s ease-in-out forwards;
  animation-iteration-count: 1;
}


@keyframes spin {
  0% {
    transform: translateY(0) rotate(0deg);
  }
  100% {
    transform: translateY(-75%) rotate(500deg);
  }
}

@keyframes spin-less {
  0% {
    transform: translateY(0) rotate(45deg);
  }
  100% {
    transform: translateY(-75%) rotate(-345deg);
  }
}

.circle {
  border-radius: 50%;
}
</style>