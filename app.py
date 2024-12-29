from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="YOUR_API_KEY")
crawl_result = app.crawl_url(
        'example.com',
        {'crawlerOptions': {'excludes': ['blog/*']}}
    )

for result in crawl_result:
    print(result['markdown'])


