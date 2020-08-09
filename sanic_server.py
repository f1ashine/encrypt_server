from sanic import Sanic
from sanic.response import text
from pyppeteer import launch
import config
import logging
import json

app = Sanic()

@app.route("/", methods=['POST', 'GET'])
async def test(request):
    if request.method == 'GET':
        return text("hello, access success!")
    else:
        payload = request.form['payload'][0]
        print(payload)
        # evalute 方法用于执行js，相当于浏览器的控制台，console.log()不能使用
        try:
            result = await app.page.evaluate(config.CODE % payload)
            app.logger.info("".join([payload, ":", result]))
            return text(result)
        except TypeError:
            if type(result) != str:
                return text("error! js code return value isn't string！")

@app.listener("before_server_start")
async def open_browser(app, loop):
    init_logger()
    await start_chrome(app)

async def start_chrome(app):
    """
    打开chromium，加载页面，若不设置executablePath，则默认自动下载chromium
    """
    if config.EXEPATH:
        browser = await launch({'executablePath': config.EXEPATH, 'headless':'False'})
    else:
        print("[!]Error! Browser's path isn't set")
    app.browser = browser
    page = await app.browser.newPage()
    if len(config.COOKIE) > 0:
        page.setCookie(config.COOKIE)
    app.page = page
    if len(config.URL) > 0:
        await page.goto(config.URL)
    else:
        print("[!]Error! Target url isn't set")
        

def init_logger():# 初始化日志记录logger
    logger = logging.getLogger('santic_server')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(config.LOGPATH, encoding='utf-8')
    handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(message)s"))
    logger.addHandler(handler)
    app.logger = logger

if __name__ == "__main__":
    try:
        app.run(host="127.0.0.1", port=8888)
    except InterruptedError:
        app.browser.close()
        app.stop()
