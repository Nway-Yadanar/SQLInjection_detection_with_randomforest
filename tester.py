import requests

# URL of the prediction endpoint
predict_url = 'http://127.0.0.1:5000/predict'

while True:
    # Get user input for SQL query
    query_to_predict = input("Enter your SQL query (or type 'exit' to quit): ")
    
    # Exit condition
    if query_to_predict.lower() == 'exit':
        print("Exiting...")
        break
    
    # Data payload for the POST request
    data = {'query': query_to_predict}
    
    try:
        # Send a POST request to the prediction endpoint
        response = requests.post(predict_url, json=data)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and print the JSON response
            prediction_result = response.json()
            print("Prediction Result:", prediction_result)
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
