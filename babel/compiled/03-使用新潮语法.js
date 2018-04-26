"use strict";

require("babel-polyfill");

var set = new Set([1, 1, 2, 2, 3, 3, 3, 4444444, 321313, 131]);

var pro = new Promise(function (resolve, reject) {
  resolve(1);
});

pro.then(function (data) {
  console.log(data);
});
