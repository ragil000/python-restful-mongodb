from pathlib import Path
from app import db, create_app
from helper import not_found_response

app = create_app(Path.cwd())
db.init_app(app)

count_request = 0

@app.before_request
def open_connection(exception=None):
    # db.disconnect()
    # db.connect()
    print('aaaaaaa')

@app.after_request
def after_request_func(response):
    global count_request
    print('ok!', count_request, response)
    # db.disconnect()
    count_request += 1
    return response

# @app.teardown_appcontext
# def close_connection(exception=None):
#     db.disconnect()
#     print('database close connection')

# url error handler
@app.errorhandler(404)
def not_found(error=None):
    response = not_found_response(url=request.url)
    return response
    
app.run()