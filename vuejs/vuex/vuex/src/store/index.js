import Vue from 'vue'
import Vuex from 'vuex'

import * as actions from './actions'
import * as getters from './getters'
import * as types from './mutation-types'

Vue.use(Vuex)

const state = {
  count: 0,
  todolists: [
    {todo: '洗澡', done: false},
    {todo: '刷牙', done: false},
    {todo: '打游戏', done: true}
  ]
}

const mutations = {
  [types.INCREMENT] (state, {amount}) {
    state.count += amount
  },
  [types.DECREMENT] (state) {
    state.count--
  },
  [types.EVENTA] (state) {
    state.count++
  },
  [types.EVENTB] (state) {
    state.count++
  }
}

export default new Vuex.Store({
  state,
  actions,
  mutations,
  getters
})
