from download import write_to_file
from openpyxl import load_workbook



def extract_xls_files(path):

    #extrait le workbook puis le worksheet
    wb = load_workbook(path, data_only=True)
    ws = wb['List of channels']

    all_col = list(ws.columns)


    for cell in all_col[6]:
        content = cell.value
        try:
            write_to_file('tv channels', content);
        except Exception as e:
            write_to_file('errors.txt', f"erreur pour {content}: {e}")

if __name__ == '__main__':
    extract_xls_files('channels_names/20240318 list of tv channels.xlsx')