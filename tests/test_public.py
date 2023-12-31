import pytest

from lab6 import MyQueue, MyStack, Transactions


@pytest.mark.timeout(0.1)
def test_stack():
    my_stack = MyStack()
    assert my_stack.is_empty() is True
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    assert my_stack.__str__() == "3 -> 2 -> 1"
    assert my_stack.is_empty() is False
    assert my_stack.min() == 1
    assert my_stack.max() == 3
    assert my_stack.pop() == 3
    assert my_stack.__str__() == "2 -> 1"
    assert my_stack.min() == 1
    assert my_stack.max() == 2
    assert my_stack.pop() == 2
    assert my_stack.__str__() == "1"
    assert my_stack.min() == 1
    assert my_stack.max() == 1
    assert my_stack.pop() == 1
    assert my_stack.__str__() == ""
    assert my_stack.is_empty() is True

    with pytest.raises(Exception):
        my_stack.pop()
    assert my_stack.min() is None
    assert my_stack.max() is None


@pytest.mark.timeout(0.1)
def test_queue():
    my_queue = MyQueue()
    assert my_queue.is_empty() is True
    my_queue.push(1)
    my_queue.push(2)
    my_queue.push(3)
    assert my_queue.__str__() == "1 -> 2 -> 3"
    assert my_queue.is_empty() is False
    assert my_queue.min() == 1
    assert my_queue.max() == 3
    assert my_queue.pop() == 1
    assert my_queue.__str__() == "2 -> 3"
    assert my_queue.min() == 2
    assert my_queue.max() == 3
    assert my_queue.pop() == 2
    assert my_queue.__str__() == "3"
    assert my_queue.min() == 3
    assert my_queue.max() == 3
    assert my_queue.pop() == 3
    assert my_queue.__str__() == ""
    assert my_queue.is_empty() is True

    with pytest.raises(Exception):
        my_queue.pop()
    assert my_queue.min() is None
    assert my_queue.max() is None


@pytest.mark.timeout(0.1)
def test_transactions():
    transactions = Transactions()
    transactions.add_transaction(67686, "deposit", 5000, "Monthly Allowance")
    transactions.add_transaction(67687, "withdrawal", 200, "Phone bill")
    transactions.add_transaction(67688, "deposit", 1234.56, "Salary")

    with pytest.raises(Exception):
        transactions.add_transaction(67688, "deposit", 1234.56, "Salary")

    assert transactions.get_transaction(67686) == {
        "transaction_type": "deposit",
        "transaction_amount": 5000,
        "transaction_details": "Monthly Allowance",
    }
    assert transactions.get_transaction(67687) == {
        "transaction_type": "withdrawal",
        "transaction_amount": 200,
        "transaction_details": "Phone bill",
    }
    assert transactions.get_transaction(67688) == {
        "transaction_type": "deposit",
        "transaction_amount": 1234.56,
        "transaction_details": "Salary",
    }
    assert transactions.get_transaction(67689) == {}
    assert transactions.get_all_transactions() == {
        67686: {"transaction_type": "deposit", "transaction_amount": 5000, "transaction_details": "Monthly Allowance"},
        67687: {"transaction_type": "withdrawal", "transaction_amount": 200, "transaction_details": "Phone bill"},
        67688: {"transaction_type": "deposit", "transaction_amount": 1234.56, "transaction_details": "Salary"},
    }
