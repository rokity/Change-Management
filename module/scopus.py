import requests
import json
import pandas as pd
import numpy as np


class Scopus:

  def __init__(self, API_KEY):
    """
      Constructor of class Scopus for API request. Get Api Key from https://dev.elsevier.com/apikey/manage .
    Args:
        API_KEY ([string]): [API KEY string retreivable from https://dev.elsevier.com/apikey/manage]
    """
    self.api_key = API_KEY

  def get_chunk(self, key, start, count='25', date='2010-2020'):
    resp = requests.get(f"https://api.elsevier.com/content/search/scopus?query={key}&start={start}&count={count}&date={date}",
                        headers={'Accept': 'application/json',
                                 'X-ELS-APIKey': self.api_key})
    data = json.loads(resp.text.encode('utf-8'))
    return data

  def execute_query(self, query, start=0, count=25, date='2010-2020'):
    """
      Execute single query .
    Args:
        query ([string]): [query composed]
        start (int, optional): [cursor index start]. Defaults to 0.
        count (int, optional): [cursor index of how many results you want, maximum it's 25]. Defaults to 25.
        date (str, optional): [range of date or single date or single year]. Defaults to '2010-2020'.

    Returns:
        [int]: [total results obtained from the API Request]
    """
    data = self.get_chunk(query, start, count, date=date)
    total_results = int(data['search-results']['opensearch:totalResults'])
    return int(total_results)
