from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Connect to the Google Drive API
creds = Credentials.from_authorized_user_info(info=info)
service = build('drive', 'v3', credentials=creds)

# Get the ID of the parent folder where the file will be uploaded
folder_id = 'your_folder_id'

# Get the file name and path of the SQLite3 database
file_name = 'database.db'
file_path = 'path/to/' + file_name

# Upload the file to Google Drive
file_metadata = {'name': file_name, 'parents': [folder_id]}
media = MediaFileUpload(file_path, mimetype='application/x-sqlite3')
file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
print(F'File ID: {file.get("id")}')
