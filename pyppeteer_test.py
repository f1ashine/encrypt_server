import asyncio
from pyppeteer import launch

async def main():
    browser = await launch({'executablePath':'/Applications/Chromium.app/Contents/MacOS/Chromium', 'headless':'False'})
    page = await browser.newPage()
    await page.goto('http://xxxxx/admin/index.jsp')
    res = await page.evaluate('''() => {
        return {
            res: encryptByDESModeCBC('123')
        }
    }''')
    print(res)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
