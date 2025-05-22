import asyncio
from pyppeteer import launch

async def auto_mint_opensea():
    browser = await launch(headless=False)
    page = await browser.newPage()

    # Open OpenSea login page
    await page.goto('https://opensea.io/login')

    # Automate wallet connection (MetaMask) - complex, may require extension support or manual step

    # Navigate to collection mint page
    await page.goto('https://opensea.io/collection/your-collection/mint')

    # Automate form filling and file upload
    await page.waitForSelector('input[type="file"]')
    await page.uploadFile('input[type="file"]', 'path_to_your_metadata.json')

    # Click mint button
    await page.click('button.mint-button')

    # Wait for confirmation
    await page.waitForSelector('.confirmation-message')

    print("Minting done!")

    await browser.close()

asyncio.get_event_loop().run_until_complete(auto_mint_opensea())
