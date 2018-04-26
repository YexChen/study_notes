var childModule = {}

childModule.install = function(Vue,options){
  Vue.component("child",{
    render: function(h){
      return(
        <div level = {1}>
          <span>Hello</span> world
        </div>)
    }
  })
}
