# Online Shopping Web App Backend

This repository contains the backend code for the Online Shopping Web App. It provides the necessary APIs and functionalities to support the frontend of the application.

## Installation

1. Clone the repository:

    ```shell
    git clone 
    cd online-shopping-web-app-backend
    ```

2. Create and activate a virtual environment:

    ```shell
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```shell
    pip install -r requirements.txt
    ```

4. Set up MongoDB:

    - Install MongoDB and start the MongoDB service.
    - Alternatively, you can use a cloud-based MongoDB service like MongoDB Atlas.

5. Create a `config.py` file for the configuration settings:

    ```python
    # config.py
    class Config:
        MONGO_URI = "mongodb://localhost:27017/online-shopping-db"
    ```

## Running the Application

To run the application, execute the following command:

```shell
python app.py
```

## Usage
The server will be running on http://localhost:5000 by default.
Use a tool like Postman to test the available APIs.
API Endpoints
Here are some example API endpoints you can use:

### Add an Item:

- **URL:** http://localhost:5000/items
- **Method:** POST
- **Request Body:**
    ```json
    {
        "item_code": "I001",
        "description": "ASUS VIVOBOOK X512FA",
       "category": "Laptop",
        "description": "ASUS VIVO BOOK 15",
        "item_code": "I005",
        "price": 3500,
        "rating": 3.5,
        "stock": 50
    }
    ```
- **Response:**
- **Success Response:**
  ```json
    {
    "success": True
    }
    ```
- **Error Response:**
    ```json
    {
        "error": "Item already exists"
    }
    ```
### Get All Items:

- **URL:** http://localhost:5000/items
- **Method:** GET
- **Response:**
- **Success Response:**
    ```json
    {
        "items": [
            {
                "category": "Laptop",
                "description": "ASUS VIVO BOOK 15",
                "item_code": "I005",
                "price": 3500,
                "rating": 3.5,
                "stock": 50
            },
            {
                "category": "Laptop",
                "description": "ASUS VIVO BOOK 15",
                "item_code": "I005",
                "price": 3500,
                "rating": 3.5,
                "stock": 50
            }
        ]
    }
    ```
- **Error Response:**
    ```json
    {
        "error": "No items found"
    }
    ```

### Get an Item:

- **URL:** http://localhost:5000/items/I001
- **Method:** GET
- **Response:**
- **Success Response:**
    ```json
    {
        "category": "Laptop",
        "description": "ASUS VIVO BOOK 15",
        "item_code": "I005",
        "price": 3500,
        "rating": 3.5,
        "stock": 50
    }
    ```
- **Error Response:**
    ```json
    {
        "error": "Item not found"
    }
    ```
### Update an Item:

- **URL:** http://localhost:5000/items/I001
- **Method:** PUT
- **Request Body:**
    ```json
    {
        "price": 4000,
        "stock": 40
    }
    ```
- **Response:**
- **Success Response:**
    ```json
    {
        "success": True
    }
    ```
- **Error Response:**
    ```json
    {
        "error": "Item not found"
    }
    ```
### Delete an Item:

- **URL:** http://localhost:5000/items/I001
- **Method:** DELETE
- **Response:**
- **Success Response:**
    ```json
    {
        "success": True
    }
    ```
- **Error Response:**
    ```json
    {
        "error": "Item not found"
    }
    ```
## Requirements
The application requires the following dependencies:

```shell
Flask==1.1.2
Flask-PyMongo==2.3.0

```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
