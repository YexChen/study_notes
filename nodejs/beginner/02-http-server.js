let http = require("http")
// console.log(http)

let server = http.createServer(function(req,res){
  let bomb = Math.random() > 0.9? true: false
  console.log(bomb)
  if(bomb) throw new Error("瞬间爆炸!")
  res.end("hello world,nodejs")
})

server.listen(4100)
