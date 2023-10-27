
import os
from supabase import create_client, Client
from cred import supurl, supkey

url: str =supurl
key: str =supkey

supabase: Client = create_client(url, key)

def insert_main(data):
    table = "main"
    supabase.table(table).insert(data).execute()
    #{"emailid":"nisarvskp@gmail.com","linkedin":"bruh.com","github":"susu.com"}
