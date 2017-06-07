import json


def get_book_id_rating_from_json_response(response):
    json_data = json.loads(response.text)
    goodreads_book_id = json_data['books'][0]['id']
    goodreads_book_rating = json_data['books'][0]['average_rating']
    return goodreads_book_id, goodreads_book_rating