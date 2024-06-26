import http.server
import socketserver

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def do_bubble_sort():
    sample_list = [64, 34, 25, 12, 22, 11, 90, 25, 44, 34, 55, 63, 62, 74, 77, 22, 21, 14, 203, 102, 304, 312, 403, 445, 500, 512, 2, 48,
                   44, 67, 83, 90, 99, 55, 77, 88, 80, 84, 36, 47, 66, 103, 999, 506, 9993, 1003, 1022, 4445, 5503, 1103, 2204, 4403, 33, 223, 445,
                   3636, 88484, 8889, 2535, 373838, 92929, 282828, 3939, 62763, 732732, 646, 35337, 282829, 66, 663, 21, 43, 45, 41, 42, 654, 448, 990,
                   773, 756, 83, 748449, 82844, 27474, 73636, 738484, 8383, 34747, 4374743, 47, 636, 38384
                   ]
    sorted_list = bubble_sort(sample_list)
    return str(sorted_list)

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response_content = "<html><body><h1>Hello, world!</h1><p>" + do_bubble_sort() +"</p></body></html>"
        self.wfile.write(response_content.encode('utf-8'))

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
