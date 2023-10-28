from supabase import create_client, Client
from cred import supurl, supkey

url: str =supurl
key: str =supkey

supabase: Client = create_client(url, key)

def insert_main(data):
    table = "main"
    supabase.table(table).insert(data).execute()
    #{"emailid":"nisarvskp@gmail.com","linkedin":"xyz.com","github":"abc.com"}
def edit_data_main(data):
    table="main"
    mail=data.get("emailid")
    supabase.table(table).update({"linkedin":data.get("linkedin"),"github":data.get("github")}).match({"emailid":mail}).execute()
def fetch_data(data):
    table="main"
    mail=data.get("emailid")
    response = supabase.table(table).select("linkedin,github").match({"emailid":mail}).execute()
    r=response.data
    r=r[0]
    res={"linkedin":r.get("linkedin"),"github":r.get("github")}
    return res
    