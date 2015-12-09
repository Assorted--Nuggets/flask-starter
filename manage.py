import os
from app import create_app, db
from app.models import User
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

basedir = os.path.abspath(os.path.dirname(__file__))

app = create_app('testing')
manager = Manager(app)
migrate = Migrate()
migrate.init_app(app, db, directory=os.path.join(basedir, 'migrations/'))

def make_shell_context():
    return dict(app=app, db=db, User=User)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests') 
    unittest.TextTestRunner(verbosity=3).run(tests)

if __name__ == '__main__': 
    manager.run()
