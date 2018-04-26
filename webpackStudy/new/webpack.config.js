const path = require("path")
const uglify = require("uglifyjs-webpack-plugin")

module.exports= {
  entry: "./app.js",
  output:{
    path: path.join(__dirname,"dist"),
    publicPath: "./dist/",
    filename: "compiled.js"
  },
  module:{
    rules: [
      {
          test: /\.css$/,
          loader: 'style-loader!css-loader'
      }
    ]
  },
  devServer:{
      port: 3000,
      publicPath: "/dist/"
  },
  plugins: [
    //new uglify()     
  ],
  mode: "development"
}
