"""Example usage for Social Choice Voting Skill."""
from client import SocialChoiceVoting

def main():
    print("Executing Social Choice Voting...")
    ballots = [
        ["Policy_Alpha", "Policy_Beta", "Policy_Gamma"],
        ["Policy_Alpha", "Policy_Gamma", "Policy_Beta"],
        ["Policy_Beta", "Policy_Alpha", "Policy_Gamma"]
    ]
    candidates = ["Policy_Alpha", "Policy_Beta", "Policy_Gamma"]

    winner = SocialChoiceVoting.condorcet_winner(ballots, candidates)
    scores = SocialChoiceVoting.borda_count(ballots, candidates)
    print("Condorcet Winner:", winner)
    print("Borda Count Scores:", scores)
    assert winner == "Policy_Alpha"
    assert scores["Policy_Alpha"] == 5
    print("Social Choice Voting verified successfully!")

if __name__ == "__main__":
    main()
