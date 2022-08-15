"""
Sudoku API /health_check endpoint.
"""
from flask_restx import Resource, fields
from ..restplus import api
from loggings import get_module_logger

log = get_module_logger(__name__)

ns = api.namespace('health_check', description='Health monitoring')

health_status = api.model(
    'Health Status', {
        'status':
        fields.String(
            required=True, readOnly=True, description='Health status')
    })


@ns.route('')
class Health(Resource):
    @ns.marshal_with(health_status)
    def get(self):
        """Return service health status."""
        log.info(f'GET /health_check')
        return {'status': 'healthy'}, 200