import pytest

try:
    import glob
    import importlib

    script_path = glob.glob("./lab6.py")[0]
    module_path = script_path[2:-3]
    module = importlib.import_module(module_path)
except Exception:
    raise Exception(
        "No script is available. Please follow the assignment instructions."
    )

try:
    MyStack = module.MyStack
    MyQueue = module.MyQueue
    Transactions = module.Transactions
except Exception:
    raise Exception(
        "Please ensure all required classes have been implemented.")

# pytest cases


def test_stack(capfd):
    my_stack = MyStack()
    assert my_stack.is_empty() is True
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    print(my_stack)
    out, _ = capfd.readouterr()
    assert out == "3 -> 2 -> 1\n"
    assert my_stack.is_empty() is False
    assert my_stack.min() == 1
    assert my_stack.max() == 3
    my_stack.pop()
    print(my_stack)
    out, _ = capfd.readouterr()
    assert out == "2 -> 1\n"
    assert my_stack.min() == 1
    assert my_stack.max() == 2
    my_stack.pop()
    print(my_stack)
    out, _ = capfd.readouterr()
    assert out == "1\n"
    assert my_stack.min() == 1
    assert my_stack.max() == 1
    my_stack.pop()
    print(my_stack)
    out, _ = capfd.readouterr()
    assert out == "\n"
    assert my_stack.is_empty() is True

    with pytest.raises(Exception):
        my_stack.pop()


def test_queue(capfd):
    my_queue = MyQueue()
    assert my_queue.is_empty() is True
    my_queue.push(1)
    my_queue.push(2)
    my_queue.push(3)
    print(my_queue)
    out, _ = capfd.readouterr()
    assert out == "1 -> 2 -> 3\n"
    assert my_queue.is_empty() is False
    assert my_queue.min() == 1
    assert my_queue.max() == 3
    my_queue.pop()
    print(my_queue)
    out, _ = capfd.readouterr()
    assert out == "2 -> 3\n"
    assert my_queue.min() == 2
    assert my_queue.max() == 3
    my_queue.pop()
    print(my_queue)
    out, _ = capfd.readouterr()
    assert out == "3\n"
    assert my_queue.min() == 3
    assert my_queue.max() == 3
    my_queue.pop()
    print(my_queue)
    out, _ = capfd.readouterr()
    assert out == "\n"
    assert my_queue.is_empty() is True

    with pytest.raises(Exception):
        my_queue.pop()
    assert my_queue.min() is None
    assert my_queue.max() is None



def test_transactions():
    transactions = Transactions()
    transactions.add_transaction(67686, "deposit", 5000, "Monthly Allowance")
    transactions.add_transaction(67687, "withdrawal", 200, "Phone bill")
    transactions.add_transaction(67688, "deposit", 1234.56, "Salary")

    assert transactions.get_transaction(67686) == {
        "transaction_type": "deposit",
        "transaction_amount": 5000,
        "transaction_details": "Monthly Allowance"
    }
    assert transactions.get_transaction(67687) == {
        "transaction_type": "withdrawal",
        "transaction_amount": 200,
        "transaction_details": "Phone bill"
    }
    assert transactions.get_transaction(67688) == {
        "transaction_type": "deposit",
        "transaction_amount": 1234.56,
        "transaction_details": "Salary"
    }
    assert transactions.get_transaction(67689) == {}
    assert transactions.get_all_transactions() == {
        67686: {
            "transaction_type": "deposit",
            "transaction_amount": 5000,
            "transaction_details": "Monthly Allowance"
        },
        67687: {
            "transaction_type": "withdrawal",
            "transaction_amount": 200,
            "transaction_details": "Phone bill"
        },
        67688: {
            "transaction_type": "deposit",
            "transaction_amount": 1234.56,
            "transaction_details": "Salary"
        }
    }
