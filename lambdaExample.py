import json

hej = ['hej1', 'hej2']

def lambda_handler(event, context):

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST,GET'
        },
        'body': json.dumps(hej)
    }
