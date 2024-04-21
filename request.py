import requests

# Replace the URL with the appropriate endpoint of your Flask application
url = 'http://localhost:5000/predict_api'
url1 ='http://localhost:5001/predict_api'

# Assuming your model expects an image for face identification
# You need to pass the image data instead of 'experience', 'test_score', and 'interview_score'
# Replace 'image_data' with the actual image data you want to send
image_data = open('image.jpg', 'rb').read()

# Send a POST request with the image data
r = requests.post(url, files={'image': image_data})

# Print the response from the server
print(r.json())
