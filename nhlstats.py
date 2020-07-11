#!/usr/bin/env python3

from argparse import ArgumentParser
import ipaddress
import json
import requests
import sys

# DISABLE HTTPS CERTIFICATE WARNINGS
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# PROVIDE THE SITE API WEBADDRESS
apiBaseUrl = 'https://statsapi.web.nhl.com/api/v1/people/'

# CREATE ARGUMENT PARSER, ALLOWING USER TO PROVIDE IP ADDRESS ARGUMENT
def create_parser():
    parser = ArgumentParser(
        description='Queries NHL API for information'
    )
    parser.add_argument(
        'nhlstat',
        type=str,
        help='Provide the stat you would like to gather'
    )
    return parser.parse_args()


ARGS = create_parser()


def main():
    # SET IP PROVIDED IN ARGUMENTS BY USER TO VARIABLE
    nhlstat = ARGS.nhlstat
    
    # QUERY USING THE NHL SUB YOU ARE LOOKING FOR
    n = 8476881 # Player IDs seem to start at 847xxxx
    while n <= 8479000:
        playerId = str(n)
        response = requests.get(apiBaseUrl + playerId, verify=False)
        n = n + 1
        # PRINT OUT RESULTS FROM QUERY
        try:
            output = json.loads(response.text)
            for names in output['people']:
                name = names['fullName']
                print("{}:{}".format(name, playerId))
        except IndexError:
            print("There is no information for this stat.")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()