var express = require('express');
var router = express.Router();
var Users = require("../database/Users")
var Memos = require("../database/Memos")
var md5 = require("../utils/md5")

//======================================================>用户登录
router.post("/login",function(req,res){
  /*
  *@params: username 用户名
  *@params: password 密码
  */
  if(!req.body.username || !req.body.password)
    return res.json({
      status : 100,
      msg : "缺少必要参数:用户名或密码"
    })
  let params = {}
  params.username = req.body.username
  params.password = md5(req.body.password)

  Users.login(params,(err,doc)=>{
    if(err)
      return res.json({
        status : 500,
        err
      })
    else if(doc.length === 0)
      return res.json({
        status : 100,
        msg : "用户名或密码不存在"
      })
    else
      return res.json({
        status : 200,
        msg : "登陆成功"
      })
  })

})

//=====================================================>用户注册
router.post("/regist",function(req,res,next){
  /*
  *@params username
  *@params password
  */
  if(!req.body.username || !req.body.password)
    return res.json({
      status : 100,
      msg : "缺少必要参数:用户名或密码"
    })
  let params = {}
  params.username = req.body.username
  params.password = md5(req.body.password)
  let promise = new Promise((resolve,reject)=>{
    Memos.generateMemo((err,doc)=>{
      if(err){
        console.log("err:",err)
        reject(err)
      }
      else
        resolve(doc._id)
    })
  })

  promise.then((id)=>{
    params.memoId = String(id)
    console.log(params)
    Users.regist(params,(err,doc)=>{
      if(err)
        return res.json({
          status : 500,
          err
        })
      else
        return res.json({
          status : 200,
          doc
        })
    })
  }).catch((err)=>{
    return res.json({
      status : 500,
      msg : "memo create failed",
      err
    })
  })

})

//=====================================================> 是否登录


module.exports = router;
