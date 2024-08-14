# Gemini LLM-Based SQL Query Generator

This project is a web-based application that uses a Large Language Model (LLM) to convert natural language questions into SQL queries, execute them on a SQLite database, and display the results. The application is built using Streamlit and is designed to make SQL querying accessible to users who may not be familiar with SQL syntax.

## Link to the application

https://sql-data-retriever-using-llm-lwqnroeevfdy6yxp7vwcby.streamlit.app/


## Features

- **Natural Language to SQL Conversion**: Users can input their queries in plain English, and the application will convert them into SQL queries.
- **SQL Execution**: The generated SQL queries are executed on a pre-defined SQLite database.
- **Query Results**: The results of the queries are displayed in a tabular format within the application.
- **View Entire Table**: Users have the option to view the entire database table in a tabular format.
- **User-Friendly Interface**: The application provides an intuitive and easy-to-use interface powered by Streamlit.

## Installation

To run this application locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/gemini-llm-sql-query-generator.git
    cd gemini-llm-sql-query-generator
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory of the project and add your Google API key:
    ```env
    GOOGLE_API_KEY=your-google-api-key
    ```

5. **Run the application**:
    ```bash
    streamlit run app.py
    ```

6. **Access the application**:
   Open your web browser and go to `http://localhost:8501`.

## Project Structure

- **app.py**: The main application file where the Streamlit app is built.
- **student.db**: The SQLite database file containing the student records.
- **requirements.txt**: A list of Python packages required to run the application.
- **.env**: A file to store environment variables (e.g., API keys).

## Usage

1. **Enter a question**: Type your natural language question in the input box (e.g., "What is the average marks of section A?").
2. **Submit the question**: Click the "Ask your question" button to generate and execute the SQL query.
3. **View results**: The SQL query and its results will be displayed on the screen.
4. **View the entire table**: You can also view the entire contents of the database table by checking the "Show the entire STUDENT table" checkbox.

## Example Questions

- How many students are in the Data Science class?
- What are the names of students in section B?
- What is the average marks for each class?

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue to discuss any changes.





