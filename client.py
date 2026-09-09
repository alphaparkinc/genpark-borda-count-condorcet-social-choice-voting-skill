"""
Autonomous Agent Social Choice Voting Skill
Pure Python Standard Library implementation.
"""
from typing import List, Dict, Optional, Any

class SocialChoiceVoting:
    """
    Borda Count and Condorcet Winner social choice aggregator.
    """
    @staticmethod
    def borda_count(ballots: List[List[str]], candidates: List[str]) -> Dict[str, int]:
        scores = {c: 0 for c in candidates}
        n = len(candidates)
        for ballot in ballots:
            for rank, c in enumerate(ballot):
                if c in scores:
                    scores[c] += (n - 1 - rank)
        return scores

    @staticmethod
    def condorcet_winner(ballots: List[List[str]], candidates: List[str]) -> Optional[str]:
        for c1 in candidates:
            wins_all = True
            for c2 in candidates:
                if c1 != c2:
                    head_to_head = sum(1 for b in ballots if b.index(c1) < b.index(c2))
                    if head_to_head <= len(ballots) / 2.0:
                        wins_all = False
                        break
            if wins_all:
                return c1
        return None
