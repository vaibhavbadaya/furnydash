# Furniture Management System

This Furniture Management System is designed to help in the management and organization of furniture inventory for a furniture store or warehouse. It provides functionalities to add, update, delete, and track furniture items along with their details.

## Features

- **Inventory Management**: Easily manage furniture inventory by adding, updating, and deleting items.
- **Categorization**: Organize furniture items into categories for easy navigation and sorting.
- **Search and Filter**: Search for specific furniture items and apply filters based on categories, price range, availability, etc.
- **Reports**: Generate reports to track inventory levels, sales, and other relevant metrics.
- **User Management**: Control access with user authentication and authorization levels.

## Installation

### Requirements

- Python 3.x
- Django Framework
- MySQL/SQLite/PostgreSQL (Choose database as per requirements)

### Installation Steps

1. **Clone the repository**:

    ```bash
 git clone https://github.com/vaibhavbadaya/furnydash.git
    ```

2. **Install dependencies**:

    ```bash
    cd furniture-management
    pip install -r requirements.txt
    ```

3. **Configure Database**:

    - Modify `settings.py` to set up the database connection.
    - Run migrations:

        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```

4. **Run the application**:

    ```bash
    python manage.py runserver
    ```

Access the application at `http://127.0.0.1:8000/`.

## Usage

- Access the admin panel to manage furniture items and categories: `http://127.0.0.1:8000/admin/`.
- Use appropriate credentials to log in (default admin credentials provided in development).
- Explore different functionalities and features to manage furniture inventory efficiently.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any enhancements, bug fixes, or new features.

## License

This project is licensed under the [MIT License](LICENSE).
