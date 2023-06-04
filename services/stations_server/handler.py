from http.server import BaseHTTPRequestHandler
from utils import parse_request_client, validator_url_arguments
from config import *
from db import WorkerDB
from log import server_logger

db = WorkerDB(USER_DB, PASSWORD_DB, HOST_DB, PORT_DB, DATABASE)
db.create_table()


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        arguments = parse_request_client(self.path)

        if validator_url_arguments(arguments) and (arguments['access_token'] in db.get_access_tokens()):
            db.add_measurements(arguments['temperature'], arguments['pressure'],
                                arguments['carbonMonoxide'], arguments['humidity'])

            self.send_response(200, 'OK')

        else:
            self.send_response(401, 'invalid access_token')
            self.log_request(401, "invalid access_token")

        self.end_headers()

    def log_message(self, format_msg: str, *args) -> None:
        server_logger.info("%s - - [%s] %s\n" % (self.address_string(), self.log_date_time_string(), format_msg%args))
