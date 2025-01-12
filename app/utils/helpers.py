def format_response(message, status=200):
    return {
        "status": status,
        "message": message
    }
