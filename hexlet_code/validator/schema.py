class Schema:

    def __init__(self):
        self.rule = None

    def required(self):
        self.rule = lambda s: s not in [None, '']
        return self

    def min_len(self, min_len):
        self.rules = lambda s: len(s) >= min_len
        return self

    def contains(self, substring):
        self.rule = lambda s: substring in s
        return self

    def is_valid(self, text):
        if self.rule is None:
            return True
        return self.rule(text)
