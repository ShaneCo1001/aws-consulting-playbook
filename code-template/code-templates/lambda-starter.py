import boto3
import json
import uuid
from boto3.dynamodb.conditions import Attr

# ============================================================
# CONFIGURATION — Update these for each project
# ============================================================
TABLE_NAME = "your-table-name"
BUCKET_NAME = "your-bucket-name"
TOPIC_ARN = "arn:aws:sns:us-east-1:YOUR_ACCOUNT:your-topic"
REGION = "us-east-1"

# ============================================================
# AWS CLIENTS — Add/remove as needed
# ============================================================
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)
s3 = boto3.client("s3")
sns = boto3.client("sns", region_name=REGION)

# ============================================================
# CORS HEADERS — Required for web app integration
# ============================================================
HEADERS = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type,Authorization",
    "Access-Control-Allow-Methods": "GET,POST,PUT,DELETE,OPTIONS"
}

# ============================================================
# HELPER FUNCTIONS
# ============================================================
def success(data, status=200):
    return {
        "statusCode": status,
        "headers": HEADERS,
        "body": json.dumps(data)
    }

def error(message, status=400):
    return {
        "statusCode": status,
        "headers": HEADERS,
        "body": json.dumps({"error": message})
    }

def get_all_items():
    response = table.scan()
    return response["Items"]

def get_item(item_id):
    response = table.get_item(Key={"id": item_id})
    return response.get("Item")

def create_item(data):
    item = {
        "id": str(uuid.uuid4()),
        **data
    }
    table.put_item(Item=item)
    return item

def delete_item(item_id):
    table.delete_item(Key={"id": item_id})

# ============================================================
# MAIN HANDLER
# ============================================================
def lambda_handler(event, context):
    method = event.get("httpMethod", "GET")
    path = event.get("path", "/")
    query_params = event.get("queryStringParameters") or {}
    body = json.loads(event.get("body") or "{}")

    # Handle CORS preflight
    if method == "OPTIONS":
        return success({})

    try:
        # GET all items
        if method == "GET" and path == "/items":
            items = get_all_items()
            return success(items)

        # GET single item
        elif method == "GET" and path.startswith("/items/"):
            item_id = path.split("/")[-1]
            item = get_item(item_id)
            if not item:
                return error("Item not found", 404)
            return success(item)

        # POST create item
        elif method == "POST" and path == "/items":
            if not body:
                return error("Request body required")
            item = create_item(body)
            return success(item, 201)

        # DELETE item
        elif method == "DELETE" and path.startswith("/items/"):
            item_id = path.split("/")[-1]
            delete_item(item_id)
            return success({"message": "Deleted successfully"})

        else:
            return error("Not found", 404)

    except Exception as e:
        print(f"Error: {str(e)}")
        return error(f"Internal server error: {str(e)}", 500)