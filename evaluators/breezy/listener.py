"""Simple HTTPServer and RequestHandler for communicating with Breezy server"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import json
import requests


class RequestHandler(BaseHTTPRequestHandler):
    """RequestHandler for communicating with Breezy server"""

    def _get_content(self):
        """Extract data from request"""
        length = int(self.headers.get('Content-Length'))
        return json.loads(self.rfile.read(length))

    def _respond(self, response):
        """Respond to request with given dictionary"""
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        self.wfile.write(str(response).encode("utf-8"))

    def do_GET(self):
        """Process GET requests"""
        self._respond(json.dumps({}))
        if self.path == '/':
            self._respond(json.dumps({}))

    def do_POST(self):
        """Process POST requests"""
        if self.path == '/':
            action = self.server.breezy_evaluator.callback(self._get_content())
            self._respond(json.dumps({"actionCode":action}))
        elif self.path == '/update':
            run_data = self._get_content()
            self.server.breezy_evaluator.game_done(run_data)
            if "webhook" in run_data:
                webhook_url = self.server.breezy_url + run_data['webhook']
                requests.get(webhook_url)
            else:
                self.server.running = False

    def log_message(self, format, *args):
        """Silence logging"""
        return

    @staticmethod
    def _print_features(features):
        indexed = [f'({i} - {feature})' for i, feature in enumerate(features)]
        print(' '.join(indexed))


class Listener:
    """HTTPServer for communicating with Breezy server"""
    def __init__(self, breezy_evaluator, address=('127.0.0.1', 8086),
                 breezy_url='http://127.0.0.1:8085'):
        self._server = HTTPServer(address, RequestHandler)
        self._server.breezy_url = breezy_url
        self._server.breezy_evaluator = breezy_evaluator
        self._thread = None
        self.agent_config = {
            'host': address[0],
            'port': address[1],
            'connect.route': '/',
            'relay.route': '/',
            'run.update.route': '/update',
        }
        self.run_count = 0

    def _run(self):
        start_data = {
            'agent': 'Agent',
            'size': self.run_count
        }
        requests.post(url=self._server.breezy_url+'/run/', data=json.dumps(start_data))
        self._server.running = True
        while self._server.running:
            self._server.handle_request()

    def start(self, run_count):
        """Start the runs"""
        self.run_count = run_count
        self._thread = threading.Thread(target=self._run)
        self._thread.daemon = True
        self._thread.start()
        requests.post(url=self._server.breezy_url+'/agent/config',
                      data=json.dumps(self.agent_config))

    def join(self):
        """Wait until runs finish"""
        self._thread.join()
