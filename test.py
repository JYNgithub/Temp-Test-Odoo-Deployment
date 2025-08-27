import os

admin_passwd = os.environ.get('ADMIN_PASSWD')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')
db_sslmode = os.environ.get('DB_SSLMODE')

"""
python3 odoo-bin --db_host="$DB_HOST" --db_port="$DB_PORT" --db_user="$DB_USER" --db_password="$DB_PASSWORD" --database="$DB_NAME" --db_sslmode="$DB_SSLMODE"
"""