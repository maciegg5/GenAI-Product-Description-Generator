# GenAI-Product-Description-Generator

An API and terminal client project for generating e-commerce product descriptions using AI. The application generates engaging and unique product descriptions based on the product's name and category. The project is built with FastAPI and utilizes NLP models to enable integration with various e-commerce systems.

🚀 Features:
Generate product descriptions based on the name and category of the product.

Filter products by category.

Quick integration with external systems via API.

📂 Project Structure:
genai/
├── main.py           # FastAPI backend
├── client.py         # Terminal client
├── products.json     # Stored products
├── requirements.txt  # Dependency list
└── README.md         # This file

🚀 How to Run the Project
1. Install Dependencies
Make sure you have Python 3.9+ and pip installed. Then run:

pip install -r requirements.txt
If you don’t have uvicorn installed, you can add it manually:
pip install fastapi uvicorn

2. Start the API Server
From the genai/ directory:
uvicorn main:app --reload
The app will run at http://127.0.0.1:8000

You can test endpoints in the Swagger UI interface:

👉 http://127.0.0.1:8000/docs

3. Run the Terminal Client
In a new terminal window:
python client.py
Features:

Add a product with an AI-generated description.

View all products.

Filter by category.

🧪 Sample Data
Product data is stored in the products.json file after app execution.

💡 Ideas for Improvement
Add product deletion.

Integrate a real NLP model (e.g., OpenAI API).

Build a web interface (React or Vue).

