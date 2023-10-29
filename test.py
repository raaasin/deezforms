from supabase import create_client
from cred import supurl, supkey

# Initialize the Supabase client
 # Replace with your Supabase API Key
supabase = create_client(supurl, supkey)

# Data to insert
data= {
 'emailid': 'new@gmail.com','linkscrape':'xyz.com','gitscrape':'abc.com'
}
mail=data.get("emailid")
# Specify the table name
table= 'main'
supabase.table(table).update({"linkscrape":data.get("linkscrape"),"gitscrape":data.get("gitscrape")}).match({"emailid":mail}).execute()