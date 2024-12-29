import datetime
import pytz
from firecrawl import FirecrawlApp
import os

# 日本時間の設定
JST = pytz.timezone('Asia/Tokyo')

# 出力ファイル名（タイムスタンプ付きで重複防止）
output_filename = f"crawl_results_{datetime.datetime.now(JST).strftime('%Y-%m-%d-%H-%M-%S')}.txt"

# Firecrawlの初期化とクロール実行
app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
params = {'crawlerOptions':{'excludes':['blog/*']}}
crawl_result = app.crawl_url('www.npwitys.com', params=params)

# 結果をテキストファイルに出力
with open(output_filename, 'w', encoding='utf-8') as f:
    for result in crawl_result:
        f.write(result['markdown'] + '\n')

print(f"クロール結果を {output_filename} に出力しました。")
