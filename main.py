import BaseHTTPServer
import SimpleHTTPServer
import json

def word_count(data) :
        """
        input:
          an array of words.
        output:
          {
            words: number,
            characters: number,
            vowels: number,
            consonants: number,
          }
        """
    
        words = 0
        characters = 0
        vowels = 0
        consonants = 0
        for each in data :
            words = words + 1
            for c in each :
                characters = characters + 1
                if c.isalpha() :
                    if c in 'aeiou' :
                        vowels = vowels + 1
                    else :
                        consonants = consonants + 1
        return {
            'words':      words,
            'characters': characters,
            'vowels':     vowels,
            'consonants': consonants
        }

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_POST(self) :
        """
        POST implements our word counter.
        """
        length = int(self.headers.getheader('content-length'))
        raw = self.rfile.read(length)
        print 'raw',raw
        data = json.loads(raw)
        print 'data',data
        response = word_count(data)
        print 'response',response
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response))
        

if __name__ == '__main__':
    address = ('', 8080)
    httpd = BaseHTTPServer.HTTPServer(address, Handler)
    print 'Starting httpd...'
    httpd.serve_forever()
