# google-scholar-scraper
## What is this?
- Google Scholarの検索結果をCSVファイルに保存するためのツールです。本ツールはSerpApiを利用しているため、使用にはSerpApiのAPIキーが必要です。
## Getting Started
1. `scrape.py`と同じ階層に、APIキーを以下のフォーマットで記載した`.env`ファイルを保存してください。
    - ```bash
      SERPAPI_KEY="******"
      ```
2. 必要なライブラリをインストールしてください。
    - `pip install pandas google-search-results python-dotenv`
3. `scrape.py`を実行してください。
    - `python scrape.py`
4. 検索クエリ、cites_id（特定の論文を引用している論文を検索したい場合）、検索対象期間の開始年、終了年を入力してください。指定しない場合は、Enterキーのみを押してください。
5. 結果が保存された旨のメッセージが画面上に表示されたら、`outputs`フォルダにCSVファイルが保存されます。