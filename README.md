# encrypt_server
### 0x01 说明
参考Burp插件[jsEncrypter](https://github.com/c0ny1/jsEncrypter)使用本地HTTP Server对payload进行加密。  

优点：不需要导入js文件，只需要事先在网页console端调试好加密代码即可

项目使用了如下框架：
- [Sanic](https://sanic.readthedocs.io/en/latest/)：一款高性能的Python异步Web框架
- [Pyppeteer](https://miyakogi.github.io/pyppeteer/)：基于谷歌官方puppeteer的python版本，可用于调用chrome API对网页进行各种操作

### 0x02 安装
#### 2.1 要求： python3.6+

```
pip install -r requirements.txt
```

#### 2.2 建议自行安装chromium，不要使用Pyppeteer下载chromium

`pyppeteer_test.py`用于调试Chromium能否正确执行js代码  
在Chromium执行js时可能会遇到  
`pyppeteer.errors.NetworkError: Protocol Error (Runtime.callFunctionOn): Session closed. Most likely the page has been closed.
`  
参考 https://github.com/miyakogi/pyppeteer/pull/160/files 修改源码解决  
其他问题可参考 https://blog.csdn.net/weixin_39198406/article/details/86719814

### 0x03 运行截图
![运行截图](https://github.com/f1ashine/encrypt_server/raw/master/screenshot.jpg)
