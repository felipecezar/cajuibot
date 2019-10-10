import argparse
import getpass
from .runner import CajuiBot

class PasswordPromptAction(argparse.Action):
    def __call__(self, parser, args, values, option_string=None):
        if values is None:
            values = getpass.getpass()
        setattr(args, self.dest, values)

def main():
    parser = argparse.ArgumentParser(prog='pycajui',
        description='Ferramenta para automatizar o uso do Cajui')
    parser.add_argument('-u','--user', type=str, required=True, 
        help='Nome de usuário do Cajui')
    parser.add_argument("-p", "--password", type=str, action=PasswordPromptAction, nargs='?', 
        help='Senha de acesso ao Cajui')
    parser.add_argument('-l', '--lesson', required=True, 
        help='Arquivo CSV com lançamento das aulas')
    parser.add_argument('--headless', action='store_true',
        help='Ativa o modo de execução sem exibir a interface do usuário')

    args = parser.parse_args()
    
    bot = CajuiBot(args.user,args.password,args.lesson,args.headless)
    bot.login()
    bot.lancarTodasAulas()

if __name__ == '__main__':
    main()
