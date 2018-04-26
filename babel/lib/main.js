"use strict";

a = function a(p) {
	return p * p;
};

b = new Promise(function (resolve, reject) {
	resolve(1);
});

b.then(function (data) {
	console.log(data);
});