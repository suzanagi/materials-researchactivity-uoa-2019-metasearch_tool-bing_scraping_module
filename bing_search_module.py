import sys
import requests
from bs4 import BeautifulSoup
from result_item import ResultItem

def search(query):
    # Prepare a list for returning the search results
    result = list()
    # Prepare a parameter for the given query
    param = {"q": query}
    try:
        # Get the Bing search result page for the query
        rt = requests.get("https://www.bing.com/search", params = param)
        # Analyse the result page using BeautifulSoup
        soup = BeautifulSoup(rt.text, "html.parser")
    except:
        print("Internet Disconnected. Connect to download text.")
    # Obtain topics and URL element by the BeautifulSoup function
    results = soup.find("ol", {"id":"b_results"})
    lists = results.findAll("li", {"class":"b_algo"})
    rank = 1
    for item in lists:
        item_text = item.find("a").text
        item_href = item.find("a").attrs["href"]
        # Put the results in the list to be returned
        if item_text and item_href:
            r_item = ResultItem(item_text, item_href, "Bing")
            r_item.add_rank(rank)
            result.append(r_item)
            rank += 1
    # Return the result list
    return result

# Main Function
if __name__ == "__main__":
    # Prepare query vairable
    query = sys.argv[1]
    # Append multiple query words with "+"
    for arg in sys.argv[2:]:
        query = query + '+' + arg
    # Experiment the search function
    result = search(query)
    # Print the result list to the command line
    for item in result:
        print("[title] "+item.title)
        print("[url] "+item.url)
        print("[rank] "+str(item.rank))
        print("\n")

