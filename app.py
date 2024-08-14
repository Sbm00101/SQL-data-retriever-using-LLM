from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai
import pandas as pd

# Load environment variables
load_dotenv()

# Configure API
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))


# Function to load Gemini Model and provide query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([question, prompt])
    return response.text


# Function to retrieve results from the database
def read_sql_query(sql_query, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql_query)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows, [desc[0] for desc in cur.description]


# Function to retrieve and display the entire table as a DataFrame
def get_table_data(db):
    conn = sqlite3.connect(db)
    df = pd.read_sql_query("SELECT * FROM STUDENT", conn)
    conn.close()
    return df


# Defining prompt
prompt = """
You are an expert in converting English Questions to SQL queries. You retrieve the logic from official SQL documentation.
The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, and MARKS.
For example, 
Example1: How many records of entry are present?
The SQL query will be something like - SELECT COUNT(*) FROM STUDENT;

Example2: Tell me all the students studying in Data Science class.
The SQL query will be something like - SELECT * FROM STUDENT WHERE CLASS = 'Data Science';

Example3: Write an SQL query to find the average marks for each grade in each class, and display the results in descending order of average marks.
The SQL query will be like - 
SELECT CLASS, SECTION, AVG(MARKS) AS average_marks
FROM STUDENT
GROUP BY CLASS, SECTION
ORDER BY average_marks DESC;

Also, the SQL query shouldn't have ''' in the beginning or end and the sql word in the output and only generate the query.
"""

st.set_page_config(page_title="I can retrieve any SQL query")
st.header("Gemini LLM based App to retrieve SQL Data")

# Add the subheader below the main header
st.text("The application will generate SQL queries and extract data from the Dataset")

question = st.text_input("Input your question in English:", key="input")
submit = st.button("Ask your question")

# Display the entire table in tabular form
if st.checkbox("Show the entire STUDENT table"):
    table_df = get_table_data("student.db")
    st.subheader("STUDENT Table Data")
    st.dataframe(table_df)  # Displaying the table using a dataframe

# If submit is clicked
if submit:
    # Get the SQL query from the LLM
    sql_query = get_gemini_response(question, prompt)

    # Display the generated SQL query
    st.subheader("Generated SQL Query:")
    st.code(sql_query, language='sql')

    # Execute the SQL query and get the results
    data, columns = read_sql_query(sql_query, "student.db")

    st.subheader("Query Result:")
    if data:
        result_df = pd.DataFrame(data, columns=columns)  # Create DataFrame with dynamic columns
        st.dataframe(result_df)  # Displaying the query result in tabular form
    else:
        st.write("No results found for this query.")

