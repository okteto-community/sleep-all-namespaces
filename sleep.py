import argparse
import requests
import json
import sys
import os


if __name__ == "__main__":

  parser = argparse.ArgumentParser(
            prog='sleep',
            description='Sleep all available namespaces')

  parser.add_argument('url')  
  parser.add_argument('token')  
  parser.add_argument('binary', default='okteto')
  args = parser.parse_args()  
  
  endpoint = f"{args.url}/graphql"
  headers = {"Authorization": f"Bearer {args.token}"}


  query = """
    query getClusterNamespaces {
      clusterNamespaces {
        namespaces {
        name
        persistent
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
      os.system(f"{args.binary} namespace sleep {n['name']}")


