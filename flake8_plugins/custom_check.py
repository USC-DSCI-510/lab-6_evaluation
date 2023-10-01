import ast


class BaseChecker:
    def __init__(self, tree, module_name, class_name, violation_code, message):
        self._tree = tree
        self.module_name = module_name
        self.class_name = class_name
        self.violation_code = violation_code
        self.message = message

    def run(self):
        for node in ast.walk(self._tree):
            if isinstance(node, ast.ImportFrom):
                if node.module == self.module_name:
                    for alias in node.names:
                        if alias.name == self.class_name:
                            yield (
                                node.lineno,
                                node.col_offset,
                                f"{self.violation_code} {self.message}",
                                type(self),
                            )
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name == self.module_name:
                        setattr(self, f"imported_{self.module_name}", True)
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == self.class_name:
                        if hasattr(self, f"imported_{self.module_name}") and getattr(
                            self, f"imported_{self.module_name}"
                        ):
                            yield (
                                node.lineno,
                                node.col_offset,
                                f"{self.violation_code} {self.message}",
                                type(self),
                            )
            elif isinstance(node, ast.Attribute) and getattr(node, "attr", "") == self.class_name:
                if hasattr(self, f"imported_{self.module_name}") and getattr(self, f"imported_{self.module_name}"):
                    yield (
                        node.lineno,
                        node.col_offset,
                        f"{self.violation_code} {self.message}",
                        type(self),
                    )
            elif isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == self.class_name:
                    if hasattr(self, f"imported_{self.module_name}") and getattr(self, f"imported_{self.module_name}"):
                        yield (
                            node.lineno,
                            node.col_offset,
                            f"{self.violation_code} {self.message}",
                            type(self),
                        )


class DequeChecker(BaseChecker):
    def __init__(self, tree):
        super().__init__(
            tree,
            "collections",
            "deque",
            "CLA001",
            "Do not use collections.deque directly. Consider using a list or other data structure.",
        )


class QueueChecker(BaseChecker):
    def __init__(self, tree):
        super().__init__(
            tree,
            "queue",
            "Queue",
            "CLA002",
            "Do not use queue.Queue directly. Consider using a list or other data structure.",
        )
