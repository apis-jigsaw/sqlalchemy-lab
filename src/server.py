from app import create_app, db
from app.models import Bartender

app = create_app()

def make_shell_context():
    return {'db': db, 'Bartender': Bartender}