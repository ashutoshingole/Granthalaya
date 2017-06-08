import inspect
import os
import requests
import urllib
import keys
import parsing_json
import parsing_xml


# _Author_ = 'Ashutosh Ingole'


def get_book_rating_and_info_and_genre(isbn):
    goodreads_book_id, goodreads_book_rating = get_book_id_and_rating(isbn)
    book_description, author_id, author_image_url = get_book_description_author_id_image_url(goodreads_book_id)
    genre = get_book_genre_from_isbndb(isbn)
    return [goodreads_book_rating, book_description, genre, author_id, author_image_url]


def get_author_info_and_image(author_id, author_name, image_url):

    url = "https://www.goodreads.com/author/show.xml?key=i2RVLibRXKLkwrd7fjyT9g&id=" + str(author_id)
    response = requests.get(url)
    response_string = response.content
    beg_index = response_string.find("<about><![CDATA[") + 1
    end_index = response_string.find("]]></about>")
    author_info = response_string[beg_index:end_index].replace('<br />', '\n')
    current_file = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    filename = current_file + "/Author_Images/" + author_name + ".jpg"
    urllib.urlretrieve(image_url, filename)
    return author_info


def get_book_id_and_rating(isbn):
    url = "https://www.goodreads.com/book/review_counts.json?key=" + keys.goodreads + "&isbns=" + isbn
    response = requests.get(url)
    return parsing_json.get_book_id_rating_from_json_response(response)


def get_book_description_author_id_image_url(goodreads_book_id):
    url = "https://www.goodreads.com/book/show.xml?key=" + keys.goodreads + "&id=" + str(goodreads_book_id)
    response = requests.get(url)
    response_xml_string = response.content
    return parsing_xml.get_book_description_author_id_image_url_from_xml(response_xml_string)


def get_book_genre_from_isbndb(isbn):
    url = "http://isbndb.com/api/books.xml?access_key=" + keys.isbndb + \
          "&results=subjects&index1=isbn&value1=" + isbn
    response = requests.get(url)
    response_xml_string = response.content
    return parsing_xml.get_book_genre_from_xml(response_xml_string)
