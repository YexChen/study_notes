a = p => p*p

b = new Promise((resolve,reject)=>{
	resolve(1)
})

b.then((data)=>{
	console.log(data)
})
