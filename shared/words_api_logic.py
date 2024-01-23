import requests

def get_word_data():
    headers = {
        'X-RapidAPI-Host': 'rapidapi.com',
        'X-RapidAPI-Key': 'c863513ba3msh8381449115dcebbp162aecjsn47843bc49832',
    }

    try:
        response = requests.get("https://wordsapiv1.p.rapidapi.com/words/random_words", headers=headers)
        response.raise_for_status()
        word_data = response.json()

        if "success" in word_data and not word_data["success"]:
            print(f"API Error: {word_data['message']}")
            return {"word": "N/A", "meaning": "N/A"}

        return {"word": word_data["word"], "meaning": word_data["meaning"]}

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
        return {"word": "N/A", "meaning": "N/A"}
    except requests.exceptions.RequestException as req_err:
        print(f"Request Exception: {req_err}")
        return {"word": "N/A", "meaning": "N/A"}

# Example usage
api_response = get_word_data()
print(api_response)
