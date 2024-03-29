from flask import Blueprint, request, jsonify
from app.services.buyer_service import BuyerService

bp = Blueprint('search', __name__)

@bp.route('properties/search', methods=['GET'])
def search_properties_endpoint():
	"""
	Endpoint for searching properties based on filters.
	"""
	# Filters are passed as query parameters, E.g,/search?location=city&min_price=100000
	filters = request.args.to_dict()

	# Convert numeric filters from string to their appropriate types
	if 'num_rooms' in filters:
		filters['num_rooms'] = int(filters['num_rooms'])
	if 'min_price' in filters:
		filters['min_price'] = float(filters['min_price'])
	if 'max_price' in filters:
		filters['max_price'] = float(filters['max_price'])

	properties = BuyerService.search_properties(filters)

	properties_list = [property.to_dict() for property in properties]

	return jsonify(properties=properties_list)