const mongoose = require("mongoose")

mongoose.connect("mongodb://localhost:27017/Memo")

let db = mongoose.connection

db.on("error",function(err){
  throw new Error("an error happened!"+err)
})

db.once("open",function(){
  console.log("mongoose connected successfully")
})

module.exports = db
