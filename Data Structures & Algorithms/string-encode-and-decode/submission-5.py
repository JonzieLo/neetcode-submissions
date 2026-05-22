class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "$"
        return "\x1e" + "\x1e".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "$":
            return []
        return s[1:].split("\x1e")
