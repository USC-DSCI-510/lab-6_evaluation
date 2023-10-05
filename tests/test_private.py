import pytest

from lab6 import MyQueue, MyStack, Transactions


# Test MyStack
@pytest.mark.timeout(0.02)
def test_empty_stack_pop():
    stack = MyStack()
    with pytest.raises(Exception):
        stack.pop()


@pytest.mark.timeout(0.02)
def test_empty_stack_min_max():
    stack = MyStack()
    assert stack.min() is None
    assert stack.max() is None


@pytest.mark.timeout(0.02)
def test_negative_push_stack():
    stack = MyStack()
    stack.push(-5)
    assert stack.pop() == -5


@pytest.mark.timeout(0.02)
def test_large_push_stack():
    stack = MyStack()
    stack.push(10**10)
    assert stack.pop() == 10**10


@pytest.mark.timeout(0.2)
def test_not_allowed_dtype_push_stack():
    stack = MyStack()
    with pytest.raises(Exception):
        stack.push("Test String")

    # with pytest.raises(Exception):
    #     stack.push(True)

    with pytest.raises(Exception):
        stack.push(5.67)

    with pytest.raises(Exception):
        stack.push(stack)

    with pytest.raises(Exception):
        stack.push([1, 2, 3])

    with pytest.raises(Exception):
        stack.push({1, 2, 3})


@pytest.mark.timeout(0.02)
def test_push_and_pop_stack():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1


# Test MyQueue
@pytest.mark.timeout(0.02)
def test_empty_queue_pop():
    queue = MyQueue()
    with pytest.raises(Exception):
        queue.pop()


@pytest.mark.timeout(0.02)
def test_empty_queue_min_max():
    queue = MyQueue()
    assert queue.min() is None
    assert queue.max() is None


@pytest.mark.timeout(0.02)
def test_negative_push_queue():
    queue = MyQueue()
    queue.push(-5)
    assert queue.pop() == -5


@pytest.mark.timeout(0.02)
def test_large_push_queue():
    queue = MyQueue()
    queue.push(10**10)
    assert queue.pop() == 10**10


@pytest.mark.timeout(0.2)
def test_not_allowed_dtype_push_queue():
    queue = MyQueue()
    with pytest.raises(Exception):
        queue.push("Test String")

    with pytest.raises(Exception):
        queue.push(5.67)

    # with pytest.raises(Exception):
    #     queue.push(True)

    with pytest.raises(Exception):
        queue.push(queue)

    with pytest.raises(Exception):
        queue.push([1, 2, 3])

    with pytest.raises(Exception):
        queue.push({1, 2, 3})


@pytest.mark.timeout(0.02)
def test_push_and_pop_queue():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3


# Test Transactions
@pytest.mark.timeout(0.02)
def test_duplicate_transaction_id():
    transactions = Transactions()
    transactions.add_transaction(1, "deposit", 100, "Salary")
    with pytest.raises(Exception):
        transactions.add_transaction(1, "withdrawal", 50, "Groceries")


@pytest.mark.timeout(0.02)
def test_get_nonexistent_transaction():
    transactions = Transactions()
    assert transactions.get_transaction(100) == {}


@pytest.mark.timeout(0.02)
def test_get_existing_transaction():
    transactions = Transactions()
    transactions.add_transaction(1, "deposit", 100, "Salary")
    assert transactions.get_transaction(1) == {
        "transaction_type": "deposit",
        "transaction_amount": 100,
        "transaction_details": "Salary",
    }


@pytest.mark.timeout(0.02)
def test_get_all_transactions():
    transactions = Transactions()
    transactions.add_transaction(1, "deposit", 100, "Salary")
    transactions.add_transaction(2, "withdrawal", 50, "Groceries")
    assert transactions.get_all_transactions() == {
        1: {"transaction_type": "deposit", "transaction_amount": 100, "transaction_details": "Salary"},
        2: {"transaction_type": "withdrawal", "transaction_amount": 50, "transaction_details": "Groceries"},
    }


@pytest.mark.timeout(0.02)
def test_valid_transaction_types():
    transactions = Transactions()
    with pytest.raises(Exception):
        transactions.add_transaction(1, "DEPOSIT", 100, "Salary")
    with pytest.raises(Exception):
        transactions.add_transaction(2, "WITHDRAWAL", 50, "Groceries")


@pytest.mark.timeout(0.02)
def test_valid_transaction_id():
    transactions = Transactions()
    with pytest.raises(Exception):
        transactions.add_transaction("g89678gfBH6", "deposit", 100, "Salary")


@pytest.mark.timeout(0.05)
def test_transaction_system():
    # Initialize components
    stack = MyStack()
    queue = MyQueue()
    transactions = Transactions()

    # Add transactions
    transactions.add_transaction(1, "deposit", 100, "Salary")
    transactions.add_transaction(2, "withdrawal", 50, "Groceries")
    transactions.add_transaction(3, "withdrawal", 30, "Rent")

    # Push transaction IDs to stack and queue
    for transaction_id in transactions.get_all_transactions().keys():
        stack.push(transaction_id)
        queue.push(transaction_id)

    # Check if order is maintained in stack
    assert str(stack) == "3 -> 2 -> 1"

    # Check if order is maintained in queue
    assert str(queue) == "1 -> 2 -> 3"

    # Pop transaction IDs from stack and queue
    stack_popped = stack.pop()
    queue_popped = queue.pop()

    # Check if popped IDs are different
    assert stack_popped != queue_popped

    # Get transaction details using popped IDs
    transaction_details_stack = transactions.get_transaction(stack_popped)
    transaction_details_queue = transactions.get_transaction(queue_popped)

    # Check if transaction details are correct
    assert transaction_details_stack == {
        "transaction_type": "withdrawal",
        "transaction_amount": 30,
        "transaction_details": "Rent",
    }

    assert transaction_details_queue == {
        "transaction_type": "deposit",
        "transaction_amount": 100,
        "transaction_details": "Salary",
    }

    # Check min and max
    assert stack.min() == 1
    assert stack.max() == 2

    # Check if stack and queue are empty
    assert not stack.is_empty()
    assert not queue.is_empty()


@pytest.mark.timeout(0.05)
def test_transaction_system_advanced():
    # Initialize components
    stack = MyStack()
    queue = MyQueue()
    transactions = Transactions()

    # Add a large number of transactions to test performance
    transactions_id_list = range(1000, 2000)
    k = len(transactions_id_list)
    for i in transactions_id_list:
        transactions.add_transaction(i, "deposit", i * 10, f"Transaction {i}")

    with pytest.raises(Exception):
        transactions.add_transaction(i, "withdrawal", 50, "Groceries")

    # Push transaction IDs to stack and queue
    for transaction_id in transactions_id_list:
        stack.push(transaction_id)
        queue.push(transaction_id)

    with pytest.raises(Exception):
        stack.push(transactions.get_transaction(i))
        queue.push(transactions.get_transaction(i + 1))

    # Pop all transactions and check if they are in the correct order
    for i in range(k):
        stack_popped = stack.pop()
        queue_popped = queue.pop()

        # Check if popped IDs are different
        assert stack_popped != queue_popped

        assert stack_popped == transactions_id_list[k - i - 1]
        assert queue_popped == transactions_id_list[i]

    # Check if stack and queue are empty
    assert stack.is_empty()
    assert queue.is_empty()
