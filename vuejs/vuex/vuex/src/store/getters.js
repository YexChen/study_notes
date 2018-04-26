export const counter = state => state.count
export const todolists = state => state.todolists
export const donetodos = state => state.todolists.filter(todo => todo.done)
export const donetodosCount = (state, getters) => getters.donetodos.length
