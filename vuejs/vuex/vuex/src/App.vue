<template>
  <div id="app">
    <div class="hello">
      <div id="app">
        {{count}}
        {{summary}}
        <button @click = "plus(10)">+</button>
        <button @click = "minus">-</button>
        <button type="button" name="button" @click = "actionB">?</button>
        <!-- <h1>所有事项</h1>
        <p v-for = "todo in todolists">{{todo.todo}}</p>
        <h1>已完成事项
          ({{donetodosCount}})
        </h1>
        <p v-for = "todo in donetodos">{{todo.todo}}</p> -->
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import {mapGetters} from 'vuex'
import {mapActions} from 'vuex'
export default {
  name: 'App',
  data(){
    return {
      localCounter : 10
    }
  },
  methods : {
    ...mapActions({
      plus : 'increment',
      minus : 'decrement'
    }),
    ...mapActions([
      'actionA',
      'actionB'
    ])
    // plus(){
    //   this.$store.dispatch("increment",10)
    // },
    // minus(){
    //   this.$store.dispatch("decrement")
    // }
  },
  computed : mapState({
    count : 'count',
    summary(state){
      return state.count + this.localCounter
    }
  })
    // ...mapGetters([
    //   'todolists',
    //   'donetodos',
    //   'donetodosCount'
    // ]),

  // }
  // {
  //   todolists(){
  //     return this.$store.getters.todolists
  //   },
  //   donetodos(){
  //     return this.$store.getters.donetodos
  //   }
  // }



}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
