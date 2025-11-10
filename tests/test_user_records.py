import pytest
from services.library_service import get_patron_status_report
import database
from os import remove

database.init_database()
database.add_sample_data()

def test_user_records_valid_input():
    borrowed_books, total_fee, borrowed_count, records = get_patron_status_report("123456")
    if not borrowed_books and not records:
        success = False
    else:
        success = True
    assert success == True

def test_user_records_patron_id_not_exist():
    borrowed_books, total_fee, borrowed_count, records = get_patron_status_report("654321")
    if not borrowed_books and not records:
        success = False
    else:
        success = True
    assert success == False

def test_user_records_patron_id_too_short():
    borrowed_books, total_fee, borrowed_count, records = get_patron_status_report("12345")
    if not borrowed_books and not records:
        success = False
    else:
        success = True
    assert success == False

def test_user_records_patron_id_too_long():
    borrowed_books, total_fee, borrowed_count, records = get_patron_status_report("1234567")
    if not borrowed_books and not records:
        success = False
    else:
        success = True
    assert success == False

# This deletes the test database file created at the start of the script file.
#remove("library.db")