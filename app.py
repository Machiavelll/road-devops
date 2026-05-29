from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"It works!!")

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), SimpleHandler)
    server.serve_forever()   