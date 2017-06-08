import xml.etree.ElementTree as ET
import re


# _Author_ = 'Ashutosh Ingole'


def get_book_description_author_id_image_url_from_xml(response_xml_string):
    root = ET.fromstring(response_xml_string)
    book_description = None
    author_id = None
    author_image_url = None
    for book in root.findall('book'):
        book_description = book.find('description').text
        for author in root.findall('./book/authors/author'):
            author_id = author.find('id').text
            author_image_url = author.find('image_url').text
    book_description = remove_xml_string_tags(book_description)
    book_description = book_description.encode('utf8')
    return book_description, author_id, author_image_url


def get_book_genre_from_xml(response_xml_string):
    root = ET.fromstring(response_xml_string)
    genre = None
    for Subjects in root.findall('./BookList/BookData/Subjects'):
        genre = Subjects.find('Subject').text
    return genre


def remove_xml_string_tags(input_string):
    output_string = re.sub('<br />', '\n', input_string)
    output_string = re.sub('<.*?>', '', output_string)
    return output_string
