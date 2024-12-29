from firecrawl import FirecrawlApp
import os

app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

content = app.scrape_url("www.npwitys.com")

print(content)
