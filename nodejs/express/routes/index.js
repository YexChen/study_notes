/*
*这里是主路由界面,分路由->主路由
*/
var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});



module.exports = router;
