from firecrawl import FirecrawlApp
import os

app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

params = {'crawlerOptions':{'excludes':['blog/*']}}
crawl_result = app.crawl_url(
        'www.npwitys.com',
        params=params
    )

for result in crawl_result:
    print(result['markdown'])


