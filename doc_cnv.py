from __future__ import print_function

import os.path

import io

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

import zipfile

import html2text

#Ideally, have a function that handles authentication and define the scope you need as well, since that's how it will authenticate
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']


def list_files():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('/Users/kitanogunkoya/Documents/Work/kylokitkog/sandbox/website/secrets/token.json'):
        creds = Credentials.from_authorized_user_file('/Users/kitanogunkoya/Documents/Work/kylokitkog/sandbox/website/secrets/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/Users/kitanogunkoya/Documents/Work/kylokitkog/sandbox/website/secrets/kitan_website_client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('/Users/kitanogunkoya/Documents/Work/kylokitkog/sandbox/website/secrets/token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')

SCOPES2 = ['https://www.googleapis.com/auth/drive']

def export_html(real_file_id):
    """Download a Document file in PDF format.
    Args:
        real_file_id : file ID of any workspace document format file
    Returns : IO object with location

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('/Users/kitanogunkoya/Documents/Work/kylokitkog/sandbox/website/secrets/token.json'):
        creds = Credentials.from_authorized_user_file('/Users/kitanogunkoya/Documents/Work/kylokitkog/sandbox/website/secrets/token.json', SCOPES2)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/Users/kitanogunkoya/Documents/Work/kylokitkog/sandbox/website/secrets/kitan_website_client_secret.json', SCOPES2)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('/Users/kitanogunkoya/Documents/Work/kylokitkog/sandbox/website/secrets/token.json', 'w') as token:
            token.write(creds.to_json())


    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        file_id = real_file_id

        # pylint: disable=maybe-no-member
        #exporting !!! -- good resource here: https://github.com/zephyrok/blog-code-examples/blob/main/python/googleapis/drive/googledriveoperations.py#L69
        #change the mimetype here to application/zip, see this doc for reference:
        #https://developers.google.com/drive/api/guides/ref-export-formats
        request = service.files().export_media(fileId=file_id,
                                               mimeType='application/zip')#using the old api mimetype to download as raw html
        # response = request.execute()
        # print(response)

        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(F'Download {int(status.progress() * 100)}.')

    except HttpError as error:
        print(F'\nAn error occurred:\n {error}')
        file = None

    #print file to check
    # print (file.getvalue())

    with open('/Users/kitanogunkoya/Documents/Work/kylokitkog/django/WebsiteSystemDesignDoc.zip', 'wb') as f:
        f.write(file.getvalue())
        # print (file.getvalue())


     #Open and read the zip file in mem
    with zipfile.ZipFile(file) as zip_ref:
        file_names = zip_ref.namelist()
        print(f"Files in the zip file: {file_names}\n")

        for file_x in file_names:
            with zip_ref.open(file_x, 'r') as file_ref:
                file_content = file_ref.read()
                print(f"Contents of {file_x}:\n")
                print(file_content.decode('utf-8'))


    return file_content.decode('utf-8')


def convert_html_to_markdown(html_content):
    # with open(html_content, 'r', encoding='utf-8') as file:
    #     html_content = file.read()

    # html_content=html_content.decode('utf-8')
    
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    markdown = converter.handle(html_content)

    with open('/Users/kitanogunkoya/Documents/Work/kylokitkog/django/WebsiteSystemDesignDoc.md', 'w', encoding='utf-8') as f:
        f.write(markdown)

    return markdown



def main():
    # list_files()
    html_content= export_html(real_file_id='1fFEuTRJtyaVosJh_XsRgAuOyNNzSHoIfkRNZKW5qL8M')
    convert_html_to_markdown(html_content)


if __name__ == '__main__':
    main()