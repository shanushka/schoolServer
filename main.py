import os
import config
from flask import Flask

from models.base_model import db
from controller import api_blueprint
from utils.custom_json_encoder import CustomJSONEncoder

def createApp():
    app = Flask(__name__)
    # takes the environment from system.env file
    if os.environ.get('ENV') == 'testing':
        #sets ths appication configuration
        app.config.from_object(config.TestConfig)
    elif os.environ.get('ENV') == 'production':
        app.config.from_object(config.ProductionConfig)
    else :
        app.config.from_object(config.DevelopmentConfig)

    app.json_encoder = CustomJSONEncoder
    app.register_blueprint(api_blueprint,url_prefix='/api')

    db.init_app(app)
    @app.route("/")
    def main():
        return "School Records"

    return app


if __name__ == '__main__':
    app = createApp()
    print(app.config.get('PORT'))
    app.run(host=app.config.get('HOST'), port=app.config.get('PORT'))
