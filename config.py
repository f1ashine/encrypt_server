# [*]chrome 或 chromium exe文件路径
EXEPATH = "/Applications/Chromium.app/Contents/MacOS/Chromium"
# [*]需要浏览器打开的网页
URL = "http://xxxx/admin/index.jsp"
# [*]js代码举例, %s为请求内容
CODE = '''
encryptByDESModeCBC('%s')
'''
# [-]设置日志文件路径
LOGPATH = './sanic.log'
# [-]访问网页需要的COOKIE
# format: cookie:{'name':'JSESSIONID','value':'ASDADFDSFD25616'}
COOKIE = {}
