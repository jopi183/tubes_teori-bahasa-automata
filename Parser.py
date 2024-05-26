def Parser(sentence):
    print("\n====== Parser ====== \n")
    tokens = sentence.lower().split()
    tokens.append('EOS')
    # symbols definition
    non_terminals = ['S','SB','P','O','K']
    terminals = ['aku','dia','tia','anto','budi'
                'suka','membaca','melihat','menonton','sayang',
                'kamu','film','buku','surat','anime',
                'kemarin','besok','banget','sekali','nanti'
                ]

    parse_table = {}

    parse_table[('S','aku')] = [['SB', 'P', 'O'], ['SB', 'P', 'K'], ['SB', 'P', 'O', 'K'],['SB','P']]
    parse_table[('S','dia')] = [['SB', 'P', 'O'], ['SB', 'P', 'K'], ['SB', 'P', 'O', 'K'],['SB','P']]
    parse_table[('S','tia')] = [['SB', 'P', 'O'], ['SB', 'P', 'K'], ['SB', 'P', 'O', 'K'],['SB','P']]
    parse_table[('S','anto')] = [['SB', 'P', 'O'], ['SB', 'P', 'K'], ['SB', 'P', 'O', 'K'],['SB','P']]
    parse_table[('S','budi')] = [['SB', 'P', 'O'], ['SB', 'P', 'K'], ['SB', 'P', 'O', 'K'],['SB','P']]
    
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
    if symbol == 'EOS' and len(stack)== 0:
        print('Input string ','"', sentence,'"', ' diterima, sesuai Grammar')
    else:
        print('Error, input string:','"', sentence,'"', ', tidak diterima, tidak sesuai Grammar')

    return Parser
