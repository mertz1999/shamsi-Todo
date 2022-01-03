import requests

# --- This Function get today date in shamsi format
def today():
    # --- months
    month = ['fa','or','kh','ti','mo','sh','me','ab','az','de','ba','es']

    # --- api-endpoint
    URL = "https://api.keybit.ir/time/"

    # --- sending get request and saving the response as response object
    r = requests.get(url = URL)

    # --- extracting data in json format
    data = r.json()
    date = data["date"]["full"]["official"]["usual"]["en"]
    # --- find short string to push it database
    short_data = date[-2::]+month[int(date[5:7])-1]

    return date,short_data

# print(today())