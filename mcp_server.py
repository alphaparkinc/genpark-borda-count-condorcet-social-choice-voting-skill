"""MCP Server for Social Choice Voting Skill."""
import json
import sys
from client import SocialChoiceVoting

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "aggregate_social_choice",
                            "description": "Aggregate agent preferences using Borda count and Condorcet winner",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "ballots": {
                                        "type": "array",
                                        "items": {"type": "array", "items": {"type": "string"}}
                                    },
                                    "candidates": {"type": "array", "items": {"type": "string"}}
                                },
                                "required": ["ballots", "candidates"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                b = args["ballots"]
                c = args["candidates"]
                cond = SocialChoiceVoting.condorcet_winner(b, c)
                borda = SocialChoiceVoting.borda_count(b, c)
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps({"condorcet_winner": cond, "borda_scores": borda})}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
