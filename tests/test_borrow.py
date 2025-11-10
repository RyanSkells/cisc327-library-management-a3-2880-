import pytest
from services.library_service import borrow_book_by_patron
import database
from os import remove

database.init_database()
database.add_sample_data()

# Test Patron ID input
def test_catalog_patron_id_valid_input():
    success, message = borrow_book_by_patron("123456", 1)
    assert success == True
    assert "successfully borrowed" in message.lower()
def test_catalog_patron_id_too_short():
    test_patron_id = "12345"
    success, message = borrow_book_by_patron(test_patron_id, 1)
    assert success == False
    assert "invalid patron id" in message.lower()
def test_catalog_patron_id_too_long():
    test_patron_id = "1234567"
    success, message = borrow_book_by_patron(test_patron_id, 1)
    assert success == False
    assert "invalid patron id" in message.lower()
# Test Borrow Limit
def test_catalog_borrow_limit():
    borrow_book_by_patron("123456", 1)
    borrow_book_by_patron("123456", 1)
    borrow_book_by_patron("123456", 2)
    success, message = borrow_book_by_patron("123456", 2)
    assert success == False
    assert "borrowing limit" in message.lower()
# This deletes the test database file created at the start of the script file.
remove("library.db")

