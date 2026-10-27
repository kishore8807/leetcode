class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentences=set(sentence.lower())
        return True if len(sentences)==26 else False
