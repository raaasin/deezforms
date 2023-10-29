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
def insert_scraped(data):
    table='main'
    mail=data.get("emailid")
    supabase.table(table).update({"linkscrape":data.get("linkscrape"),"gitscrape":data.get("gitscrape")}).match({"emailid":mail}).execute()
    #{"emailid":"nisarvskp","linkscrape":"xyz.com","gitscrape":"abc.com"}
def edit_data_scraped(data):
    table="main"
    mail=data.get("emailid")
    supabase.table(table).update({"linkscrape":data.get("linkscrape"),"gitscrape":data.get("gitscrape")}).match({"emailid":mail}).execute()
def fetch_data_scraped(data):
    table="main"
    mail=data.get("emailid")
    response = supabase.table(table).select("linkscrape,gitscrape").match({"emailid":mail}).execute()
    r=response.data
    r=r[0]
    res={"linkscrape":r.get("linkscrape"),"gitscrape":r.get("gitscrape")}
    return res
def does_user(data):
    table="userbase"
    mail=data.get("emailid")
    pas=data.get("password")
    response = supabase.table(table).select("emailid,password").match({"emailid":mail,"password":pas}).execute()
    r=response.data
    if len(r)==0:
        return False
    else:
        return True
def new_user(data):
    table="userbase"
    #check if email already exists then return false
    mail=data.get("emailid")
    pas=data.get("password")
    response = supabase.table(table).select("emailid").match({"emailid":mail}).execute()
    r=response.data
    if len(r)==0:
        try:
            supabase.table(table).insert(data).execute()
            return True
        except:
            return "something went wrong"
    else:
        return "user already exists"
    