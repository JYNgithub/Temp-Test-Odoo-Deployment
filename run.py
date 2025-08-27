import os
import subprocess

cmd = [
    'python3', 'odoo-bin',
    '--db_host', os.environ.get('DB_HOST'),
    '--db_port', os.environ.get('DB_PORT', '5432'),
    '--db_user', os.environ.get('DB_USER'),
    '--db_password', os.environ.get('DB_PASSWORD'),
    '--database', os.environ.get('DB_NAME'),
    '--db_sslmode', os.environ.get('DB_SSLMODE', 'require')
]

subprocess.run(cmd)