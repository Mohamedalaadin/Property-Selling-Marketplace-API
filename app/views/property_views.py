from flask import request ,Blueprint, jsonify
from app import db
from app.services.property_owner_service import PropertyOwnerService


bp = Blueprint('property', __name__)

@bp.route('/properties', methods=['GET'])
def get_properties_list_endpoint():

	user_id = request.headers.get("X-User-Id")

	try:
		properties = PropertyOwnerService.view_properties_list(user_id)
		properties_list = [property.to_dict() for property in properties]
		return jsonify(properties= properties_list), 200
	except PermissionError as e:
		# Permission denied error handling
		return jsonify(message=str(e)), 403
	except Exception as e:
		print(f"Error: {e}")  # Or use logging.error(f"Error: {e}")
		return jsonify(message=str(e)), 500

@bp.route('/properties', methods=['POST'])
def add_property_endpoint():
	"""
	Endpoint to create a new property entry in the database.
	Note: As authorization was not part of the assignment requirements, the user ID is passed via the 'X-User-Id' header.

	:return: A JSON response with a success or error message.
	:rtype: flask.Response
	"""
	property_data = request.json
	user_id = request.headers.get("X-User-Id")

	try:
		# Pass the user_id and property_data to function add_property at the service layer
		PropertyOwnerService.add_property(user_id, property_data)
		return jsonify(message="Property added successfully"), 201
	except PermissionError as e:
		# Permission denied error handling
		return jsonify(message=str(e)), 403
	except Exception as e:
		print(f"Error: {e}")  # Or use logging.error(f"Error: {e}")
		return jsonify(message=str(e)), 500


@bp.route('/properties/<int:id>', methods=['PUT'])
def modify_property_endpoint(id):

	"""
	Endpoint to modify an existing property. Expects property data in the request JSON and the user ID in the request headers.
	Note: As authorization was not part of the assignment requirements, the user ID is passed via the 'X-User-Id' header.

	:param id: The ID of the property to modify. Must be the property owner.
	:type id: int

	:return: A JSON response with success or error message.
	:rtype: flask.Response
	"""
	property_data = request.json
	user_id = request.headers.get("X-User-Id")

	try:
		# Pass the user_id ,id and property_data to function modify_property at the service layer
		updated_property = PropertyOwnerService.modify_property(user_id, id, property_data)
		return jsonify(message=f"Property {updated_property.id} updated successfully"), 200
	except Exception as e:
		# Log the actual error message to your console or log file
		print(f"Error: {e}")  # Or use logging.error(f"Error: {e}")
		return jsonify(message=str(e)), 500

@bp.route('/properties/<int:id>', methods=['DELETE'])
def delete_property_endpoint(id):
	"""
	Endpoint to delete an existing property. Requires the user ID to be provided in the request headers.

	:param id: The ID of the property to delete.
	:type id: int

	:return: A JSON response with success or error message.
	:rtype: flask.Response
	"""

	user_id = request.headers.get("X-User-Id")

	try:
		PropertyOwnerService.delete_property(user_id, id)
		return jsonify(message=f"Property {id} deleted successfully"), 200
	except Exception as e:
		print(f"Error: {e}")
		return jsonify(message=str(e)), 500
