# google-scholar-scraper
## What is this?
- Google Scholarの検索結果をCSVファイルに保存するためのツールです。本ツールは[SerpApi](https://serpapi.com/google-scholar-api)を利用しているため、使用にはSerpApiのAPIキーが必要です。
## Getting Started
1. `scrape.py`と同じ階層に、APIキーを以下のフォーマットで記載した`.env`ファイルを保存してください。
    - ```bash
      SERPAPI_KEY="******"
      ```
2. 必要なライブラリをインストールしてください。
    - `pip install pandas google-search-results python-dotenv`
3. `scrape.py`を実行してください。20件ごとに取得を続けるかを選びたい場合は、`-i`オプションを付けて実行してください。
    - `python scrape.py` or `python scrape.py -i`
4. 検索クエリ、cites_id（特定の論文を引用している論文を検索したい場合）、検索対象期間の開始年、終了年を入力してください。指定しない場合は、Enterキーのみを押してください。以下は入力例です。
    - ```bash
      Type the query (optional if you want to specify "cites_id"):
      entity "linking" -quality author:a source:"ACL" OR source:"IEEE"
      Type the cites_id to trigger Cited By searches (optional):
      10656872565717657704
      Type the year from which you want the results to be included (optional):
      2010
      Type the year until which you want the results to be included (optional):
      2020
      Waiting for article results to save..
      ```
5. 結果が保存された旨のメッセージが画面上に表示されたら、`outputs`フォルダにCSVファイルが保存されます。以下は出力されるCSVファイルの例です。
    - ```csv
      page_number,position,title,url,year,publication_info,snippet,pdf_url,cited_num,cites_id,cites_url,version_num,versions_url,result_id
      1,1,Graph-based relational data visualization,https://ieeexplore.ieee.org/abstract/document/6676565/,2013,"DM De Lima, JF Rodrigues… - 2013 17th International …, 2013 - ieeexplore.ieee.org","… influence the relationships of the entities? • How do we … of the relationships between data entities intuitive and com… to the relationships linking Person to all the other entities, and …",https://www.academia.edu/download/61219486/Lima-et_al_IV-201320191114-101278-sscqhi.pdf,10,7270436057986000666,"https://scholar.google.com/scholar?cites=7270436057986000666&as_sdt=2005&sciodt=0,5&hl=en&num=20",8,"https://scholar.google.com/scholar?cluster=7270436057986000666&hl=en&lr=lang_en%7Clang_ja&num=20&as_sdt=2005&sciodt=0,5&as_ylo=2010&as_yhi=2020",GmdyBhPH5WQJ
      1,2,Architecture and system design issues of contemporary web-based information systems,https://ieeexplore.ieee.org/abstract/document/6089978/,2011,"B Molnár, A Tarcsi - 2011 5th International Conference on …, 2011 - ieeexplore.ieee.org","… reflected in the form of entity life history, life cycle, state chart or state transition diagram. … semi-structured document then storing , or linking to the data structure and content of underlying …",https://www.researchgate.net/profile/Balint-Molnar-5/publication/229034157_Architecture_and_system_design_issues_of_contemporary_Web-based_Information_Systems/links/00b4952becc9f6339a000000/Architecture-and-system-design-issues-of-contemporary-Web-based-Information-Systems.pdf,23,7691717608147233323,"https://scholar.google.com/scholar?cites=7691717608147233323&as_sdt=2005&sciodt=0,5&hl=en&num=20",7,"https://scholar.google.com/scholar?cluster=7691717608147233323&hl=en&lr=lang_en%7Clang_ja&num=20&as_sdt=2005&sciodt=0,5&as_ylo=2010&as_yhi=2020",K6o7gml4vmoJ
      1,3,"Model for the organization, storage and processing of large data banks of physiological variables",https://ieeexplore.ieee.org/abstract/document/7496757/,2016,"FE Palominos, H Diaz, FM Cordova… - … and Control (ICCCC …, 2016 - ieeexplore.ieee.org","… experimental protocols and relevant ethical requirements, linking the information with the methods of … a high-level entity called ""applies"" and the entity called ""registration"" (see Figure 4). …",https://www.researchgate.net/profile/Lucio-Canete/publication/304563530_Model_for_the_organization_storage_and_processing_of_large_data_banks_of_physiological_variables/links/5ad4aa3e458515c60f54555b/Model-for-the-organization-storage-and-processing-of-large-data-banks-of-physiological-variables.pdf,2,606900249744401617,"https://scholar.google.com/scholar?cites=606900249744401617&as_sdt=2005&sciodt=0,5&hl=en&num=20",2,"https://scholar.google.com/scholar?cluster=606900249744401617&hl=en&lr=lang_en%7Clang_ja&num=20&as_sdt=2005&sciodt=0,5&as_ylo=2010&as_yhi=2020",0WQcyI8kbAgJ
      1,4,Modelling project management and innovation competences for technology enhanced learning,https://ieeexplore.ieee.org/abstract/document/5756500/,2010,"SA Petersen, T Heikura - eChallenges e-2010 Conference, 2010 - ieeexplore.ieee.org","… The model is a step towards linking competence management to learning content. This … Using ideas from entity relationship modelling [16], we tried to identify how one competence may …",https://ieeexplore.ieee.org/iel5/5583931/5592106/05592523.pdf,15,7398039285246603700,"https://scholar.google.com/scholar?cites=7398039285246603700&as_sdt=2005&sciodt=0,5&hl=en&num=20",4,"https://scholar.google.com/scholar?cluster=7398039285246603700&hl=en&lr=lang_en%7Clang_ja&num=20&as_sdt=2005&sciodt=0,5&as_ylo=2010&as_yhi=2020",tDGCj4gdq2YJ
      1,5,From business functions to control functions: Transforming REA to ISA-95,https://ieeexplore.ieee.org/abstract/document/7264713/,2015,"A Mazak, C Huemer - 2015 IEEE 17th Conference on Business …, 2015 - ieeexplore.ieee.org",… entities and as such they are not described in the functional enterprise control model. These entities … REA does not provide any language concepts for linking identified tasks with agents…,https://www.academia.edu/download/38173551/CBI_2015_final_Mazak-Huemer.pdf,13,12823586430930390062,"https://scholar.google.com/scholar?cites=12823586430930390062&as_sdt=2005&sciodt=0,5&hl=en&num=20",8,"https://scholar.google.com/scholar?cluster=12823586430930390062&hl=en&lr=lang_en%7Clang_ja&num=20&as_sdt=2005&sciodt=0,5&as_ylo=2010&as_yhi=2020",LgwgquqH9rEJ
      ```
