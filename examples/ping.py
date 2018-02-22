"""
Example redis server that only implements PING command
"""

from gedis import RedisServer
import logging


def ping(request, response):
    response.encode("PONG")

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    server = RedisServer()
    server.register_command('PING', ping)
    server.start()
