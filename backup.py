import json
# import the AWS SDK (for Python the package name is boto3)
import boto3

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table

table = dynamodb.Table('Artists') 

def update_item(name):
    
    try:
        response = table.update_item(
        Key={'id': name},
        UpdateExpression="set var_value=list_append(var_value, :p)",
        ExpressionAttributeValues={':p': val},
        ReturnValues="UPDATED_NEW"
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Attributes']

def lambda_handler(event, context):
    print(event)
    artist = json.loads( event['body'] )
    name = artist['name']
    acclaimed_albums_count = artist['acclaimed_albums_count']
    genre = artist['genre']
    average = artist['average']
    albums = artist['albums']
    
    print(name)
    print(genre)
    print(albums)
    print(average)
    msg = "failed to write to table"
    # debateToken = remove_chars(debateToken,"\"")
    # if debateId:
    response = table.get_item( Key={'id':name} )
    
    if response:
        response = update_item(name)
    else:
        response = table.put_item(
        Item={
            'id': name,
            'name': name,
            'genre': genre,
            'albums': albums, 
            'acclaimed_albums_count': acclaimed_albums_count
            })
            
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
