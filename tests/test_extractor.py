from web_extractor import WebDataExtractor
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Create the extractor
extractor = WebDataExtractor(api_key=gemini_api_key)

# URL of the product you want to extract data from
amazon_url = "https://www.amazon.in/Celestron-AstroMaster-130-EQ-Telescope/dp/B000MLL6RS"

# Define what information you want to get
schema = {
    "name": "string",    # Product name
    "price": "float",    # Product price
    "description": "string"  # Product description
}

# Get the data
result = extractor.extract(amazon_url, schema)

# Print the results
print("Product Name:", result["name"])
print("Price:", result["price"])
print("Description:", result["description"])