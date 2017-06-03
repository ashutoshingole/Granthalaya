import MySQLdb


def add_new_book_entry_to_db(book_info):
    db = MySQLdb.connect("localhost", port=3306, user="root", passwd="", db="Library")
    cursor = db.cursor()
    cursor.execute('INSERT INTO Books (title, author, genre, rating, ISBN, price, info) VALUES '
                   '(%s, %s, %s, %s, %s, %s, %s)', (book_info[0], book_info[1], book_info[6], float(book_info[4]),
                                                    book_info[2], int(book_info[3]), book_info[5]))
    db.commit()


def get_all_books_from_db():
    db = MySQLdb.connect("localhost", port=3306, user="root", passwd="", db="Library")
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Books')
    return cursor


def check_if_author_exist(author):
    db = MySQLdb.connect("localhost", port=3306, user="root", passwd="", db="Library")
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Authors WHERE name = %s', author)
    return len(cursor.fetchall())


def check_if_book_exist(book):
    db = MySQLdb.connect("localhost", port=3306, user="root", passwd="", db="Library")
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Books WHERE title = %s', book)
    return len(cursor.fetchall())


def add_author_info_to_db(author_name, author_info):
    db = MySQLdb.connect("localhost", port=3306, user="root", passwd="", db="Library")
    cursor = db.cursor()
    cursor.execute('INSERT INTO Authors (name, info) VALUES (%s, %s)', (author_name, author_info))
    db.commit()
