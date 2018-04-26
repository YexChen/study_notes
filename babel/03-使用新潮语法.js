require("babel-polyfill")

let set = new Set([1,1,2,2,3,3,3,4444444,321313,131])

let pro = new Promise((resolve,reject)=>{
  resolve(1)
})

pro.then((data)=>{
  console.log(data)
})
