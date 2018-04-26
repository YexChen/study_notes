var elementNumbers = {}

elementNumbers.install = function(Vue,options){
  Vue.component("elNumbers",{
    render: function(h){
      return(
        <div class = {this.size}>
          <button onClick={this.minus}>-</button>
          <input on-input= {(e)=> this.sync("cValue",parseInt(e.target.value))} value={this.cValue} />
          <button onClick={this.add}>+</button>
        </div>)
    },
    props: {
      value: {type: Number,default: 0},
      min: {type:Number,default: Infinity * -1},
      max: {Number,default: Infinity},
      step: {type: Number,default: 1},
      size: {String,default: "large"},
      disabled: {type: Boolean, default: false}
    },
    data: function(){
      return{
        cValue: this.value,
        cDisabled: this.passDisabled
      }
    },
    watch: {
      cValue: function(newVal,oldVal){
        if(newVal < this.min) this.cValue = this.min
        else if(newVal > this.max) this.cValue = this.max
      }
    },
    methods: {
      add: function(){
        this.cValue+= this.step
      },
      minus: function(){
        this.cValue-= this.step
      },
      sync: function(prop,value){
        console.log("sync")
        this[prop]= value
      }
    }
  })
}
