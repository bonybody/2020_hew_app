from api.controllers import index, user, test, item


def register_controller_blueprint(app):
    app.register_blueprint(index.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(test.bp)
    app.register_blueprint(item.bp)
