from langchain_core.tools import tool

@tool
def translate45():
    """Translating the code 45 to a string"""
    return "Code 45: Request timeout - the Nissim server did not receive a complete request within the allowed time."

@tool
def translate63():
    """Translating the code 63 to a string"""
    return "Code 63: Nissim Service unavailable - the requested service is temporarily down for maintenance."
