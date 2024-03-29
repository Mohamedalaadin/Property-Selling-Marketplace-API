from flask import Blueprint, jsonify
from app.services.user_service import UserService

# Define the blueprint
bp = Blueprint('common', __name__)

@bp.route('/users', methods=['GET'])
def get_all_users():
    try:
        users_list = UserService.get_all_users()
        return jsonify(users_list), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'message': str(e)}), 500

#route: View Property Details
@bp.route('/properties/<int:property_id>', methods=['GET'])
def view_property_endpoint(property_id):
	"""
	Endpoint to retrieve and view details of a specific property by its ID.

	:param property_id: The ID of the property to view.
	:type property_id: int

	:return: On success, returns a JSON representation of the property details,
			including its location, number of rooms, price, and status. On failure,
			returns a JSON object with an error message.
	:rtype: flask.Response
	"""

	try:
		property_details = UserService.view_property(property_id)
		return jsonify(property_details), 200
	except Exception as e:
		print(f"Error: {e}")
		return jsonify(message=str(e)), 500

