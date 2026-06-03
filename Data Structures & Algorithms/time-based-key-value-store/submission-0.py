class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = {}
        if timestamp not in self.keys[key]:
            self.keys[key][timestamp] = []
        self.keys[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""

        counter = 0
        for t in self.keys[key]:
            if t <= timestamp:
                counter = max(counter, t)
        if counter == 0:
            return ""
        else:
            return self.keys[key][counter][-1]
