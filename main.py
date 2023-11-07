import pymongo
from http.server import HTTPServer, BaseHTTPRequestHandler

class CustomHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write('Hello Motherfucker'.encode())
        
        client = pymongo.MongoClient("mongodb://root:123456@localhost:27017")

    def main():
        PRT = 8000
        srv = HTTPServer(('',PRT), CustomHandler)
        print('Server está rodando na porta %s' %PRT)
        srv.serve_forever()
    

if __name__ == '__main__':
    CustomHandler.main()