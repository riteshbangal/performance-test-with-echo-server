from http.server import HTTPServer, SimpleHTTPRequestHandler
import logging

class MyHandler(SimpleHTTPRequestHandler):
    protocol_version = 'HTTP/1.0'

    def do_GET(self):
        # Customize the response for a GET request
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = b"Custom Server Response: Hello, client!"
        self.wfile.write(response)
        self.log_message('Request received and served: %s', self.requestline)
        logging.info('Request received and served: %s', self.requestline)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    with HTTPServer(('0.0.0.0', 8080), MyHandler) as httpd:
        logging.info("Server listening on 0.0.0.0:8080")
        httpd.serve_forever()
