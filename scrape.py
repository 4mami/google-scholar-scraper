import os
import re
import sys
from urllib.parse import parse_qsl, urlsplit
import pandas as pd
from dotenv import dotenv_values
from serpapi import GoogleSearch

def get_inputs():
    ret = {}
    print('Type the query (optional if you want to specify "cites_id"):')
    q: str = input().strip()
    print("Type the cites_id to trigger Cited By searches (optional):")
    cites: str = input().strip()
    print("Type the year from which you want the results to be included (optional):")
    as_ylo: str = input().strip()
    print("Type the year until which you want the results to be included (optional):")
    as_yhi: str = input().strip()

    if q:
        ret["q"] = q
    if cites:
        ret["cites"] = cites
    if as_ylo:
        ret["as_ylo"] = as_ylo
    if as_yhi:
        ret["as_yhi"] = as_yhi
    return ret

def get_api_key():
    env_file = ".env"
    if not os.path.isfile(env_file):
        print('[Error] No ".env" file')
        sys.exit(1)

    config = dotenv_values(env_file)
    if "SERPAPI_KEY" not in config:
        print('[Error] No api key in ".env" file')
        sys.exit(1)
    return config["SERPAPI_KEY"]

def get_article_results(inputs, is_interactive=False):
    if "q" not in inputs and "cites" not in inputs:
        print("[Error] No query and no cites_id")
        sys.exit(1)
    params = {
        "api_key": get_api_key(),
        "engine": "google_scholar",
        "lr": "lang_en|lang_ja",
        "start": "0",
        "num": "20",
        }
    params.update(inputs)
    print("Waiting for article results to save..")
    search = GoogleSearch(params)

    publications = []
    publications_is_present = True
    total_results = ""
    while publications_is_present:
        results = search.get_dict()
        if "error" in results:
            if not publications:
                print(f"[Error] Api error: {results['error']}")
                sys.exit(1)
            print(f"[Warn ] Save current artical results because of api error: {results['error']}")
            return publications, params, total_results

        if not total_results : total_results = results["search_information"]["total_results"]
        print(f"Currently extracting page #{results.get('serpapi_pagination', {}).get('current', 1)}..")
        for result in results["organic_results"]:
            position = result["position"]
            title = result["title"]
            result_id = result["result_id"]
            link = result.get("link")
            snippet = result.get("snippet")
            publication_info_summary = result["publication_info"]["summary"]
            resources_link = result["resources"][0].get("link") if "resources" in result else None
            cited_by_total = result.get("inline_links", {}).get("cited_by", {}).get("total", 0)
            cited_by_cites_id = result.get("inline_links", {}).get("cited_by", {}).get("cites_id")
            cited_by_link = result.get("inline_links", {}).get("cited_by", {}).get("link")
            versions_total = result.get("inline_links", {}).get("versions", {}).get("total", 0)
            versions_link = result.get("inline_links", {}).get("versions", {}).get("link")

            year_lis = re.findall(r"\d\d\d\d", publication_info_summary)
            publications.append({
                "page_number": results.get("serpapi_pagination", {}).get("current", 1),
                "position": position + 1,
                "title": title,
                "url": link,
                "year": int(year_lis[-1]) if year_lis else 0,
                "publication_info": publication_info_summary,
                "snippet": snippet,
                "pdf_url": resources_link,
                "cited_num": cited_by_total,
                "cites_id": cited_by_cites_id,
                "cites_url": cited_by_link,
                "version_num": versions_total,
                "versions_url": versions_link,
                "result_id": result_id
                })

        if "next" in results.get("serpapi_pagination", {}):
            # splits URL in parts as a dict and passes it to a GoogleSearch() class.
            if is_interactive:
                print(f"Want to stop? ({len(publications)}/{total_results}): [yes/no/all]")
                ans = input().strip()
                if ans == "yes":
                    break
                elif ans == "all":
                    is_interactive = False
            search.params_dict.update(dict(parse_qsl(urlsplit(results["serpapi_pagination"]["next"]).query)))
        else:
            publications_is_present = False
    return publications, params, total_results

def save_article_results_to_csv(article_results, params, total_results):
    csv_file = ""
    if "q" in params and "cites" in params:
        csv_file = f"outputs/cites({params['cites']})_query({params['q']})_total({len(article_results)}-{total_results}).csv"
    elif "cites" not in params:
        csv_file = f"outputs/query({params['q']})_total({len(article_results)}-{total_results}).csv"
    else:
        csv_file = f"outputs/cites({params['cites']})_total({len(article_results)}-{total_results}).csv"

    if not os.path.isdir("outputs"):
        os.mkdir("outputs")
    pd.DataFrame(data=article_results).to_csv(csv_file, encoding="utf-8", index=False)
    print("Article results Saved.")

def main():
    inputs = get_inputs()
    args = sys.argv
    if len(args) > 1 and args[1] == "-i":
        publications, params, total_results = get_article_results(inputs, True)
    else:
        publications, params, total_results = get_article_results(inputs)
    save_article_results_to_csv(publications, params, total_results)

if __name__ == '__main__':
    main()
