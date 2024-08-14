# 🚀 RESTful API TUTORIAL

This project demonstrates the implementation of a Django RESTful API using different approaches across multiple Git branches. Each branch offers the same functionality but implemented in a distinct way. The main goal is to create an API that returns JSON responses for two entities: 📚 **Books** and ✍️ **Writers**.

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
