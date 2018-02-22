# gevent-redis-server
A python redis server using gevent

## Install
```
pip install .
```

## Example
```python
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
```

In order to add new command, you need to do 2 things:

1. define a method that represent the logic of your command
2. register the command and the callback using `register_command`

The method needs to accepts 2 arguments, `request` and `response`.

- `request` is a list that contains the command name as first item and the optional extra arguments of the command in the rest of the list.
- `response` is an object that has 3 methods that you need to use to rend response to the client
     - status: to send some status back to the client
     - error: to notify an error
     - encode: to write any type of data