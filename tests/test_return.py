import pytest
from services.library_service import return_book_by_patron, borrow_book_by_patron
import database
from os import remove

database.init_database()
database.add_sample_data()

def test_return_valid_input():
    success, message = return_book_by_patron("123456", 3)
    assert success == True

def test_return_no_books_checked_out():
    success, message = return_book_by_patron("123456", 3)
    assert success == False
    # Re-borrow the book so the remaining tests will work
    borrow_book_by_patron("123456", 3)

def test_return_invalid_patron_id():
    test_patron_id = "1234567"
    success, message = return_book_by_patron(test_patron_id, 3)
    assert success == False

def test_return_invalid_book_id():
    test_book_id = 4
    success, message = return_book_by_patron("123456", test_book_id)
    assert success == False
    assert success == False

# This deletes the test database file created at the start of the script file.
remove("library.db")