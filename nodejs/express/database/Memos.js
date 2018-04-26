let mongoose = require("mongoose")
let Schema = mongoose.Schema

let memoSchema = new Schema({
  data : String
})

//注册方法
memoSchema.static("generateMemo",function(callback){
  this.create({data:''},callback)
})

//查询方法
memoSchema.static("queryMem",function(dataId,callback){
  this.findById(dataId,callback)
})

//更新方法
memoSchema.static("updateMemo",function(info,callback){
  this.update({_id : info.dataId},{$set : {data : info.data}},callback)
})

let Memos = mongoose.model('Memos',memoSchema)

module.exports = Memos
