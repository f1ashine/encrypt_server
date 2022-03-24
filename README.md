# encrypt_server
### 0x01 说明
参考Burp插件[jsEncrypter](https://github.com/c0ny1/jsEncrypter)使用本地HTTP Server对payload进行加密。  
只需要参考config.py进行配置，然后参考运行截图即可。

优点：不需要导入js文件，只需要事先在网页console端调试好加密代码即可

项目使用了如下框架：
- [Sanic](https://sanic.readthedocs.io/en/latest/)：一款高性能的Python异步Web框架
- [Pyppeteer](https://miyakogi.github.io/pyppeteer/)：基于谷歌官方puppeteer的python版本，可用于调用chrome API对网页进行各种操作

### 0x02 安装
#### 2.1 要求： python3.6+

```
pip install -r requirements.txt
```
#### 2.2 遇到的问题
1. windows环境下安装sanic可能会遇到`error: Microsoft Visual C++ 14.0 is required`的问题，直接下载[Microsoft Visual C++ Build Tools 2015](http://go.microsoft.com/fwlink/?LinkId=691126)安装即可解决
2. `pyppeteer_test.py`用于调试Chromium能否正确执行js代码，在Chromium执行js时可能会遇到  
`pyppeteer.errors.NetworkError: Protocol Error (Runtime.callFunctionOn): Session closed. Most likely the page has been closed.`  
参考 https://github.com/miyakogi/pyppeteer/pull/160/files 修改源码解决  
3. 在从python传递字符串到js中，若python代码的字符串中含有`\n`等特殊字符，需要改写为`\\n`才行。
4. 在调试过程中，使用`console.log`无法输出变量，可直接调用`evaluate(param)`函数输出变量值。

其他问题可参考 https://blog.csdn.net/weixin_39198406/article/details/86719814

#### 2.3 tips
**pyppeteer**安装目录下有一个chromium_downloader.py，安装时如检测到未安装chromium，该脚本则会自启动下载chromium，并保存在`__pyppeteer_home__`下  
windows下的`__pyppeteer_home__`路径为`C:\Users\f1ashine\AppData\Local\pyppeteer\pyppeteer`，其他平台可自行寻找。  

mac安装chromium：https://storage.googleapis.com/chromium-browser-snapshots/Mac/575458/chrome-mac.zip  
linux安装chromium：https://storage.googleapis.com/chromium-browser-snapshots/Linux_x64/575458/chrome-linux.zip  
win64安装chromium：https://storage.googleapis.com/chromium-browser-snapshots/Win_x64/575458/chrome-win32.zip  
win32安装chromium：https://storage.googleapis.com/chromium-browser-snapshots/Win/575458/chrome-win32.zip


### 0x03 运行截图
![运行截图](https://github.com/f1ashine/encrypt_server/blob/master/screenshot.jpg)
