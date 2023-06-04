import os

# SSL
PATH_CERTIFICATE = "./certificates/stations_server.crt"
PATH_PRIVATE_KEY = "./certificates/stations_server.key"

# Server
SERVER_PORT = 8888
SERVER_HOST = "0.0.0.0"

# Log
ERROR_SERVER_LOG_FILE = "./error_server.log"
ERROR_DB_LOG_FILE = "./error_db.log"
LOG_SIZE = 5  # Size in megabytes

# DB
SENSOR_READINGS_TABLE = os.getenv("SENSOR_READINGS_TABLE")
ACCESS_TOKEN_TABLE = os.getenv("ACCESS_TOKEN_TABLE")
USER_DB = os.getenv("USER_DB")
HOST_DB = os.getenv("HOST_DB")
PORT_DB = os.getenv("PORT_DB")
PASSWORD_DB = os.getenv("PASSWORD_DB")
DATABASE = os.getenv("DATABASE")
