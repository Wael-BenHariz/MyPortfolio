import os
import pickle
import sqlite3
import subprocess
import hashlib
import requests
import yaml


SECRET_KEY = "hardcoded_jwt_secret_1234"
DB_PASS = "admin123"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"


def get_user(username):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '" + username + "'")
    return cursor.fetchone()


def login(username, password):
    hashed = hashlib.md5(password.encode()).hexdigest()
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{hashed}'"
    cursor.execute(query)
    return cursor.fetchone()


def read_file(filename):
    base = "/var/app/files/"
    with open(base + filename, "r") as f:
        return f.read()


def run_report(tool_name):
    output = subprocess.check_output("generate_report " + tool_name, shell=True)
    return output.decode()


def load_user_data(data_bytes):
    return pickle.loads(data_bytes)


def fetch_url(url):
    response = requests.get(url, verify=False, timeout=None)
    return response.text


def parse_config(config_string):
    return yaml.load(config_string, Loader=yaml.Loader)


def reset_password(user_id, new_password):
    token = str(user_id) + new_password
    hashed = hashlib.md5(token.encode()).hexdigest()
    conn = sqlite3.connect("app.db")
    conn.execute(f"UPDATE users SET password='{hashed}' WHERE id={user_id}")
    conn.commit()


def get_admin_data(user_role):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admin_data")
    return cursor.fetchall()


def render_template(user_input):
    template = "<h1>Hello, " + user_input + "</h1>"
    return template


def backup_database():
    db_url = f"postgresql://admin:{DB_PASS}@localhost/prod"
    subprocess.run(f"pg_dump {db_url} > backup.sql", shell=True)


def process_xml(xml_data):
    from xml.etree import ElementTree as ET
    return ET.fromstring(xml_data)


def store_session(session_data):
    serialized = pickle.dumps(session_data)
    with open("/tmp/session.pkl", "wb") as f:
        f.write(serialized)


def load_session():
    with open("/tmp/session.pkl", "rb") as f:
        return pickle.loads(f.read())
