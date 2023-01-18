pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

creds = Credentials.from_authorized_user_info(info=info)
drive_service = build('drive', 'v3', credentials=creds)
file_id = 'FILE_ID'
request = drive_service.files().get_media(fileId=file_id)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print("Download %d%%." % int(status.progress() * 100))
fh.seek(0)

