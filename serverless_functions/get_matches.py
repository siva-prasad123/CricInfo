# serverless_functions/get_matches.py
import json

def handler(event, context):
    tournament_name = event['pathParameters']['tournament_name']
    # Fetch match data for the specified tournament
    if tournament_name == 'IPL 2024':  # Adjust as needed
        matches_data = {
            'matches': [
                {
                    'match_id': 1,
                    'pitch_report': 'Pitch is dry with cracks, good for spinners.',
                    'toss_status': 'Mumbai Indians won the toss and elected to bat.',
                    'current_players': ['Kohli', 'Rohit', 'Dhoni', 'Pandya'],
                    'bowler': 'Bumrah',
                    'target': '250'
                }
            ]
        }
        return {
            'statusCode': 200,
            'body': json.dumps(matches_data)
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Tournament not found'})
        }
