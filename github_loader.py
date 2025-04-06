from github import Github
import json

def load_catalog_from_github():
    g = Github("your_github_token")  # Replace with token or use env var
    repo = g.get_repo("org_or_username/repo_name")
    file = repo.get_contents("path/to/products.json")  # e.g., "data/products.json"
    data = json.loads(file.decoded_content)
    return data
