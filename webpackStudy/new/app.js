import log from "./module.js"
import './index.css'
import('./async.js').then(module=>{
    module.log()
}).catch(err=>{throw new Error("An error happend!:"+err)})
document.write("app was loaded!")
log()
