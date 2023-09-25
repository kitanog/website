import html2text
import os.path
import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError


# =======================================================
# CONVERT Google docs FILE - V3 (using api V3)
# =======================================================

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

#The main method that will be used here will be the file.export
#Exports a Google Workspace document to the requested MIME type and returns exported byte content. Note that the exported content is limited to 10MB.
#https://developers.google.com/drive/api/reference/rest/v3/files/export
#export mime types: https://developers.google.com/drive/api/guides/ref-export-formats
#NOTE: file.get is used to https://developers.google.com/drive/api/reference/rest/v3/files/get


#Convert to markdown
#some other options for conversion: https://pypi.org/project/pyandoc/
# def convert_html_to_markdown(html_content):
#     converter = html2text.HTML2Text()
#     converter.ignore_links = False
#     markdown = converter.handle(html_content)
#     return markdown

# # DOCUMENT_ID = '1fFEuTRJtyaVosJh_XsRgAuOyNNzSHoIfkRNZKW5qL8M'
# html_content = get_google_docs_as_html(DOCUMENT_ID)
# markdown_content = convert_html_to_markdown(html_content)

# with open('/Users/kitanogunkoya/Documents/Work/kylokitkog/django/WebsiteSystemDesignDoc.md', 'w') as f:
#     f.write(markdown_content)









# =======================================================
# CONVERT Google docs FILE - V2 (using api V1)
# =======================================================


# # If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

# # The ID of a sample document.
# DOCUMENT_ID = '1fFEuTRJtyaVosJh_XsRgAuOyNNzSHoIfkRNZKW5qL8M'


# def get_google_docs_as_html(DOCUMENT_ID):
#     creds = None
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json')
    
#     # If no (valid) credentials available, prompt the user to log in.
#     # This part is generally done once to get the token.json
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 '/Users/kitanogunkoya/Documents/Work/kylokitkog/sandbox/website/kitan_website_client_secret.json', SCOPES)
#             creds = flow.run_local_server(port=0)
            
#         # Save the credentials for the next run
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())

#     try:
#         service = build('docs', 'v1', credentials=creds)
        
#         #get the document as html
#         # document = service.documents().get(documentId=DOCUMENT_ID).execute()

#         document = service.documents().get(documentId=DOCUMENT_ID).execute()
#         #get the content, body, titele -  change to title for title
#         # Ref doc: 
#         response = document.get('body')
#         #troubleshooting
#         print(response)

#         return response
#     except HttpError as err:
#         print(err)

# json_content = get_google_docs_as_html(DOCUMENT_ID)
# # print(html_content)

# with open('/Users/kitanogunkoya/Documents/Work/kylokitkog/django/WebsiteSystemDesignDoc.json', 'w+') as f:
#     json.dump(json_content, f)


#Convert to markdown
# def convert_html_to_markdown(html_content):
#     converter = html2text.HTML2Text()
#     converter.ignore_links = False
#     markdown = converter.handle(html_content)
#     return markdown

# # DOCUMENT_ID = '1fFEuTRJtyaVosJh_XsRgAuOyNNzSHoIfkRNZKW5qL8M'
# html_content = get_google_docs_as_html(DOCUMENT_ID)
# markdown_content = convert_html_to_markdown(html_content)

# with open('/Users/kitanogunkoya/Documents/Work/kylokitkog/django/WebsiteSystemDesignDoc.md', 'w') as f:
#     f.write(markdown_content)



# =======================================================
# CONVERT LOCAL FILE - V1
# =======================================================

# def convert_html_to_markdown(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         html_content = file.read()
    
#     converter = html2text.HTML2Text()
#     converter.ignore_links = False
#     markdown = converter.handle(html_content)
#     return markdown

# markdown_content = convert_html_to_markdown("/Users/kitanogunkoya/Documents/Work/kylokitkog/django/WebsiteSystemDesignDoc.html")

# with open('/Users/kitanogunkoya/Documents/Work/kylokitkog/django/WebsiteSystemDesignDoc.md', 'w', encoding='utf-8') as f:
#     f.write(markdown_content)
