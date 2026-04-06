import json
import asyncio
import re
from urllib.parse import quote_plus
from playwright.async_api import async_playwright

SEARCH_QUERY = "Cyber Security Internship"
LOCATION = "India, IN"
TARGET_COUNT = 10

async def ai_extract_skills(description):

    return["penetration testing", "SOC"]

async def scrape_site(page, url, platform):
    job_list = []
    await page.goto(url)
    await page.wait_for_timeout(3000)

    if platform == "LinkdIn":
        selector = "ul.jobs-search__results-list li"
        promo_label = ".job-card-container__footer-item"
    else:
        selector = "[data-testid='slider-item']"
        promo_label = ".sponsoredGray"
    cards = await page.query_selector_all(selector)

    for card in cards:
        if len(job_list) >= TARGET_COUNT: break

        footer = await card.query_selector(promo_label)
        if footer and " Promoted" in await footer.inner_text():
            continue
        
        try:
            title_el = await card.query_selector("h3, h2")
            if not title_el:
                continue
            title = (await title_el.inner_text()) or ""

            link_el = await card.query_selector("a")
            if not link_el:
                continue
            link = await link_el.get_attribute("href")
            if not link:
                continue


            if platform == "LinkdIn":
                if link.startswith("/"):
                    link = "https://www.linkedin.com" + link
                elif not link.startswith("http"):
                    link = "https://www.linkedin.com/" + link.lstrip("/")
            else:
                if link.startswith("/"):
                    link = "https://www.indeed.com" + link
                elif not link.startswith("http"):
                    link = "https://www.indeed.com/" + link.lstrip("/")

                skills = await ai_extract_skills(title)

                job_list.append({
                    "source": platform,
                    "data":{
                        "job_title": title.strip(),
                        "job_url":link
                    },
                    "ai_summary": {"top_skills": skills}
                })
        except Exception:
                    continue
            
    return job_list

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        q_query = quote_plus(SEARCH_QUERY)
        q_location = quote_plus(LOCATION)

        li_url = f"https://www.linkedin.com/jobs/search/?keywords={q_query}&location={q_location}&f_TPR=r86400"
        ind_url = f"https://www.indeed.com/jobs?q={q_query}&l={q_location}&fromage=1"

        all_jobs = []
        all_jobs.extend(await scrape_site(page, li_url, "LinkdIn"))
        all_jobs.extend(await scrape_site(page, ind_url, "Indeed"))

        with open("job_listings.json", "w") as f:
            json.dump(all_jobs, f, indent=4)

        print(f"Successfully scraped {len(all_jobs)} organic jobs.")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())