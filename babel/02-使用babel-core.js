var babel = require("babel-core")

var result = babel.transform("d = p => p*p").code

console.log(result)
