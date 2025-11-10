#OLD VERSION FROM PREVIOUS SUBMISSION

import pytest
from services.library_service import calculate_late_fee_for_book, insert_borrow_record, insert_book
import database
from os import remove
from datetime import datetime, timedelta

database.init_database()
# borrow_date, due_date
def test_late_fee_zero_days():
    remove("library.db")
    database.init_database()
    # Generate dummy book for calculation to work
    insert_book("Test Book", "Test Author", "1234567890123", 5, 5)
    now = datetime.now()

    insert_borrow_record("123456", 1, now, now)
    fee_details = calculate_late_fee_for_book("123456", 1)
    assert fee_details['status'] == True
    assert fee_details['days_overdue'] <= 0
    assert fee_details['fee_amount'] == 0

def test_late_fee_seven_days():
    remove("library.db")
    database.init_database()
    # Generate dummy book for calculation to work
    insert_book("Test Book", "Test Author", "1234567890123", 5, 5)
    now = datetime.now()
    borrow_date = now - timedelta(days=7)
    due_date = borrow_date + timedelta(days=14)

    insert_borrow_record("123456", 1, borrow_date, due_date)
    fee_details = calculate_late_fee_for_book("123456", 1)
    assert fee_details['status'] == True
    assert fee_details['days_overdue'] <= 0
    assert fee_details['fee_amount'] == 0
def test_late_fee_fourteen_days():
    remove("library.db")
    database.init_database()
    # Generate dummy book for calculation to work
    insert_book("Test Book", "Test Author", "1234567890123", 5, 5)
    now = datetime.now()
    borrow_date = now - timedelta(days=14)
    due_date = borrow_date + timedelta(days=14)

    insert_borrow_record("123456", 1, borrow_date, due_date)
    fee_details = calculate_late_fee_for_book("123456", 1)
    assert fee_details['status'] == True
    assert fee_details['days_overdue'] == 0
    assert fee_details['fee_amount'] == 0

def test_late_fee_twentyone_days():
    remove("library.db")
    database.init_database()
    # Generate dummy book for calculation to work
    insert_book("Test Book", "Test Author", "1234567890123", 5, 5)
    now = datetime.now()
    borrow_date = now - timedelta(days=21)
    due_date = borrow_date + timedelta(days=14)

    insert_borrow_record("123456", 1, borrow_date, due_date)
    fee_details = calculate_late_fee_for_book("123456", 1)
    assert fee_details['status'] == True
    assert fee_details['days_overdue'] == 7
    assert fee_details['fee_amount'] == 3.5

def test_late_fee_twentyeight_days():
    remove("library.db")
    database.init_database()
    # Generate dummy book for calculation to work
    insert_book("Test Book", "Test Author", "1234567890123", 5, 5)
    now = datetime.now()
    borrow_date = now - timedelta(days=28)
    due_date = borrow_date + timedelta(days=14)

    insert_borrow_record("123456", 1, borrow_date, due_date)
    fee_details = calculate_late_fee_for_book("123456", 1)
    assert fee_details['status'] == True
    assert fee_details['days_overdue'] == 14
    assert fee_details['fee_amount'] == 10.5
def test_late_fee_thirtyfive_days():
    remove("library.db")
    database.init_database()
    # Generate dummy book for calculation to work
    insert_book("Test Book", "Test Author", "1234567890123", 5, 5)
    now = datetime.now()
    borrow_date = now - timedelta(days=35)
    due_date = borrow_date + timedelta(days=14)

    insert_borrow_record("123456", 1, borrow_date, due_date)
    fee_details = calculate_late_fee_for_book("123456", 1)
    assert fee_details['status'] == True
    assert fee_details['days_overdue'] == 21
    assert fee_details['fee_amount'] == 15
# This deletes the test database file created at the start of the script file.
remove("library.db")

