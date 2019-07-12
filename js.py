一些学习　javascript 的笔记

１．　安装２个插件　Prettier，　Live Server
２．　VSCode, 一个感叹号然后快速新建文件模板
３．　// a lot of strings and add a param
console.log(`something happens  aaaa  ${name}`)


npm　创建项目的顺序:

1. npm init -y                       初始化一个nodejs项目
2. npm install express  　　          安装一个包  -g  全局安装
3. npm install --save-dev nodemon　   重启服务器
4. delete 'package.json' line 7, add:
"start": "nodemon index.js"
5. npm start                          run app
6. go to localhost:3000



Electron的安装  报错了, 需要再看看...
0. npm init -y                              初始化一个nodejs项目
1.  sudo npm install -g cnpm --registry=https://registry.npm.taobao.org
把npm的仓库切换到国内taobao仓库
2. sudo cnpm install -g electron            全局安装这个包
3. sudo cnpm install -g electron-packager   安装打包工具
4. delete 'package.json' line 7, add:
"start": "electron ."
5. add main.js index.html


javascript 方法:
1. toUpperCase()
2. typeof <variable>
3. 22 == '22'   ----> true , please use ===
4. && ---> and,  || ---> or
5. array, pop(), push(), unshift(), shift(), indexOf()
6. [this] , default to window object, but you can define it
7.
