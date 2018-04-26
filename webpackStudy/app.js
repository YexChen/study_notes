import('./module.js').then(module => {
    module.log()
}).catch(err=> console.log("An error ocuured:"+err))

import('./module2.js').then(module=> {
    module.log()
}).catch(err=> console.log("An error ocuured:"+err))

import './index.css'
document.write("app.js loaded!")
moduleLog()
