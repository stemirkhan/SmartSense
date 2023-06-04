from config import SERVER_HOST, SERVER_PORT, PATH_CERTIFICATE, PATH_PRIVATE_KEY
from log import server_logger

from http.server import HTTPServer
from handler import HTTPRequestHandler
from ssl import SSLContext, PROTOCOL_TLS_SERVER


if __name__ == '__main__':
    try:
        httpd = HTTPServer((SERVER_HOST, SERVER_PORT), HTTPRequestHandler)
        sslctx = SSLContext(PROTOCOL_TLS_SERVER)
        sslctx.load_cert_chain(certfile=PATH_CERTIFICATE, keyfile=PATH_PRIVATE_KEY)
        httpd.socket = sslctx.wrap_socket(httpd.socket, server_side=True)
        httpd.serve_forever()
    except Exception:
        server_logger.exception("Error server startup")
