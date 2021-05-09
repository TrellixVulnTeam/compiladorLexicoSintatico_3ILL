#pip install sly
from sly import Lexer

class CalcLexer(Lexer):

    # Set of token names.   This is always required
    tokens = {
    ALGORITMO,VAR,VERDADEIRO,FALSO,FUNCAO,FIMFUNCAO,ID,REAL,INTEIRO,
    CARACTERE,LOGICO, SE, ENTAO,SENAO,FIMSE,ENQUANTO,FACA,REPITA,FIMREPITA,
    FIMENQUANTO,ESCREVA,E,OU,NAO,LEIA, LIMPATELA, PROCEDIMENTO,
    FIMPROCEDIMENTO, ESCOLHA, FIMESCOLHA, VETOR, ASC, TIMER, CARAC, ECO,
    LE, LT ,GE, GT,EQ, NE, ASSIGN,MOD, RETORNE, POS, XOU, CRONOMETRO
    }#Nome dos tokens devem estar em maiusculo
    #O valor de cada chave desse dicionario sera definido durante a execução


    literals = {'+','-','*','/','^','(', ')', ':', '\\', '%'} #caracteres literais, o token é representado pelo proprio simbolo


    ###Caracteres Ignorados###

    ###As variáveis que começam com o nome ignore, serão ignoradas pelo analisador léxico
    # String containing ignored characters between tokens
    ignore = ' \t'#ignora espaços entre os tokens
    ignore_comment = r'([//].+)' #ignora as linhas que são comentáriosc
    ignore_newline = r'\n+'  #ignora varias linhas vazias
    ####################################################

    # Regular expression rules for tokens -- Aqui será definido as expressoes regulares que caracterizam os tokens definidos antes
    REAL = r'(real|[0-9]+.[0-9]+)'#se for a palavra reservada ou (um conjunto de digitos . conjunto de digitos) é do tipo real
    INTEIRO = r'(inteiro|[0-9]+)' #se for a palavra reservada ou um conjunto de digitos é do tipo inteiro
    CARACTERE = r'(caractere|"[^\n]+"|"")'#se for a palavra reservada ou qualquer coisa que n seja \n no texto entao é caracter
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*' #variavel que começa com alguma letra maiuscula ou minuscula
    NE      = r'<>' #diferença - not equal
    ASSIGN  = r'<-' #atribuição
    LE      = r'<=' #menor que
    LT      = r'<'  #menor
    GE      = r'>=' #maior que
    GT      = r'>'  #maior
    EQ     = r'==' #comparação
    

    # Caracteres especiais / palavras reservadas / Definir todas aqui
    ID['var'] = VAR
    ID['MOD'] = MOD
    ID['algoritmo'] = ALGORITMO
    ID['verdadeiro'] = VERDADEIRO
    ID['falso'] = FALSO
    ID['funcao'] = FUNCAO
    ID['fimfuncao'] = FIMFUNCAO
    ID['procedimento'] = PROCEDIMENTO
    ID['fimprocedimento'] = FIMPROCEDIMENTO
    ID['escolha'] = ESCOLHA
    ID['fimescolha'] = FIMESCOLHA
    ID['repita'] = REPITA
    ID['fimrepita'] = FIMREPITA
    ID['enquanto'] = ENQUANTO
    ID['faca'] = FACA
    ID['fimenquanto'] = FIMENQUANTO
    ID['limpatela'] = LIMPATELA
    ID['se'] = SE
    ID['entao'] = ENTAO
    ID['senao'] = SENAO
    ID['fimse'] = FIMSE
    ID['escreva'] = ESCREVA
    ID['logico'] = LOGICO
    ID['e'] = E 
    ID['ou'] = OU
    ID['nao'] = NAO
    ID['leia'] = LEIA
    ID['vetor'] = VETOR
    ID['retorne'] = RETORNE
    ID['pos'] = POS
    ID['xou'] = XOU
    ID['cronometro'] = CRONOMETRO
    ID['asc'] = ASC
    ID['timer'] = TIMER
    ID['carac'] = CARAC
    ID['eco'] = ECO

    # Define a rule so we can track line numbers
    @_(r'\n+')
    def ignore_newline(self, t):#função que auxilia a funcao error(contando as linhas do algoritmo), no qual irá mostrar qual linha que dá erro lexico 
        self.lineno += len(t.value)
    def error(self, t):#funçãoq que mostra erro lexico na linha do algoritmo dado como entrada
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1

if __name__ == '__main__':
    arquivo = open('algoritmo.txt', 'r')
    data = arquivo.read()
    arquivo.close()
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))
    