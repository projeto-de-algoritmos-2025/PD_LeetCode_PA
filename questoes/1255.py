from typing import List, Tuple
from functools import lru_cache


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        def count_letters(letters: List[str]) -> List[int]:
            count = [0] * 26
            for letter in letters:
                count[ord(letter) - ord("a")] += 1
            return count

        def calculate_word_score(word: str) -> int:
            return sum(score[ord(char) - ord("a")] for char in word)

        word_letter_counts = [count_letters(list(word)) for word in words]
        word_scores = [calculate_word_score(word) for word in words]
        total_words = len(words)
        initial_letters = tuple(count_letters(letters))  # convert to tuple for hashability

        @lru_cache(maxsize=None)
        def backtrack(index: int, remaining: Tuple[int, ...]) -> int:
            if index == total_words:
                return 0

            # Caso 1: não usar a palavra atual
            max_score = backtrack(index + 1, remaining)

            # Caso 2: tentar usar a palavra atual, se possível
            can_use = True
            new_remaining = list(remaining)
            for i in range(26):
                if word_letter_counts[index][i] > new_remaining[i]:
                    can_use = False
                    break
                new_remaining[i] -= word_letter_counts[index][i]

            if can_use:
                max_score = max(
                    max_score,
                    word_scores[index] + backtrack(index + 1, tuple(new_remaining))
                )

            return max_score

        return backtrack(0, initial_letters)
