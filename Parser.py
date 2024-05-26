import string

def subjectRecognizer(word):
    alphabet_list = list(string.ascii_lowercase)
    state_list = [
                'q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10',
                'q11','q12','q13'
                ]
    transition_table = {}

    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state, alphabet)] = 'error'
        transition_table[(state, '#')] = 'error'
        transition_table[(state, ' ')] = 'error'

    #Table transition
    # first state
    transition_table[("q0", " ")] = "q0"

    # Finish state
    transition_table[("q13", "#")] = "accept"
    transition_table[("q13", " ")] = "q13"

    #Untuk kata "aku"
    transition_table[("q0","a")] = "q1"
    transition_table[("q1","k")] = "q2"
    transition_table[("q2","u")] = "q13"

    #Untuk kata "dia"
    transition_table[("q0","d")] = "q3"
    transition_table[("q3","i")] = "q4"
    transition_table[("q4","a")] = "q13"

    #Untuk kata "tia"
    transition_table[("q0","t")] = "q5"
    transition_table[("q5","i")] = "q6"
    transition_table[("q6","a")] = "q13"

    #Untuk kata "anto"
    transition_table[("q0","a")] = "q7"
    transition_table[("q7","n")] = "q8"
    transition_table[("q8","t")] = "q9"
    transition_table[("q9","o")] = "q13"

    #Untuk kata "budi"
    transition_table[("q0","b")] = "q10"
    transition_table[("q10","u")] = "q11"
    transition_table[("q11","d")] = "q12"
    transition_table[("q12","i")] = "q13"

    idx_char = 0
    state = 'q0'
    current_token = ''
    while state!='accept':
        current_char = word[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state=='q13':
            return True
        if state== 'error':
            return False
        idx_char = idx_char + 1
    return False

def predicateRecognizer(word):
    alphabet_list = list(string.ascii_lowercase)
    state_list = [
                'q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10',
                'q11','q12','q13','q14','q15','q16','q17','q18','q19',
                'q20','q21','q22','q23'
                ]
    transition_table = {}

    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state, alphabet)] = 'error'
        transition_table[(state, '#')] = 'error'
        transition_table[(state, ' ')] = 'error'

    #Table transition
    # first state
    transition_table[("q0", " ")] = "q0"

    # Finish state
    transition_table[("q23", "#")] = "accept"
    transition_table[("q23", " ")] = "q23"

    #Untuk kata "suka"
    transition_table[("q0","s")] = "q1"
    transition_table[("q1","u")] = "q2"
    transition_table[("q2","k")] = "q3"
    transition_table[("q3","a")] = "q23"

    #Untuk kata "membaca"
    transition_table[("q0","m")] = "q3"
    transition_table[("q3","e")] = "q4"
    transition_table[("q4","m")] = "q5"
    transition_table[("q5","b")] = "q6"
    transition_table[("q6","a")] = "q7"
    transition_table[("q7","c")] = "q8"
    transition_table[("q8","a")] = "q23"

    #Untuk kata "menonton"
    transition_table[("q0","m")] = "q3"
    transition_table[("q3","e")] = "q4"
    transition_table[("q4","n")] = "q13"
    transition_table[("q13","o")] = "q14"
    transition_table[("q14","n")] = "q15"
    transition_table[("q15","t")] = "q16"
    transition_table[("q16","o")] = "q17"
    transition_table[("q17","n")] = "q23"

    #Untuk kata "melihat"
    transition_table[("q0","m")] = "q3"
    transition_table[("q3","e")] = "q4"
    transition_table[("q4","l")] = "q9"
    transition_table[("q9","i")] = "q10"
    transition_table[("q10","h")] = "q11"
    transition_table[("q11","a")] = "q12"
    transition_table[("q12","t")] = "q23"

    #Untuk kata "sayang"
    transition_table[("q0","s")] = "q18"
    transition_table[("q18","a")] = "q19"
    transition_table[("q19","y")] = "q20"
    transition_table[("q20","a")] = "q21"
    transition_table[("q21","n")] = "q22"
    transition_table[("q22","g")] = "q23"

    idx_char = 0
    state = 'q0'
    current_token = ''
    while state!='accept':
        current_char = word[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state=='q13':
            return True
        if state== 'error':
            return False
        idx_char = idx_char + 1
    return False

def tokenRecognizer(sentence):
    tokens = sentence.lower().split()
    terminal = []
    for word in tokens:
        if subjectRecognizer(word) :
            terminal.append('SB')
        elif PredicateRecognizer(word):
            terminal.append('P')
        elif objectRecognizer(word):
            terminal.append('O')
        elif keteranganRecognizer(word):
            terminal.append('K')
    return terminal


def Parser(sentence):
    print("\n====== Parser ====== \n")
    tokens = sentence.lower().split()
    tokens.append('EOS')
    # symbols definition
    non_terminals = ['S','SB','P','O','K']
    terminals = ['aku','dia','tia','anto','budi',
                'suka','membaca','melihat','menonton','sayang',
                'kamu','film','buku','surat','anime',
                'kemarin','besok','banget','sekali','nanti'
                ]

    parse_table = {}

    parse_table[('S','aku')] = ['SB', 'P', 'O']
    parse_table[('S','dia')] = ['SB', 'P', 'O']
    parse_table[('S','tia')] = ['SB', 'P', 'O']
    parse_table[('S','anto')] = ['SB', 'P', 'O']
    parse_table[('S','budi')] = ['SB', 'P', 'O'] 
    
    parse_table[('S','suka')] = ['error']
    parse_table[('S','membaca')] =['error']
    parse_table[('S','melihat')] = ['error']
    parse_table[('S','menonton')] = ['error']
    parse_table[('S','sayang')] = ['error']
    
    parse_table[('S','kamu')] = ['error']
    parse_table[('S','film')] = ['error']
    parse_table[('S','buku')] = ['error']
    parse_table[('S','surat')] = ['error']
    parse_table[('S','anime')] = ['error']

    parse_table[('S','kemarin')] = ['error']
    parse_table[('S','besok')] = ['error']
    parse_table[('S','banget')] = ['error']
    parse_table[('S','sekali')] = ['error']
    parse_table[('S','nanti')] = ['error']
    parse_table[('S','EOS')] = ['error']


    parse_table[('SB','aku')] = ['aku']
    parse_table[('SB','dia')] = ['dia']
    parse_table[('SB','tia')] = ['tia']
    parse_table[('SB','anto')] = ['anto']
    parse_table[('SB','budi')] = ['budi']
    
    parse_table[('SB','suka')] = ['error']
    parse_table[('SB','membaca')] =['error']
    parse_table[('SB','melihat')] = ['error']
    parse_table[('SB','menonton')] = ['error']
    parse_table[('SB','sayang')] = ['error']
    
    parse_table[('SB','kamu')] = ['error']
    parse_table[('SB','film')] = ['error']
    parse_table[('SB','buku')] = ['error']
    parse_table[('SB','surat')] = ['error']
    parse_table[('SB','anime')] = ['error']

    parse_table[('SB','kemarin')] = ['error']
    parse_table[('SB','besok')] = ['error']
    parse_table[('SB','banget')] = ['error']
    parse_table[('SB','sekali')] = ['error']
    parse_table[('SB','nanti')] = ['error']
    parse_table[('SB','EOS')] = ['error']

 
    parse_table[('P','aku')] = ['error']
    parse_table[('P','dia')] = ['error']
    parse_table[('P','tia')] = ['error']
    parse_table[('P','anto')] = ['error']
    parse_table[('P','budi')] = ['error']
    
    parse_table[('P','suka')] = ['suka']
    parse_table[('P','membaca')] =['membaca']
    parse_table[('P','melihat')] = ['melihat']
    parse_table[('P','menonton')] = ['menonton']
    parse_table[('P','sayang')] = ['sayang']
    
    parse_table[('P','kamu')] = ['error']
    parse_table[('P','film')] = ['error']
    parse_table[('P','buku')] = ['error']
    parse_table[('P','surat')] = ['error']
    parse_table[('P','anime')] = ['error']

    parse_table[('P','kemarin')] = ['error']
    parse_table[('P','besok')] = ['error']
    parse_table[('P','banget')] = ['error']
    parse_table[('P','sekali')] = ['error']
    parse_table[('P','nanti')] = ['error']
    parse_table[('P','EOS')] = ['error']

   
    parse_table[('O','aku')] = ['error']
    parse_table[('O','dia')] = ['error']
    parse_table[('O','tia')] = ['error']
    parse_table[('O','anto')] = ['error']
    parse_table[('O','budi')] = ['error']
    
    parse_table[('O','suka')] = ['error']
    parse_table[('O','membaca')] =['error']
    parse_table[('O','melihat')] = ['error']
    parse_table[('O','menonton')] = ['error']
    parse_table[('O','sayang')] = ['error']
    
    parse_table[('O','kamu')] = ['kamu']
    parse_table[('O','film')] = ['film']
    parse_table[('O','buku')] = ['buku']
    parse_table[('O','surat')] = ['surat']
    parse_table[('O','anime')] = ['anime']

    parse_table[('O','kemarin')] = ['error']
    parse_table[('O','besok')] = ['error']
    parse_table[('O','banget')] = ['error']
    parse_table[('O','sekali')] = ['error']
    parse_table[('O','nanti')] = ['error']
    parse_table[('O','EOS')] = ['error']


    parse_table[('K','aku')] = ['error']
    parse_table[('K','dia')] = ['error']
    parse_table[('K','tia')] = ['error']
    parse_table[('K','anto')] = ['error']
    parse_table[('K','budi')] = ['error']
    
    parse_table[('K','suka')] = ['error']
    parse_table[('K','membaca')] =['error']
    parse_table[('K','melihat')] = ['error']
    parse_table[('K','menonton')] = ['error']
    parse_table[('K','sayang')] = ['error']
    
    parse_table[('K','kamu')] = ['error']
    parse_table[('K','film')] = ['error']
    parse_table[('K','buku')] = ['error']
    parse_table[('K','surat')] = ['error']
    parse_table[('K','anime')] = ['error']

    parse_table[('K','kemarin')] = ['kemarin']
    parse_table[('K','besok')] = ['besok']
    parse_table[('K','banget')] = ['banget']
    parse_table[('K','sekali')] = ['sekali']
    parse_table[('K','nanti')] = ['nanti']
    parse_table[('K','EOS')] = ['error']

        #stack initialization
    stack = []
    stack.append('#')
    stack.append('S')

    #input reading initialization
    idx_token = 0
    symbol = tokens[idx_token]

    #parse table process
    while (len(stack) > 0):
        top = stack[len(stack)-1]
        print('top = ', top)
        print('symbol = ', symbol)
        if top in terminals:
            print('top adalah simbol terminal')
            if top == symbol:
                stack.pop()
                idx_token = idx_token + 1
                symbol = tokens[idx_token]
                if symbol == "EOS":
                    stack.pop()
                    print('isi stack:', stack)
            else:
                print('error')
                break;
        elif top in non_terminals:
            print('top adalah simbol non-terminal')
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                symbol_to_be_pushed = parse_table[(top, symbol)]
                for i in range(len(symbol_to_be_pushed)-1,-1,-1):
                    stack.append(symbol_to_be_pushed[i])
            else:
                print('error')
                break;
        else:
            print('error')
            break;
        print('isi stack: ', stack)
        print()

    #conlusion
    print()
    if symbol == 'EOS' and len(stack) == 0:
        print('Input string ', '"', sentence,'"', ' diterima, sesuai Grammar')
    else:
        print('Error, input string:','"', sentence,'"', ', tidak diterima, tidak sesuai Grammar')

print("Terminal: aku - dia - tia - anto - budi | suka - membaca - melihat - menonton - sayang | kamu - film - buku - surat - anime | kemarin - besok - banget - sekali - nanti \n")
sentence = input("Masukkan kalimat: ") 
Parser(sentence)

