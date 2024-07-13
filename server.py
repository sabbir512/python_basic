from http.server import SimpleHTTPRequestHandler, HTTPServer

server_address = ("", 8000)

httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print(f"Server is running in {server_address} port")

httpd.serve_forever()