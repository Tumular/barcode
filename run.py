from src.main.server.server import app

if __name__ == "__main__":
    print('ola mundo')
    app.run(host='0.0.0.0', port=3000, debug=True)
