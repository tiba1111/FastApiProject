# FastApiProject

## Description

This is a simple backend application built with **FastAPI** that exposes an HTTPS RESTful **GET** endpoint `/address`. The endpoint returns a JSON object containing an address, where the postcode is dynamically retrieved from environment variables.

### Key Features:
- **Environment Variables**: Postcode and other address fields are pulled from environment variables using the `.env` file for easy configuration management.
- **HTTPS Support**: The app is configured to run with HTTPS, ensuring secure communication.
- **Production-Grade Practices**: Implements best practices including:
  - Input validation with **Pydantic** models.
  - Secure app configuration with **dotenv** to handle environment variables.
  - The app is structured for ease of scalability and deployment in production environments.

## Features

- **Address Retrieval**: Fetches and returns an address (street, city, country, postcode) as JSON.
- **HTTPS Support**: The app supports secure connections through HTTPS, ensuring data privacy.
- **Environment Variable Management**: Configuration is handled securely using environment variables in a `.env` file.
- **Production-Grade Security**: The app can be deployed in production with HTTPS, security headers, and environment-specific configuration.

## Prerequisites

Before running the app, make sure you have the following installed:

- Python 3.7+ (preferably 3.8 or higher)
- Virtual environment management (optional, but recommended)
#####

Folder Structure
FastApiProject/
├── main.py                # Main FastAPI app
├── routers/               # Folder for API routers (optional)
├── models.py              # Pydantic models
├── config.py              # Configuration file (loads environment variables)
├── .env                   # Environment variables
├── requirements.txt       # List of dependencies
├── test_main.py           # Tests for FastAPI app
└── README.md  
####
1)Clone the Repository
First, clone the repository to your local machine:


git clone https://github.com/tiba1111/FastApiProject.git
cd FastApiProject

2)Set Up a Virtual Environment
Create a virtual environment to isolate the dependencies:
#####
python -m venv venv
Activate the virtual environment:
#####
Windows:
.\venv\Scripts\activate
#####
Linux/Mac:
source venv/bin/activate

####
3)Install Dependencies
Install the required dependencies using pip:
pip install -r requirements.txt
Or, if you don't have requirements.txt:
pip install fastapi pydantic pytest httpx
####
4) Set Up Environment Variables
 Create a .env file at the root of the project and add the following content:
ADDRESS_POSTCODE=75001  # Set your desired postcode here

#####
5) Run the Application
To run the FastAPI app locally, execute the following command:
uvicorn main:app --reload
This will start the FastAPI server at http://127.0.0.1:8000.
######
6) Access the API
To access the API, visit:
http://127.0.0.1:8000/address
It will return the address in JSON format, e.g.:
{
  "street": "123 Main Street",
  "city": "Sample City",
  "postcode": "75001"
}
#####
7)Running Tests
To run tests for your FastAPI application, use pytest:
pytest test_main.py
############
PROJECT DEMO VIDEO 
https://youtube.com/shorts/dOn-EOUoflQ?si=XIrdTDB80fuBWI4x
