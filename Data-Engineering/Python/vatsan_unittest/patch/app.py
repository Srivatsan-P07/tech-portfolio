import requests

class RandomUser:
    def __init__(self):
        self.url = "https://randomuser.me/api/"

    def get_user(self):
        try:
            # Send a GET request to the API
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error if the request failed
            

            # Parse the JSON data
            data = response.json()

            # Extract relevant information
            user = data['results'][0]
            output_dict = {}
            output_dict["Name"] = user['name']['first'] +' '+ user['name']['last']
            output_dict["Gender"] = user['gender']
            output_dict["Email"] = user['email']
            output_dict["Location"] = user['location']['city']+' '+user['location']['country']

            return output_dict

        except requests.exceptions.RequestException as e:
            print("Error:", e)

instance = RandomUser()
instance.get_user()