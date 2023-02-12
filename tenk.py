from sec_api import QueryApi

queryApi = QueryApi(api_key="06f52aff513852105d085561a23c6212a7df5b277582e1a5e9c76c8bb95ba01f")

query = {

        "query": {"query_string:": {
            "query": "ticker:TSLA AND formType:\"10-K\""
            }},
        "from": "0",
        "size": "10",
        "sort": [{ "filedAt": { "order": "desc" } }]
}

filings = queryApi.get_filings(query)

print(filings)



