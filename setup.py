import sys

from app import create_app
from flask_script import Manager
from flask_twisted import Twisted
from twisted.python import log

if __name__ == '__main__':
    app = create_app()

    twisted = Twisted(app)
    log.startLogging(sys.stdout)

    app.logger.info(f'Running the app...')

    manazer = Manager(app)
    manazer.run()
