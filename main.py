import streamlit as st
import pandas as pd
import numpy as np

# Allow user to upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# If a file was uploaded
if uploaded_file is not None:

    # Read CSV file
    df = pd.read_csv(uploaded_file)

    st.write(df)

    # Allow user to choose a preprocessing task
    task = st.selectbox("Select a preprocessing task", ["Not-Selected", "Data Cleaning"])

    if task == "Not-Selected":
        st.write("Please select a task to continue")
    # If the user chose "Data Cleaning"
    elif task == "Data Cleaning":
        null_values = ["-", "--", "---", "n/a", "N/A", "NA", "na", "nan", "NaN", "null", "Null", "NULL", "#N/A", "#N/A N/A", "#NA", "#REF!", "#VALUE!", "?", "None", "none", "", " ", "inf", "-inf", ".", "..", "...", "....", "......"]

        columns = ["Not-Selected"] + df.columns.tolist()
    
        # Allow user to choose a column
        column = st.selectbox("Choose a column", columns)

        if not(column == "Not-Selected"):

            # Display unique values in the selected column
            unique_values = df[column].unique()
            st.write(f"Unique values in column {column}:")
            st.write(str(unique_values))
            print(unique_values)

            # Display number of null values in the selected column
            df = df.replace(null_values, np.nan)
            null_values_count = df[column].isnull().sum()

            if null_values_count > 0:
                missing_data_options = ["Not-Selected", "Drop rows with missing data", "Drop columns with missing data", "Replace missing data with a specific value"]
                st.write(f"Number of null values in column {column}: {null_values_count}")

                # Allow user to choose an option for handling missing data
                missing_data_option = st.selectbox("Select an option for handling missing data", missing_data_options)

                if missing_data_option == "Not-Selected":
                    st.write("Select a option to deal with missing values")
                elif missing_data_option == "Drop rows with missing data":
                    df = df.dropna(subset=[column])
                    st.write("Rows with missing data dropped.")
                    st.write(df)
                elif missing_data_option == "Drop columns with missing data":
                    df = df.drop(columns=[column])
                    st.write("Column with missing data dropped.")
                    st.write(df)
                elif missing_data_option == "Replace missing data with a specific value":
                    replace_value = st.text_input("Enter a value to replace missing data with")
                    df[column] = df[column].fillna(replace_value)
                    st.write(f"Missing values in column {column} replaced with {replace_value}.")
                    st.write(df)
                else:
                    st.write("No missing data found in selected column.")
        else:
            st.write("Please select a column")
