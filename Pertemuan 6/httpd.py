import socket
import os
import mimetypes
from template import Template
from urllib.parse import unquote

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

sessions = {}


def tcp_server():
	SERVER_HOST = '127.0.0.1'
	SERVER_PORT = 9090
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind((SERVER_HOST, SERVER_PORT))
	server_socket.listen()
	print('='*50)
	print('Server Running!')
	print('='*50)
	print(f'Home: http://{SERVER_HOST}:{SERVER_PORT}/')
	print(f'Admin: http://{SERVER_HOST}:{SERVER_PORT}/admin/')
	print(f'Login: username={ADMIN_USERNAME}, password={ADMIN_PASSWORD}')
	print('='*50)
	while True:
		client_connection, client_address = server_socket.accept()
		request = client_connection.recv(8192).decode('utf-8', errors='ignore')
		if request and request.strip():
			print(f'Request from {client_address[0]}: {request.split(chr(13))[0]}')
			response = handle_request(request)
			client_connection.sendall(response)
		client_connection.close()
	server_socket.close()


def handle_request(request):
	request_message = str(request).split("\r\n")
	request_line = request_message[0]
	words = request_line.split()
	method = words[0]
	uri = words[1]
	http_version = words[2]
	
	headers = {}
	for line in request_message[1:]:
		if ': ' in line:
			key, value = line.split(': ', 1)
			headers[key.lower()] = value
	
	cookies = {}
	if 'cookie' in headers:
		for cookie in headers['cookie'].split('; '):
			if '=' in cookie:
				key, value = cookie.split('=', 1)
				cookies[key] = value
	
	if method == 'GET':
		response = handle_get(uri, http_version, cookies)
	elif method == "POST":
		data = request_message[len(request_message)-1]
		response = handle_post(uri, http_version, data, cookies)
	else:
		response = create_response(http_version, 405, "Method Not Allowed", b"<h1>405 Method Not Allowed</h1>")
	return response


def resolve_path(uri):
	original_uri = uri
	uri = uri.split('?')[0]
	
	if uri == "/admin" or uri == "/admin/":
		return ("file", "admin/index.html")
	
	if uri.startswith("/admin/"):
		return ("file", uri[1:])
	
	if uri.startswith("/home/"):
		return ("file", uri[1:])
	
	uri = uri.strip("/")
	
	if uri == "" or uri == "home" or uri == "home/":
		return ("file", "home/index.html")
	if uri == "login":
		return ("login", "home/index.html")
	if uri.startswith("admin"):
		return ("file", uri)
	if not uri.startswith("home/"):
		return ("file", "home/" + uri)
	return ("file", uri)


def create_response(http_version, status_code, status_text, message_body, content_type=b'text/html', extra_headers=None):
	response_line = f'{http_version} {status_code} {status_text}'.encode()
	if isinstance(content_type, str):
		content_type = content_type.encode()
	headers = [b'Content-type: ' + content_type]
	if extra_headers:
		for h in extra_headers:
			if isinstance(h, str):
				headers.append(h.encode())
			else:
				headers.append(h)
	crlf = b'\r\n'
	response = response_line + crlf + crlf.join(headers) + crlf + crlf + message_body
	return response


def create_redirect(http_version, location):
	response_line = f'{http_version} 302 Found'.encode()
	headers = f'Location: {location}'.encode()
	crlf = b'\r\n'
	return response_line + crlf + headers + crlf + crlf


def handle_get(uri, http_version, cookies):
	result = resolve_path(uri)
	
	if result[0] == "redirect":
		return create_redirect(http_version, result[1])
	
	file_path = os.path.join(BASE_DIR, result[1])
	
	if os.path.exists(file_path) and not os.path.isdir(file_path):
		content_type = mimetypes.guess_type(file_path)[0] or 'text/html'
		file = open(file_path, 'rb')
		message_body = file.read()
		file.close()
		return create_response(http_version, 200, "OK", message_body, content_type)
	else:
		return create_response(http_version, 404, "Not Found", b'<h1>404 Not Found</h1>')


def handle_post(uri, http_version, data, cookies):
	result = resolve_path(uri)
	
	if result[0] == "redirect":
		return create_redirect(http_version, result[1])
	
	_POST = {}
	for i in data.split("&"):
		if "=" in i:
			x = i.split("=", 1)
			_POST[x[0]] = unquote(x[1].replace('+', ' '))
	
	if result[0] == "login" or uri.strip('/') == "login":
		username = _POST.get('username', '')
		password = _POST.get('password', '')
		
		if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
			import hashlib
			import time
			session_id = hashlib.md5(f"{username}{time.time()}".encode()).hexdigest()
			sessions[session_id] = {'username': username, 'logged_in': True}
			
			extra_headers = [f'Set-Cookie: session_id={session_id}; Path=/']
			redirect_html = b'''<!DOCTYPE html>
<html>
<head>
<meta http-equiv="refresh" content="0;url=/admin/">
<title>Login Successful</title>
</head>
<body>
<h1>Login Successful!</h1>
<p>Redirecting to admin panel...</p>
<a href="/admin/">Click here if not redirected</a>
</body>
</html>'''
			return create_response(http_version, 200, "OK", redirect_html, 'text/html', extra_headers)
		else:
			error_html = b'''<!DOCTYPE html>
<html>
<head>
<title>Login Failed</title>
<style>
body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: #f5f5f5; }
.error-box { background: white; padding: 40px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); text-align: center; }
h1 { color: #e74c3c; }
a { color: #3498db; text-decoration: none; }
a:hover { text-decoration: underline; }
</style>
</head>
<body>
<div class="error-box">
<h1>Login Failed!</h1>
<p>Invalid username or password.</p>
<a href="/">Back to Home</a>
</div>
</body>
</html>'''
			return create_response(http_version, 401, "Unauthorized", error_html)
	
	file_path = os.path.join(BASE_DIR, result[1])
	
	if os.path.exists(file_path) and not os.path.isdir(file_path):
		content_type = mimetypes.guess_type(file_path)[0] or 'text/html'
		file = open(file_path, 'r')
		html = file.read()
		file.close()
		
		context = {
			'_POST' : _POST
		}
		t = Template(html)
		message_body = t.render(context).encode()
		return create_response(http_version, 200, "OK", message_body, content_type)
	else:
		return create_response(http_version, 404, "Not Found", b'<h1>404 Not Found</h1>')


if __name__ == "__main__":
	tcp_server()
