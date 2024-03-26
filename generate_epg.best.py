from extract_xlsx_files import get_all_specchar
from download import write_to_xlsx_file

dico_spec = {"+": "Plus", "&": "And", "'": "", "_": "", "(": "", "/": "", ")": "", "-": "", ".": "", ";": "", " ": "", "*": "", "!": "", "´": ""}
def modify_specchar(channel_name):
    new_channel_name = ""
    i, n = 0, len(channel_name)
    while i<n:
        char = channel_name[i]
        if not (char.isalpha() or char.isnumeric()):
            new_channel_name += dico_spec[char]
        else:
            new_channel_name += char
        i += 1
    return new_channel_name



def modify_all_channel(channel_list):
    res = []
    for channel in channel_list:
        new_channel_name = modify_specchar(channel)
        res.append(new_channel_name)
    return res

if __name__ == "__main__":
    write_to_xlsx_file("channels_names/channel_list_charspec.xlsx", modify_all_channel(get_all_specchar("channels_names/20240318 list of tv channels.xlsx")))