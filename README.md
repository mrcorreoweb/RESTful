# 🚀 Same API in Django in 9 different ways

This project demonstrates the implementation of a Django RESTful API using 9⃣️ different approaches across multiple Git branches. Each branch offers the same functionality but implemented in a distinct way. 

The main goal is to create an API that returns JSON responses for two entities: 📚 **Books** and ✍️ **Writers**.

## API endpoints

The following are the API endpoints available for managing 📚 **Books** and ✍️ **Writers**:

### Writers Endpoints ✍️

- **List Writers**:

  - **Endpoint:** `library/writers/`
  - **Method:** `GET`
  - **Description:** Retrieve a list of all writers.

- **Create Writer**:

  - **Endpoint:** `library/writers/`
  - **Method:** `POST`
  - **Description:** Add a new writer.

- **Retrieve Writer**:

  - **Endpoint:** `library/writers/<int:id>/`
  - **Method:** `GET`
  - **Description:** Retrieve details of a specific writer.

- **Update Writer**:

  - **Endpoint:** `library/writers/<int:id>/`
  - **Method:** `PUT`
  - **Description:** Update an existing writer.

- **Delete Writer**:
  - **Endpoint:** `library/writers/<int:id>/`
  - **Method:** `DELETE`
  - **Description:** Delete a writer.

### Books Endpoints 📚

- **List Books**:

  - **Endpoint:** `library/books/`
  - **Method:** `GET`
  - **Description:** Retrieve a list of all books.

- **Create Book**:

  - **Endpoint:** `library/books/`
  - **Method:** `POST`
  - **Description:** Add a new book.

- **Retrieve Book**:

  - **Endpoint:** `library/books/<int:id>/`
  - **Method:** `GET`
  - **Description:** Retrieve details of a specific book.

- **Update Book**:

  - **Endpoint:** `library/books/<int:id>/`
  - **Method:** `PUT`
  - **Description:** Update an existing book.

- **Delete Book**:
  - **Endpoint:** `library/books/<int:id>/`
  - **Method:** `DELETE`
  - **Description:** Delete a book.

## 📋 Project Structure

Below is a breakdown of the project branches and their respective implementations:

### 🌿 Main Branch: `main`

- **Approach:** Django Function-Based Views (FBVs).
- **Description:** Implements the API using traditional Django FBVs.

### 🌱 Branch: `DCBVs`

- **Approach:** Django Class-Based Views (CBVs).
- **Description:** Re-implements the API using Django's CBV pattern.

### 🛠️ Branch: `DRF-FBVs`

- **Approach:** Django Rest Framework (DRF) + Function-Based Views.
- **Description:** Enhances the FBV implementation by using DRF with the `@api_view` decorator.

### 🏗️ Branch: `DRF-CBVs`

- **Approach:** DRF + Class-Based Views.
- **Description:** Extends the CBV pattern by using DRF's `APIView` class and response modules.

### 🌿 Branch: `DRF-Mixins`

- **Approach:** DRF + Mixins.
- **Description:** Re-implements the API using DRF's mixins for common actions like `list`, `create`, `retrieve`, `update`, and `destroy`.

### 🌳 Branch: `DRF-GenericCBVs`

- **Approach:** DRF + Generic Class-Based Views.
- **Description:** Implements the API using DRF's generic class-based views, providing a more concise and reusable structure for common patterns.

### 🧰 Branch: `DRF-CBVs-ViewSets`

- **Approach:** DRF + ViewSets.
- **Description:** Further evolves the API implementation using DRF's `ViewSets`.

### ⚙️ Branch: `DRF-CBVs-ModelViewSets`

- **Approach:** DRF + ModelViewSets.
- **Description:** Final evolution that leverages DRF’s `ModelViewSets` to simplify the codebase using built-in capabilities.

### 🧵 Branch: `DRF-HMSs`

- **Approach:** DRF + ModelViewSets + HyperlinkedModelSerializers.
- **Description:** From DRF’s `ModelViewSets` change serializers to use API urls as primary keys.

## Setup Instructions

### 1. Install Dependencies

Make sure you have Python and pip installed, then install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Create the .env file

In the project root, create a .env file to store environment-specific settings. This file should include the SECRET_KEY for Django and any other sensitive information. You can generate a new SECRET_KEY using the following Python command:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Once you have generated the secret key, create a .env file and add the following:

```bash
SECRET_KEY=your_generated_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 3. Add .env to .gitignore

To prevent sensitive information from being committed to version control, ensure the .env file is added to your .gitignore file. Open or create the .gitignore file in the root directory of your project, and add the following:

```bash
# Ignore .env file containing sensitive data
.env
```

### 4. Run Migrations

Apply the necessary database migrations by running the following command:

```bash
python manage.py migrate
```

### 5. Start the Development Server

Once the migrations are complete, start the Django development server:

```bash
python manage.py runserver
```

Your API will now be accessible at <http://localhost:8000/library/(...)> completed with the appropriate endpoints (see [API endpoints](#api-endpoints)).

### 6. Testing

If you are using VSCode you can use the REST Client extension to send requests to the API.

You will find files for the CRUD operations using REST Client in the test-api-request folder.

## Contributing

If you'd like to contribute to this project, please follow the contribution guidelines to get started.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
