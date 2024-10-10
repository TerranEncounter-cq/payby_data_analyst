import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Database connection parameters
db_params = {
    'dbname': 'payby',
    'user': 'postgres',
    'password': '2458',
    'host': 'localhost',
    'port': '5432'
}

# get all dish names from the database
def get_all_dish_names_and_save_to_file(file_path):
    query = """
    SELECT DISTINCT jsonb_array_elements(items)->>'name' AS dish_name
    FROM core_ticket
    WHERE items IS NOT NULL;
    """
    conn = psycopg2.connect(**db_params)
    
    try:
        df = pd.read_sql(query, conn)
        dish_names = df['dish_name'].dropna().unique().tolist()

        # Writing the dish names to a .txt file with UTF-8 encoding
        with open(file_path, 'w', encoding='utf-8') as file:
            for dish_name in dish_names:
                file.write(f"{dish_name}\n")
        print(f"Dish names successfully written to {file_path}")

    except psycopg2.Error as e:
        print(f"Database error: {e}")
        dish_names = []
    finally:
        conn.close()

    return dish_names

# Example usage:
file_path = 'all_dish_names.txt'
get_all_dish_names_and_save_to_file(file_path)