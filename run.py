from app import app

if __name__ == '__main__':
    app.run(
        debug = True,
        port = app.config['PORT'],
        host = app.config['BASE_URL']
    )
