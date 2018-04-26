import * as types from './mutation-types'

export const increment = ({commit}, amount) => setTimeout(function () { commit({type: types.INCREMENT, amount: amount }) }, 1000)

export const decrement = ({commit}) => commit(types.DECREMENT)

export const actionA = ({commit}) => {
  return new Promise((resolve, reject) => {
    setTimeout(function () {
      commit(types.EVENTA)
      console.log('a waiting resolve')
      resolve()
    }, 1000)
  })
}

export const actionB = ({commit, dispatch}) => {
  dispatch('actionA').then(() => {
    console.log('a is resolved,now b')
    commit(types.EVENTB)
  })
}
