from collections import defaultdict


class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        try:
            self.stack.pop()
        except Exception as e:
            print("The MyStack is empty. No more pop operations can be performed.")
            raise e

    def min(self) -> int:
        return min(self.stack) if not self.is_empty() else None

    def max(self) -> int:
        return max(self.stack) if not self.is_empty() else None

    def __str__(self) -> str:
        ans = ""
        if self.is_empty():
            return ans
        for i in range(len(self.stack) - 1, -1, -1):
            if i == 0:
                ans += str(self.stack[i])
            else:
                ans += str(self.stack[i]) + " -> "
        return ans

    def is_empty(self) -> bool:
        return len(self.stack) == 0


class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        try:
            self.queue.pop(0)
        except Exception as e:
            print("The MyQueue is empty. No more pop operations can be performed.")
            raise e

    def min(self) -> int:
        return min(self.queue) if not self.is_empty() else None

    def max(self) -> int:
        return max(self.queue) if not self.is_empty() else None

    def __str__(self) -> str:
        ans = ""
        if self.is_empty():
            return ans
        for i in range(0, len(self.queue)):
            if i == len(self.queue) - 1:
                ans += str(self.queue[i])
            else:
                ans += str(self.queue[i]) + " -> "
        return ans

    def is_empty(self) -> bool:
        return len(self.queue) == 0


class Transactions:
    def __init__(self):
        self.transaction_dict = defaultdict(dict)

    def add_transaction(
        self,
        transaction_id: int,
        transaction_type: str,
        transaction_amount: float,
        transaction_details: str,
    ):
        if transaction_id in self.transaction_dict:
            raise Exception('Duplicated transaction_id')
        self.transaction_dict[transaction_id]["transaction_type"] = transaction_type
        self.transaction_dict[transaction_id]["transaction_amount"] = transaction_amount
        self.transaction_dict[transaction_id][
            "transaction_details"
        ] = transaction_details

    def get_transaction(self, transaction_id: int) -> dict:
        if transaction_id in self.transaction_dict.keys():
            return self.transaction_dict[transaction_id]
        else:
            return {}

    def get_all_transactions(self) -> dict:
        return self.transaction_dict
