from flask import Flask, request, Response
import requests
from cachetools import TTLCache
import json

cache = TTLCache(maxsize=100, ttl=300)

def start_server(port, origin):
    app = Flask(__name__)

    @app.route('/', defaults={'path': ''}, methods=['GET'])
    @app.route('/<path:path>', methods=['GET'])
    def proxy(path):
        cache_key = request.full_path
        
        if cache_key in cache:
            cached_response = cache[cache_key]
            response = Response(cached_response.data, cached_response.status_code, cached_response.headers)
            response.headers['X-Cache'] = 'HIT'
        else:
            url = f'{origin}/{path}'
            upstream_response = requests.get(url, params=request.args)
            response = Response(upstream_response.content, upstream_response.status_code, upstream_response.headers.items())
            response.headers['X-Cache'] = 'MISS'
            cache[cache_key] = response
        
        print(response.headers['X-Cache'])

        # try:
        #     response_data = json.loads(response.get_data(as_text=True))
        #     pretty_json = json.dumps(response_data, indent=4)
        #     print(pretty_json)
        # except json.JSONDecodeError:
        #     print("Response is not in JSON format")

        return response

    app.run(port=port)

def clear_cache():
    cache.clear()
    print('Cache cleared')
