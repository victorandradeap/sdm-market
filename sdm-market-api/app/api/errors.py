from flask import jsonify
from app.api import bp
from app.services.user_service import UserAlreadyExistsError

class NotFoundError(Exception):
    pass

class ValidationError(Exception):
    pass

@bp.app_errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not found'}), 404

@bp.app_errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

@bp.app_errorhandler(NotFoundError)
def handle_not_found_error(error):
    return jsonify({'error': str(error)}), 404

@bp.app_errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({'error': str(error)}), 400

@bp.app_errorhandler(UserAlreadyExistsError)
def handle_user_already_exists_error(error):
    return jsonify({'error': str(error)}), 409
