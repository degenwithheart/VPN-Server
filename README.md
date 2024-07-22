# VPN Server

## Overview

This is a basic VPN server setup that listens for incoming VPN connections and routes traffic accordingly.

## File Structure

```plaintext
server/
│
├── server.py
└── config.py
```

## Prerequisites

- Python 3.8 or later
- Required Python libraries: `cryptography`, `dotenv`

## Setup

### 1. Install Dependencies

Ensure you have Python 3.8 or later installed. Install the required dependencies for the server:

```bash
pip install cryptography dotenv
```

### 2. Configure Server

Edit `server/config.py` to set your desired server configurations:

```python
SERVER_PORT = 8000
```

### 3. Run Server

Start the VPN server using:

```bash
python server/server.py
```

## Usage

The server listens for incoming VPN connections and routes traffic accordingly. Ensure it is running before starting the client.

## Troubleshooting

- **Connection Issues**: Ensure the server is using the correct IP addresses and ports. Verify that the server is running and properly configured.
- **Dependency Errors**: Ensure all required Python packages are installed. Use `pip` to install any missing dependencies.

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome to improve the VPN system or add new features.

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details. 
