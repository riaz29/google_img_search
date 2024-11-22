from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

# Test CI on github action 2
# Google Custom Search API details
API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
CX = "eeeeeeeeeeeeeeeeeee"

@app.route("/", methods=["GET", "POST"])
def index():
    images = []
    if request.method == "POST":
        query = request.form.get("q")
        if query:
            # Prepare the API request
            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                "key": API_KEY,
                "cx": CX,
                "q": query,
                "searchType": "image"
            }
            headers = {"Content-type": "application/json"}

            try:
                # Make the API call
                response = requests.get(url, params=params, headers=headers)
                data = response.json()

                # Extract image links
                if "items" in data:
                    images = [item["link"] for item in data["items"]]
            except Exception as e:
                print(f"Error: {e}")

    return render_template("index.html", images=images)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
