import asyncio
import os
from pyppeteer import launch

PYPPETEER_CHROMIUM_REVISION = '1181217'
os.environ['PYPPETEER_CHROMIUM_REVISION'] = PYPPETEER_CHROMIUM_REVISION

async def scrape_indeed():

    browser = await launch(headless=False)
    page = await browser.newPage()

    await page.goto('https://www.indeed.com')
    await page.waitForSelector('#text-input-what')
    await page.waitForSelector('#text-input-where')

    await page.type('#text-input-what', 'Software Engineer')
    await page.type('#text-input-where', '')

    await page.click('button[type="submit"]')

    await page.waitForNavigation()

    job_listings = await page.querySelectorAll('.resultContent')
    for job in job_listings:
        # extracts job title
        title_element = await job.querySelector('h2.jobTitle span[title]')
        title = await page.evaluate('(element) => element.textContent', title_element)

        # extracts company name
        company_element = await job.querySelector('div.company_location [data-testid="company-name"]')
        company = await page.evaluate('(element) => element.textContent', company_element)

        # extracts location
        location_element = await job.querySelector('div.company_location [data-testid="text-location"]')
        location = await page.evaluate('(element) => element.textContent', location_element)

        print({'title' : title, 'company' : company, 'location' : location})
    
    await browser.close()

asyncio.get_event_loop().run_until_complete(scrape_indeed())