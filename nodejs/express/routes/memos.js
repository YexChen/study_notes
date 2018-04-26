/*
*这里是memo路由界面,分路由->memo路由
*/
var express = require('express');
var router = express.Router();
var Memos = require('../database/Memos')

//===================================================>>查询文章
router.get('/query', function(req, res, next) {
  /*
  * @params userId
  */
  let params = req.query.dataId
  // console.log(req.params,req.body,req.query)
  Memos.queryMem(params,(err,doc)=>{
    if(err)
      return res.json({
        err
      })
    else if(!doc)
      return res.json({
        status : 502,
        msg : "文章未找到"
      })
    else
      return res.json({
        status : 200,
        doc
      })
  })
})

//========================================================>更新文章
router.post('/update',function(req,res,next){
  /*
  *@params dataId 备忘的ID
  *@params data 需要更新的数据
  */
  let params = req.body

  Memos.updateMemo(params,(err,doc)=>{
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

})

module.exports = router;
