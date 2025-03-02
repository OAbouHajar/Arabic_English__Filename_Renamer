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
    ' ': ' '
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

# TODO: make generic file path [args maybe?]
path = '/Users/oabouhajar/project/rename_files/Arabic_English__Filename_Renamer/files/'
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

def file_name_ext_constractor(path, name, ext):
    return path+ name + "." + ext


def file_renamer(old_file_name, new_file_name , ext):
    os.rename(file_name_ext_constractor(path,old_file_name,ext),file_name_ext_constractor(path,new_file_name,ext))
    return True

def en_ar_replacement_process(user_select = '1'):
    one_at_time = False
    all_at_one = False

    if(user_select == '1'):
        all_at_one = True
    elif user_select == '2':
        one_at_time = True

    for file in files:
        old_file_name , ext = file.split(".")
        new_file_name = replace_name(old_file_name.lower())
        print("File Extension: \t\t\t",ext)
        print("Old File Name: \t\t\t", old_file_name)
        print("New File Name: \t\t\t", new_file_name)
        if (one_at_time):
            if(input('''Are you Happy with the generated name [y/n]?''') == 'y'):
                file_renamer(old_file_name, new_file_name, ext)
            else:
                file_renamer(old_file_name, input("Enter the name you like please: "), ext)
        elif (all_at_one):
            file_renamer(old_file_name, new_file_name, ext)



def get_user_selection():
    print(MENU)
    return input("Please Select One OF The Option: ")


if __name__ == "__main__":

#     comment
    print("hello")
    print("hello again")
    user_select = get_user_selection()
    en_ar_replacement_process(user_select)