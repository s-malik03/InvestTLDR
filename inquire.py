import json
import requests
import parse_report

API_KEY_HEADER = "X-API-KEY"


def generate_key(url: str, email: str):
    response = requests.post(f"{url}/generate-key", json={"email": email})
    return response


def ask_collection(url: str, collection_name: str, q: str, key: str):
    response = requests.get(
        f"{url}/ask/{collection_name}?q={q}", headers={API_KEY_HEADER: key}
    )
    return response


def create_collection(url: str, collection_name: str, json_file: str, key: str):
    with open(json_file, "r") as f:
        data = json.load(f)
    response = requests.post(
        f"{url}/create/text/{collection_name}", json=data, headers={API_KEY_HEADER: key}
    )
    return response


def create_collection_from_notion_db(
    url: str, collection_name: str, token: str, db_id: str, key: str
):
    response = requests.post(
        f"{url}/create/notion/{collection_name}",
        json={"notion_integration_token": token, "database_id": db_id},
        headers={API_KEY_HEADER: key},
    )
    return response


def update_collection(url: str, collection_name: str, json_file: str, key: str):
    with open(json_file, "r") as f:
        data = json.load(f)
    response = requests.patch(
        f"{url}/update/text/{collection_name}", json=data, headers={API_KEY_HEADER: key}
    )
    return response


def update_collection_from_notion_db(
    url: str, collection_name: str, token: str, db_id: str, key: str
):
    response = requests.patch(
        f"{url}/update/notion/{collection_name}",
        json={"notion_integration_token": token, "database_id": db_id},
        headers={API_KEY_HEADER: key},
    )
    return response


def history_collection(url: str, collection_name: str, key: str):
    response = requests.get(
        f"{url}/history/{collection_name}", headers={API_KEY_HEADER: key}
    )
    return response


def delete_collection(url: str, collection_name: str, key: str):
    response = requests.delete(
        f"{url}/delete/{collection_name}", headers={API_KEY_HEADER: key}
    )
    return response


if __name__ == "__main__":
    base_url = "https://inquire.maheshnatamai.com"

    key = "8ZC8lvc9IBCZQb4jj-O9Uw"

    print(key)

    response = create_collection(base_url, "data", "data.json", key)
    response = ask_collection(
         base_url,
         "data",
         "Should I invest in Apple? Yes or no. Give reasons why.",
         key
     )
    try:
        print(json.loads(response.text)['response'])

    except:
        print(json.loads(response.text))

    #response = history_collection(base_url, "10k", key)
    #response = update_collection(base_url, "10k", "10k.json", key)
    response = delete_collection(base_url, "data", key)
