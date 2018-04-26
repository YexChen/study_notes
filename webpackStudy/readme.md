====
webpack学习
这里是最简单的打包代码,把app.js打包到了bundle.js中（app.js require了其他包）
./node_modules/.bin/webpack app.js dist/bundle.js

关于webpack.config.js:
	const path = require('path');

	   module.exports = {
	    entry: './app.js',
	    output: {
		path: path.join(__dirname, 'dist'),
		filename: 'bundle.js'
	    },
	    mode: 'production'
	}

这上面的代码定义了入口和出口文件，可以是多个文件，mode是webpack4的模式

接下来下载一下webpack-dev-server，当我们修改文件，保存的时候可以实现重新打包，并且重新刷新浏览器（热加载）

webpack-dev-server不会生成实际的文件,资源存在于内存中,当浏览器发出请求的时候先从内存加载,返回打包后的资源结果

###关于在webpack中使用样式
直接在app.js中require样式文件,报错说没有loader,我们需要在webpack.config.js中配置css-loader

module: {
    rules: [
        {
            test: /\.css$/,
            loader: 'css-loader'
        } 
      ]
  }
}

以上是webpack4的新写法,添加以后,只是成功加载了css,但是页面上面并没有效果
我们还需要安装一个style-loader,来展示页面
module: {
    rules: [
        {
            test: /\.css$/,
            loader: 'style-loader!css-loader'
        } 
      ]
  }
我们加入了style-loader,webpack解析方式是从右到左,先css-loader->style-loader


####资源打包
打包的主要目的是去掉生产环境中不需要的内容,如注释,换行,空格等


#####安装uglifyjs
yarn add uglifyjs-webpack-plugin 

const UglifyJSPlugin= require('uglifyjs-webpack-plugin')
plugins: [
    new UglifyJSPlugin()  
]

webpack支持require和import两种加载方式
webpack中output加入一个键publicPath,这是静态资源的路径
有点奇怪的是为什么要生成两份文件
output: {
    path: path.join(__dirname, 'dist'),
    publicPath: './dist/',
    filename: 'bundle.js'
  }
如果不设置publicPath,异步请求将会报错
import('./module.js').then(module => {
    module.log()
}).catch(err=> console.log("An error ocuured:"+err))

将app.js改成这样可以异步加载模块(import后面绝对不能有空格!)
当打包的时候,会生成一个0.bundle.js,bundle.js里面会加载0.bundle.js来实现异步
同理,当使用第二模块的时候会生成一个1.bundle.js,可以再network标签里面查看详情

####webpack的构建特性

#####tree-shaking
减少代码量的工具,检测工程中哪些代码未被引用并删除
遵循es6 Module的形式,会默认开启tree-shaking


####scope-hoisting
作用域提升,是webpack3提供的特性,可以拍平长的引用链.
const webpack = require("webpack")
new webpack.optimize.ModuleConcatenationPlugin()


####君玉皓老师的案例学习

#####入口引入polyfill
module.exports = {
    entry: ['babel-polyfill', './index.js'],
    output: {
        path: path.join(__dirname, 'dist'),
        filename: 'bundle.js'
    },
    devServer: {
        publicPath: "/dist/",
        port: 3000
    },
    mode: "development"
}
通过在入口引入polyfill,可以使代码转成es5

#####混合方式引入entry入口文件
module.exports = {
    entry: {
        'partA': './partA.js',
        'partB': './partB.js',
        'index': ['babel-polyfill', './index.js'],
    },
    output: {
        path: path.join(__dirname, 'dist'),
        filename: '[name].js'
    },
    devServer: {
        publicPath: "/dist/",
        port: 3000
    }
}

根据打印结果，是partA - partB - index 的顺序进行引入的
partA,partB,index.js中的文件如下:
document.write('index.js: ');
document.write(
    global._babelPolyfill
        ? 'added babel-polyfill'
        : 'no global babel-polyfill'
);
document.write('<br/>');
结果是只有index.js打印出了add babel-polyfill,说明webpack是顺序加载的

#####函数方式引入entry入口文件
const path = require('path');

module.exports = {
    entry: () => ({
        'partA': './partA.js',
        'partB': './partB.js',
        'index': ['babel-polyfill', './index.js'],
    }),
    output: {
        path: path.join(__dirname, 'dist'),
        filename: '[name].js'
    },
    devServer: {
        publicPath: "/dist/",
        port: 3000
    }
}

结果和上面一样

#####对象方式引入入口文件
const path = require('path');

module.exports = {
    entry: {
        app: './app.js',
        list: './components/list',
        detail: './components/detail'
    },
    output: {
        path: path.join(__dirname, 'dist'),
        filename: '[name].js'
    },
    devServer: {
        publicPath: "/dist/",
        port: 3000
    }
}

这里的list和detail是两个文件夹，会自动引入里面的index.js
我在list文件夹里面加了一个another.js，打包的时候不会自动加进去，需要在index.js里面引入（require/import）
感觉就像一个个模块一样

#####字符串引入
不做介绍

######输出带指纹的文件
const path = require('path');

module.exports = {
    entry: {
        'partA': './partA.js',
        'partB': './partB.js',
        'index': './index.js',
    },
    output: {
        path: path.join(__dirname, 'dist'),
        filename: '[name]-[chunkhash].js'
    },
    devServer: {
        publicPath: "/dist/",
        port: 3000
    },
    mode: "development"
}
在我们的output-filename中的chunkhash是指纹哈希值，会根据文本的内容进行哈希计算
详情：https://www.cnblogs.com/ihardcoder/p/5623411.html
避坑：https://github.com/kaola-fed/blog/issues/37
官方文档: https://doc.webpack-china.org/guides/caching/

如果不用插件的话是读不到hash值的,还要下一个html webpack plugin
  npm i --save-dev html-webpack-plugin
不过有bug - - 回头在解决吧


###loader

####babel
君玉皓的教程是webpack3的，我得改成webpack4的用法
下载babel:
npm install --save-dev babel-loader babel-core
进行babel的配置：
npm install babel-preset-env --save-dev
module: {
        rules:[
            {test: /\.js$/,exclude: /node_modules/,loader:"babel-loader"}    
        ]
    }

####css-loader
遵循webpack4的新写法：
module: {
        rules: [
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            }
        ]
    }

####eslint-loader
module: {
        rules: [
            {
                test: /\.js$/,
                enforce: 'pre',
                use: 'eslint-loader'
            }
        ]
    }
这里的enforce-pre是前置的意思
在webpack4中出bug了
