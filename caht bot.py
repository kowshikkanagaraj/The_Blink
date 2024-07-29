import requests

API_KEY = 'your_api_key_here'
API_ENDPOINT = 'https://api.example.com/career_guidelines'

def get_career_guidelines(career_name):
    headers = {'Authorization': f'Bearer {API_KEY}'}
    params = {'career_name': career_name}
    
    response = requests.get(API_ENDPOINT, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['guidelines']
    else:
        return "Unable to retrieve career guidelines."

def main():
    print("Welcome to the Career Path Guidelines System!")
    while True:
        career_name = input("Enter a career path (or 'quit' to exit): ")
        if career_name.lower() == "quit":
            break
        if not career_name:
            print("Please enter a career path.")
            continue
        guidelines = get_career_guidelines(career_name)
        if guidelines:
            print("Guidelines:")
            print(guidelines)
        else:
            print(f"No guidelines found for '{career_name}'.")
            print("Please try another career path.")

if __name__ == "__main__":
    main()
