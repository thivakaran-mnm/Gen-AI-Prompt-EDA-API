import requests

def get_news(api_key, keyword):
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': keyword,
        'apiKey': api_key,
        'language': 'en',
        'sortBy': 'publishedAt'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        data = response.json()

        if data['status'] == 'ok':
            articles = data['articles']
            if articles:
                print(f"Top news articles for '{keyword}':\n")
                for index, article in enumerate(articles[:5], start=1):
                    print(f"{index}. {article['title']}")
                    print(f"   Source: {article['source']['name']}")
                    print(f"   Published at: {article['publishedAt']}")
                    print(f"   URL: {article['url']}\n")
            else:
                print(f"No articles found for '{keyword}'.")
        else:
            print("Error: ", data.get('message', 'Unknown error occurred'))

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    api_key = "505941a927e74a929c525328196c4b59"  # Replace with your actual NewsAPI key
    keyword = input("Enter a keyword to search for news: ")
    get_news(api_key, keyword)

if __name__ == "__main__":
    main()
