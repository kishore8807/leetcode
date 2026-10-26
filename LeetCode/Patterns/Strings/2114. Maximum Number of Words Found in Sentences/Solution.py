class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        large_sentence= max(sentences,key=len)
        return len(large_sentence.split())