from flask import Blueprint, jsonify

error= Blueprint('error', __name__)


@error.app_errorhandler(404)
def not_found(err):
    return jsonify({
        'success': False,
        'message': 'Resource Not Found',
        'error': 404
    }), 404


@error.app_errorhandler(405)
def not_allowed(err):
    return jsonify({
        'success': False,
        'error': 405,
        'message': "Method Not Allowed"
    }), 405


@error.app_errorhandler(422)
def unprocessable(err):
    return jsonify({
        'success': False,
        'error': 422,
        'message': "Unprocessable Request"
    }), 422


@error.app_errorhandler(500)
def server_damage(err):
    return jsonify({
        'success': False,
        'error': 500,
        'message': "Internal Server Error"
    }), 500


@error.app_errorhandler(400)
def bad_request(err):
    return jsonify({
        'success': False,
        'error': 400,
        'message': 'Bad Request'
    }), 400
