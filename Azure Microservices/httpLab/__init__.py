import logging
import pyodbc

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(f"This Azure function rocks. With pyodbc version {pyodbc.version}")