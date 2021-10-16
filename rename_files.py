import os


AR_EN_ALPHA = {
    'ع': 'aa',
    'ا':'a', 
    'ب':'b', 
    'ت':'t', 
    'ث':'th', 
    'ج':'j', 
    'ح':'h', 
    'خ':'kh', 
    'ه':'h', 
    'ة': 'h',
    'غ':'g', 
    'ف':'f', 
    'ق':'q', 
    'ص':'s', 
    'ض':'da', 
    'د':'d', 
    'ذ':'z', 
    'ط':'ta', 
    'ك':'k', 
    'م':'m', 
    'ن':'n', 
    'ل':'l', 
    'ي':'y', 
    'س':'s', 
    'ش':'sh', 
    'ظ':'za', 
    'ز':'z', 
    'و':'w', 
    'ر':'r',
    }

EN_ALPH_LETTER = ['a', 'b', 'c', 'd', 'e', 'f', 
                  'g', 'h', 'i', 'j', 'k', 'l', 
                  'm', 'n', 'o', 'p', 'q', 'r', 
                  's', 't', 'u', 'v', 'w', 'x', 
                  'y', 'z']

OK_CHAR = ['/','-', ',','*']

MENU = '''
       ##########################################
       ###########      WELCOME TO    ###########
       ###########  AR -> EN RENAMER  ###########
       ##########################################
       1- To change all name at once.
       2- To check names before each change.
       3- Read The App Description.
       '''

path = '/Users/oabouhajar/project/rename_files/files/'
files = os.listdir(path)


def replace_name(name):
    en_name = ""
    for char in name:
        if(char in AR_EN_ALPHA): # handeling Arabic letter replacement
            en_name += AR_EN_ALPHA.get(char)
        elif(char in EN_ALPH_LETTER): # handeling English Letter 
            en_name += char
        elif(isinstance(char, int) or char in OK_CHAR): # handeling Numbers
            en_name += char
        else:               # handeling Other Charecters by removing it
            en_name +=''

    # return english new name
    return en_name


def en_ar_replacement():
    for f in files:
        file_name , ext= f.split(".")
        print(file_name)
        print(ext)
        new_name = replace_name(file_name)
        os.rename(path+f, ( path+ new_name + "." + ext))


def get_user_description():
    print(MENU)
    return input("Please Select One OF The Option: ")


if __name__ == "__main__":
    user_select = get_user_description()