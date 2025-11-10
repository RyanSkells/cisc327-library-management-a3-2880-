import pytest
from services.library_service import search_books_in_catalog
import database
from os import remove

database.init_database()
database.add_sample_data()

def test_search_by_title_valid_input():
    success = search_books_in_catalog("great", "title")

    if success:
        assert True
    else:
        assert False

def test_search_by_author_valid_input():
    success = search_books_in_catalog("fitz", "author")

    if success:
        assert True
    else:
        assert False
def test_search_by_isbn_valid_input():
    success = search_books_in_catalog("9780743273565", "isbn")

    if success:
        assert True
    else:
        assert False
def test_search_invalid_title():
    success = search_books_in_catalog("100984", "title")

    if not success:
        assert True
    else:
        assert False

def test_search_invalid_author():
    success = search_books_in_catalog("George Orwellington", "author")

    if not success:
        assert True
    else:
        assert False
def test_search_invalid_isbn():
    success = search_books_in_catalog("50", "isbn")

    if not success:
        assert True
    else:
        assert False

# This deletes the test database file created at the start of the script file.
remove("library.db")