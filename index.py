import os
from dotenv import load_dotenv

load_dotenv(".env.pro")

user_name = os.getenv('USER_NAME')      #Se cargan las variables del entorno
api_key = os.getenv('API_KEY')
email = os.getenv('EMAIL')
database_url = os.getenv('DATABASE_URL')

print(f"USER_NAME:{user_name}")
print(f"API_KEY:{api_key}")
print(f"EMAIL:{email}")
print(f"DATABASE_URL:{database_url}")