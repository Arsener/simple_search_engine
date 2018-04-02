#!/usr/bin/env python
import os
from app import create_app
from flask_script import Manager, Shell


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

key =os.urandom(24)
app.config['SECRET_KEY'] = key
manager = Manager(app)


def make_shell_context():
    return dict(app=app)
manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()

