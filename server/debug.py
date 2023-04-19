from app import app
from models import db, Vocab, Favorite, User, ModuleContent

if __name__ == '__main__':
    with app.app_context():
        import ipdb; ipdb.set_trace()