<div align="center">
    
  # Caching Proxy Server
  
  ![alt text](image.png)
  
  [Overview](#🎯-overview) •
  [Features](#✨-features) •
  [Getting Started](#🚀-getting-started) •
  [Usage](#📘-usage) •
  [API](#📚-api)
  
</div>
  
---

## 🎯 Overview

This project is a CLI tool that starts a caching proxy server. The server forwards requests to the actual server, caches the responses, and returns the cached response if the same request is made again. This reduces the load on the origin server and improves response times for repeated requests.

## ✨ Features

- **Request Forwarding**: Forwards requests to the specified origin server.
- **Response Caching**: Caches responses and returns them for repeated requests.
- **Cache Control**: Provides the ability to clear the cache via a CLI command.
- **Custom Headers**: Adds headers to indicate whether the response was served from the cache or fetched from the origin server.

## 🚀 Getting Started

To get a local copy up and running, follow these steps:

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Flask
- requests
- cachetools

You can install the required Python packages using pip:

```bash
pip install Flask requests cachetools
```

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/hamza-140/caching-server.git
    cd caching-proxy-server
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the server:

    ```bash
    python main.py start --port 3000 --origin http://dummyjson.com
    ```

## 📘 Usage

To start the caching proxy server, run the following command:

```bash
python main.py start --port <number> --origin <url>
```

- `--port`: The port on which the caching proxy server will run.
- `--origin`: The URL of the server to which the requests will be forwarded.

Example:

```bash
python main.py start --port 3000 --origin http://dummyjson.com
```

To clear the cache, run:

```bash
python main.py clear-cache
```

## 📚 API

### `start_server(port, origin)`

Starts the caching proxy server on the specified port and forwards requests to the origin server.

| Parameter | Type   | Description                        |
| --------- | ------ | ---------------------------------- |
| `port`    | Int    | The port on which the server runs. |
| `origin`  | String | The URL of the origin server.      |

### `clear_cache()`

Clears the cache of all stored responses.

**Returns**: `None`

## Example

```bash
python main.py start --port 3000 --origin http://dummyjson.com
```

This command starts the caching proxy server on port 3000. If you request `http://localhost:3000/products`, it will forward the request to `http://dummyjson.com/products`, cache the response, and return it. Subsequent requests to the same endpoint will be served from the cache.

```bash
python main.py clear-cache
```

This command clears the cached responses, so the next request will be forwarded to the origin server again.

## CC
https://roadmap.sh/projects/caching-server