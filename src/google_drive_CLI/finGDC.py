#!/usr/bin/env python3
"""
FinGDC - Command line Google Drive Client
Author: alfin.akhret@gmail.com
"""
import httplib2                     # Comprehensive Http client library
import os                           # Operating system module
import apiclient                    # Google API client Core library : https://developers.google.com/api-client-library/python/reference/pydoc
from apiclient import errors
from apiclient import discovery     # A client library for Google's discovery based APIs.
from apiclient.http import MediaFileUpload  # use to file upload
import oauth2client                 # OAuth 2.0  Functionality of apiclient library
from oauth2client import client     # Oauth 2.0 Client
from oauth2client import tools      # Command-line tools for authenticating via OAuth 2.0
import argparse

SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'FinGDC'

def get_credentials(flags):
    """Get valid user credentials from storage
    if nothing has been stored, or if the stores credentials are invalid
    the Oauth2 flow is completed to obtain the new credentials
    Returns:
        Credentials, the obtained credentials
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'drive-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        print('Storing credentials to:' + credential_path)
    return credentials

  
    
def ls(maxNumber,service):
    """List all files in the drive
    param: maxNumber - the maximum number of file to bi listed
    """
    
    results = service.files().list(maxResults=maxNumber).execute()
    items = results.get('items',[])
    if not items:
        print('No files found')
    else:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['title'], item['id']))


def u(service, title, filename):
    """ insert a new file
        reference: https://developers.google.com/resources/api-libraries/documentation/drive/v2/python/latest/drive_v2.files.html#insert 
    """
    body = {'title':title}

    try:
        file = service.files().insert(body=body, media_body=filename).execute()
        return file
    except errors.HttpError as error:
       print('An error occured: {}'.format(error))
       return None


    

def main():
    """Basic usage of google drive API
    Create google drive API service object and ouput the names and IDs
    for up to 10 files"""
    

    parser = argparse.ArgumentParser(parents=[tools.argparser])
    parser.add_argument('-ls', help='list all files in drive', action='store_true')
    parser.add_argument('-u', help='upload single file drive')
    args = parser.parse_args()
    
    credentials = get_credentials(args)
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v2', http=http)
  
    # file upload
    if args.u:
        u(service, args.u, args.u)

if __name__ == '__main__':
    main()

