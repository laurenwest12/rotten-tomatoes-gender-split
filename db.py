import psycopg2
from config import DB,DB_USER, DB_PASS, DB_PORT

conn = psycopg2.connect(dbname=DB,user=DB_USER,password=DB_PASS,host='localhost', port=DB_PORT)
cursor = conn.cursor()

def create_table(table, fields):
    sql=f'''CREATE TABLE {table}
           ({fields})'''
    cursor.execute(sql)
    conn.commit()

def insert_row(table, dict):
    name = dict.get('name')
    gender = dict.get('gender')
    probability = dict.get('probability')
    count = dict.get('count')
    
    cursor.execute(f'''INSERT INTO "{table}"(name, gender, probability, count) VALUES('{name}','{gender}',{probability},{count})''')
    conn.commit()

def find_row(table, name):
    cursor.execute(f'''SELECT * FROM {table} WHERE name = '{name}' ''')
    rows = cursor.fetchall()
    print(rows)

# create_table('name_data', '''name CHAR(50) NOT NULL, gender CHAR(50), probability FLOAT, count INT''')
# insert_row('name_data', {
#     "name": "peter",
#     "gender": "male",
#     "probability": 0.99,
#     "count": 165452
# })

# find_row('name_data', 'lauren')