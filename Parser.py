import string
import streamlit as st

def subjectRecognizer(word):
    alphabet_list = list(string.ascii_lowercase)
    state_list = [
                'q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10',
                'q11','q12'
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
    transition_table[("q12", "#")] = "accept"
    transition_table[("q12", " ")] = "q12"

    #Untuk kata "aku"
    transition_table[("q0","a")] = "q1"
    transition_table[("q1","k")] = "q2"
    transition_table[("q2","u")] = "q12"

    #Untuk kata "dia"
    transition_table[("q0","d")] = "q5"
    transition_table[("q5","i")] = "q6"
    transition_table[("q6","a")] = "q12"

    #Untuk kata "tia"
    transition_table[("q0","t")] = "q7"
    transition_table[("q7","i")] = "q8"
    transition_table[("q8","a")] = "q12"

    #Untuk kata "anto"
    transition_table[("q0","a")] = "q1"
    transition_table[("q1","n")] = "q3"
    transition_table[("q3","t")] = "q4"
    transition_table[("q4","o")] = "q12"

    #Untuk kata "budi"
    transition_table[("q0","b")] = "q9"
    transition_table[("q9","u")] = "q10"
    transition_table[("q10","d")] = "q11"
    transition_table[("q11","i")] = "q12"

    idx_char = 0
    state = 'q0'
    current_token = ''
    while state!='q12':
        current_char = word[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state=='q12':
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
    transition_table[("q0","m")] = "q8"
    transition_table[("q8","e")] = "q9"
    transition_table[("q9","m")] = "q10"
    transition_table[("q10","b")] = "q11"
    transition_table[("q11","a")] = "q12"
    transition_table[("q12","c")] = "q13"
    transition_table[("q13","a")] = "q23"

    #Untuk kata "menonton"
    transition_table[("q0","m")] = "q8"
    transition_table[("q8","e")] = "q9"
    transition_table[("q9","n")] = "q18"
    transition_table[("q18","o")] = "q19"
    transition_table[("q19","n")] = "q20"
    transition_table[("q20","t")] = "q21"
    transition_table[("q21","o")] = "q22"
    transition_table[("q22","n")] = "q23"

    #Untuk kata "melihat"
    transition_table[("q0","m")] = "q8"
    transition_table[("q8","e")] = "q9"
    transition_table[("q9","l")] = "q14"
    transition_table[("q14","i")] = "q15"
    transition_table[("q15","h")] = "q16"
    transition_table[("q16","a")] = "q17"
    transition_table[("q17","t")] = "q23"

    #Untuk kata "sayang"
    transition_table[("q0","s")] = "q1"
    transition_table[("q1","a")] = "q4"
    transition_table[("q4","y")] = "q5"
    transition_table[("q5","a")] = "q6"
    transition_table[("q6","n")] = "q7"
    transition_table[("q7","g")] = "q23"

    idx_char = 0
    state = 'q0'
    current_token = ''
    while state!='accept':
        current_char = word[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state=='q23':
            return True
        if state== 'error':
            return False
        idx_char = idx_char + 1
    return False

def objectRecognizer(word):
    alphabet_list = list(string.ascii_lowercase)
    state_list = [
                'q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10',
                'q11','q12','q13','q14','q15','q16','q17','q18'
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
    transition_table[("q18", "#")] = "accept"
    transition_table[("q18", " ")] = "q18"

    #Untuk kata "kamu"
    transition_table[("q0","k")] = "q1"
    transition_table[("q1","a")] = "q2"
    transition_table[("q2","m")] = "q3"
    transition_table[("q3","u")] = "q18"

    #Untuk kata "film"
    transition_table[("q0","f")] = "q4"
    transition_table[("q4","i")] = "q5"
    transition_table[("q5","l")] = "q6"
    transition_table[("q6","m")] = "q18"

    #Untuk kata "buku"
    transition_table[("q0","b")] = "q7"
    transition_table[("q7","u")] = "q8"
    transition_table[("q8","k")] = "q9"
    transition_table[("q9","u")] = "q18"

    #Untuk kata "surat"
    transition_table[("q0","s")] = "q10"
    transition_table[("q10","u")] = "q11"
    transition_table[("q11","r")] = "q12"
    transition_table[("q12","a")] = "q13"
    transition_table[("q13","t")] = "q18"

    #Untuk kata "anime"
    transition_table[("q0","a")] = "q14"
    transition_table[("q14","n")] = "q15"
    transition_table[("q15","i")] = "q16"
    transition_table[("q16","m")] = "q17"
    transition_table[("q17","e")] = "q18"

    idx_char = 0
    state = 'q0'
    current_token = ''
    while state!='q18':
        current_char = word[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state=='q18':
            return True
        if state== 'error':
            return False
        idx_char = idx_char + 1
    return False

def keteranganRecognizer(word):
    alphabet_list = list(string.ascii_lowercase)
    state_list = [
                'q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10',
                'q11','q12','q13','q14','q15','q16','q17','q18','q19','q20',
                'q21','q22','q23','q24'
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
    transition_table[("q24", "#")] = "accept"
    transition_table[("q24", " ")] = "q18"

    #Untuk kata "kemarin"
    transition_table[("q0","k")] = "q1"
    transition_table[("q1","e")] = "q2"
    transition_table[("q2","m")] = "q3"
    transition_table[("q3","a")] = "q4"
    transition_table[("q4","r")] = "q5"
    transition_table[("q5","i")] = "q6"
    transition_table[("q6","n")] = "q24"


    #Untuk kata "besok"
    transition_table[("q0","b")] = "q7"
    transition_table[("q7","e")] = "q12"
    transition_table[("q12","s")] = "q13"
    transition_table[("q13","o")] = "q14"
    transition_table[("q14","k")] = "q24"

    #Untuk kata "banget"
    transition_table[("q0","b")] = "q7"
    transition_table[("q7","a")] = "q8"
    transition_table[("q8","n")] = "q9"
    transition_table[("q9","g")] = "q10"
    transition_table[("q10","e")] = "q11"
    transition_table[("q11","t")] = "q24"

    #Untuk kata "sekali"
    transition_table[("q0","s")] = "q15"
    transition_table[("q15","e")] = "q16"
    transition_table[("q16","k")] = "q17"
    transition_table[("q17","a")] = "q18"
    transition_table[("q18","l")] = "q19"
    transition_table[("q19","i")] = "q24"

    #Untuk kata "nanti"
    transition_table[("q0","n")] = "q20"
    transition_table[("q20","a")] = "q21"
    transition_table[("q21","n")] = "q22"
    transition_table[("q22","t")] = "q23"
    transition_table[("q23","i")] = "q24"

    idx_char = 0
    state = 'q0'
    current_token = ''
    while state!='q24':
        current_char = word[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state=='q24':
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
        elif predicateRecognizer(word):
            terminal.append('P')
        elif objectRecognizer(word):
            terminal.append('O')
        elif keteranganRecognizer(word):
            terminal.append('K')
        else:
            terminal.append('INVALID')
    return terminal


def Parser(sentence):
    st.write("\n - Parser  \n")
    tokens = sentence.lower().split()
    tokens.append('EOS')
    logic = True
    # symbols definition
    non_terminals = ['S','SB','P','O','K']
    terminals = ['aku','dia','tia','anto','budi',
                'suka','membaca','melihat','menonton','sayang',
                'kamu','film','buku','surat','anime',
                'kemarin','besok','banget','sekali','nanti'
                ]

    parse_table = {}
    if len(tokens) >= 3 :
        if tokens[1] == 'membaca' and (tokens[2] == 'film' or tokens[2] == 'anime'):
            logic = False
        elif tokens[1] == 'menonton' and (tokens[2] == 'buku' or tokens[2] == 'surat'):
            logic = False
        elif (tokens[1] == 'suka' or tokens[1] == 'sayang') and (tokens[2] == 'surat'):
            logic = False

    terminal = tokenRecognizer(sentence)
    print(terminal)
    if terminal == ['SB','P','O']:                 
        parse_table[('S','aku')] = ['SB', 'P', 'O']
        parse_table[('S','dia')] = ['SB', 'P', 'O']
        parse_table[('S','tia')] = ['SB', 'P', 'O']
        parse_table[('S','anto')] = ['SB', 'P', 'O']
        parse_table[('S','budi')] = ['SB', 'P', 'O'] 
    elif terminal == ['SB','P']: 
        parse_table[('S','aku')] = ['SB', 'P']
        parse_table[('S','dia')] = ['SB', 'P']
        parse_table[('S','tia')] = ['SB', 'P']
        parse_table[('S','anto')] = ['SB', 'P']
        parse_table[('S','budi')] = ['SB', 'P'] 
    elif terminal == ['SB','P','K']:
        parse_table[('S','aku')] = ['SB', 'P', 'K']
        parse_table[('S','dia')] = ['SB', 'P', 'K']
        parse_table[('S','tia')] = ['SB', 'P', 'K']
        parse_table[('S','anto')] = ['SB', 'P', 'K']
        parse_table[('S','budi')] = ['SB', 'P', 'K'] 
    elif terminal == ['SB','P','O','K']:
        parse_table[('S','aku')] = ['SB', 'P','O', 'K']
        parse_table[('S','dia')] = ['SB', 'P','O', 'K']
        parse_table[('S','tia')] = ['SB', 'P','O', 'K']
        parse_table[('S','anto')] = ['SB', 'P', 'O','K']
        parse_table[('S','budi')] = ['SB', 'P','O', 'K']     
    else:
        st.write("INPUTAN ANDA TIDAK DITERIMA, TIDAK SESUAI STRUKTUR !!")
        return
         
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
        st.write('top = ', top)
        st.write('symbol = ', symbol)
        if top in terminals:
            st.write('top adalah simbol terminal')
            if top == symbol:
                stack.pop()
                idx_token = idx_token + 1
                symbol = tokens[idx_token]
                if symbol == "EOS":
                    stack.pop()
                    st.write('isi stack:', stack)
            else:
                st.write('error')
                break;
        elif top in non_terminals:
            st.write('top adalah simbol non-terminal')
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                symbol_to_be_pushed = parse_table[(top, symbol)]
                for i in range(len(symbol_to_be_pushed)-1,-1,-1):
                    stack.append(symbol_to_be_pushed[i])
            else:
                st.write('error')
                break;
        else:
            print('error')
            break;
        st.write('isi stack: ', stack)
        print("\n====== ========= ====== \n")

        print()

    #conlusion
    print()
    if symbol == 'EOS' and len(stack) == 0:
        if not logic :
            teks = "SESUAI STRUKTUR/DITERIMA NAMUN TIDAK LOGIS"
        else:
            teks = "SESUAI STRUKTUR/DITERIMA DAN LOGIS"
        # Menggabungkan semua bagian teks menjadi satu string
        output = f'Input string "{sentence}" : <b>{teks}</b>'
        # Menampilkan teks dalam satu baris tanpa pemisah baris
        st.write(output, unsafe_allow_html=True)
       
    else:
        st.write('Error, input string:','"', sentence,'"', ', tidak diterima, tidak sesuai Grammar')
def header() :
    st.title("TOKEN RECOGNIZER & PARSER DALAM PENGECEKAN STRUKTUR BAHASA INDONESIA")
    print("=======================================")
    #st.subheader("            SELAMAT DATANG         ")
    print("=======================================")
    st.sidebar.subheader("  TUGAS BESAR TEORI BAHASA DAN AUTOMATA")
    print("=======================================")
    st.sidebar.markdown("<h2 style='text-align: center;'>IF-46-02</h2>", unsafe_allow_html=True)
    print("=======================================")
    st.sidebar.subheader("By:")
    st.sidebar.write("- Joshua Pinem (1301223051)")
    st.sidebar.write("- Zaky Al Fatih Nata Imam (1301223172)")
    st.sidebar.write("- Yosia Parade Banua Sinaga (1301220190)")

    


def struktur(sentence):
    terminal = tokenRecognizer(sentence)
    tokens = sentence.lower().split()
    st.subheader("\n Token Recognizer  \n")
    st.write(" - Struktur kalimat : ",terminal)
    for word in tokens:
        if subjectRecognizer(word) :
            st.write(word, " : ","Subjek")
        elif predicateRecognizer(word):
            st.write(word, " : ","Predikat")
        elif objectRecognizer(word):
            st.write(word, " : ","Objek")
        elif keteranganRecognizer(word):
            st.write(word, " : ","Keterangan")
        else:
            st.write(word, " : ","Tidak Valid")
    print("\n============================== \n")



def mainParser():
    header()  
    terminal = 'Terminal:\n aku - dia - tia - anto - budi | suka - sayang - membaca - melihat - menonton | kamu - buku - anime - surat - film | kemarin - besok - nanti - banget - sekali'
    st.write(f'<b>{terminal}</b>', unsafe_allow_html=True)
    sentence = st.text_input("Masukan kalimat di sini:  ")
    struktur(sentence)
    Parser(sentence)

mainParser()