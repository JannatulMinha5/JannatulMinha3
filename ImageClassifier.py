import requests

class ImageClassifier:
    def __init__(self, api_key):
        self.api_key = api_key

    def classify_image(self, image_url):
        url = "https://api.imagerecognition.com/v1/classify"
        headers = {
            "API-Key": self.api_key
        }
        data = {
            "url": image_url
        }
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if response.status_code == 200:
            if "predictions" in result:
                print("Image Classification Result:")
                for prediction in result["predictions"]:
                    label = prediction["label"]
                    confidence = prediction["confidence"]
                    print(f"- Label: {label}, Confidence: {confidence}")
            else:
                print("Unable to classify the image.")
        else:
            print("Unable to process the image.")

def main():
    api_key = "YOUR_API_KEY"
    image_url = "https://example.com/image.jpg"

    classifier = ImageClassifier(api_key)
    classifier.classify_image(image_url)

if __name__ == "__main__":
    main()
