from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        os.system("/var/www/html/deploy.sh")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Deployed")

server = HTTPServer(("0.0.0.0", 9000), Handler)
server.serve_forever()
