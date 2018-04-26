let mongoose = require("mongoose")
let Schema = mongoose.Schema

let userSchema = new Schema({
  username : String,
  password : String,
  memo : String
})

//注册方法
userSchema.static("regist",function(userinfo,callback){
  this.create({username: userinfo.username,password: userinfo.password,memo: userinfo.memoId},callback)
})

//登录方法
userSchema.static("login",function(userinfo,callback){
  this.find({username: userinfo.username,password: userinfo.password},callback)
})

let Users = mongoose.model('Users',userSchema)

module.exports = Users
