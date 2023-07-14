from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from auth import get_credentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SPREADSHEET_ID = '1EuqtYAOY3mhgjbOSljBEKcuj46NJU1jBRYymaWD_So4'


# RANGE_NAME = 'Пользователи!A:E'


def append(sheets: str, values: list):
    """Пример использования Sheets API.
    Записывает данные в таблицу.
    """
    try:
        service = build('sheets', 'v4', credentials=get_credentials())

        # Вызываем Sheets API
        sheet = service.spreadsheets()
        values = [values]
        body = {'values': values}
        sheet.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=sheets,
            valueInputOption='RAW',
            body=body,
            insertDataOption='INSERT_ROWS',
        ).execute()
        return 'Данные успешно записаны в таблицу.'
    except HttpError as err:
        return str(err)
    
if __name__ == "__main__":
    print(append(sheets="Users", values=["asd", "qwe", "sdfd"]))