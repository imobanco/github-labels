from main import create_or_update_labels, delete_existing_labels

owner = "imobanco"
repos = [
    "income-front",
    "imobanco.github.io",

    "income-back",
    "imopay-api",
    "bb-wrapper",
    "zoop-wrapper",
    "imopay-wrapper",
    "as-webservice-wrapper"
]

for repo in repos:
    print(f"Running for {repo}")
    # delete_existing_labels(owner=owner, repo=repo)
    create_or_update_labels(owner=owner, repo=repo)
