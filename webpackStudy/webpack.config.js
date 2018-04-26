const path = require('path')
const UglifyJSPlugin= require('uglifyjs-webpack-plugin')
const webpack= require('webpack')

module.exports = {
  entry: './app.js',
  output: {
    path: path.join(__dirname, 'dist'),
    publicPath: './dist/',
    filename: 'bundle.js'
  },
  module: {
    rules: [
        {
            test: /\.css$/,
            loader: 'style-loader!css-loader'
        } 
      ]
  },
  devServer: {
    port: 3000,
    publicPath: "/dist/"
  },
  plugins: [
    new UglifyJSPlugin(),  
    new webpack.optimize.ModuleConcatenationPlugin()
  ],
  mode: "production"
}
