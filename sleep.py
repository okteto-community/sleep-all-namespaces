import requests
import json
import sys
import os


if __name__ == "__main__":

  url = os.environ.get("OKTETO_URL")
  token = os.environ.get("OKTETO_TOKEN")
  binary = '/usr/local/bin/okteto'

  endpoint = f"{url}/graphql"
  headers = {"Authorization": f"Bearer {token}"}

  query = """
    query getClusterNamespaces {
      clusterNamespaces {
        namespaces {
        name
        persistent
        status
        }
      }
    }
  """

  r = requests.post(endpoint, json={"query": query}, headers=headers)
  if r.status_code != 200:
    raise Exception(f"Query failed to run with a {r.status_code}.")

  namespaces = r.json()['data']['clusterNamespaces']['namespaces']
  for n in namespaces:
    if n['persistent'] != True:
      if n['status'] == "Sleeping":
        print(f"Namespace {n['name']} is already sleeping.")
      else:
        os.system(f"{binary} namespace sleep {n['name']}")