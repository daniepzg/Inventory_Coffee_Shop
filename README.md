# Coffee Shop Inventory Manager

## Overview

Welcome to the Coffee Shop Inventory Manager! This project is a simple inventory management system designed for coffee shops. It allows users to manage product inventory, generate reports, and handle various data formats (CSV, Pickle, JSON).

## Features

- **Manage Inventory**: Add, remove, and update products in the inventory.
- **Generate Reports**: Create and export various reports such as current inventory, products to expire, and assets balance.
- **Data Handling**: Supports reading and saving data in multiple formats (CSV, Pickle, JSON).
- **Logging**: Logs events to either a file or the console.

## Components

### Inventory Management

- **`Inventory` Class**: Handles product management and integrates with the data adapter to load and save data.
- **`Product` Class**: Represents a product with attributes like type, name, price, description, and quantity.

### Reporting

- **`Reports` Class**: Generates and exports different reports based on the inventory data.

### Data Adapters

- **`CsvAdapter`**: Reads and writes CSV files.
- **`PickleAdapter`**: Reads and writes Pickle files.
- **`JsonAdapter`**: Reads and writes JSON files.

### Logging

- **`LoggerFactory`**: Creates either a `FileLogger` or `ConsoleLogger`.
- **`FileLogger`**: Logs messages to a file.
- **`ConsoleLogger`**: Logs messages to the console.

### User Interface

- **`Menu` Class**: Provides a text-based menu for interacting with the inventory and reports.
- **`main` Function**: Handles user input and orchestrates menu operations.

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/coffee-shop-inventory-manager.git
   ```

2. **Install Dependencies**:
   Make sure you have Python and the required libraries installed. You can install the necessary libraries using:
   ```bash
   pip install pandas
   ```

3. **Run the Application**:
   ```bash
   python main.py
   ```

4. **Follow the Prompts**:
   Use the menu to manage inventory, generate reports, or choose the data format for your coffee shop.

## Example Usage

- **Add New Product**:
   - Choose option `2` in the inventory menu.
   - Enter product details when prompted.

- **Generate a Report**:
   - Choose option `1`, `2`, or `3` in the report menu to generate different types of reports.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements. Please ensure that your contributions follow the project's guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
