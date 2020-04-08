from app import app, db
from app.models import Store, Book

if __name__ == '__main__':
    app.run(port=8080, debug=True)