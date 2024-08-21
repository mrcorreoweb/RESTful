# 🚀 Learning APIs in Django 

This project demonstrates the implementation of a Django RESTful API using different approaches across multiple Git branches. Each branch offers the same functionality but implemented in a distinct way. The main goal is to create an API that returns JSON responses for two entities: 📚 **Books** and ✍️ **Writers**.

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

### 🧰 Branch: `DRF-CBVs-ViewSets`

- **Approach:** DRF + ViewSets.
- **Description:** Further evolves the API implementation using DRF's `ViewSets`.

### ⚙️ Branch: `DRF-CBVs-ModelViewSets`

- **Approach:** DRF + ModelViewSets.
- **Description:** Final evolution that leverages DRF’s `ModelViewSets` to simplify the codebase using built-in capabilities.
