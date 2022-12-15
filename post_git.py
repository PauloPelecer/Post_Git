from config import System


profile = System.read_json('config/Profile/profile.json')

    
'''
git remote add origin https://github.com/SenhorLoock/Post_Git.git
git branch -M main
git push -u origin main
'''


def get_dados():    
    arqs = input(str('Digite o Nome do Arquivo: '))
    
    link = input(str('Digite o Link do Git: '))
    commit = input(str('Numero da Versão: '))
    diretory = input(str('Digite o Local Do Projeto: '))
    return arqs, link, commit, diretory
def push(l,a,c, d):
    dir = '/storage/emulated/0/'+d
    cmd_1 = f'''
cd 
cd {dir}
rm -rf README.md
rm -rf .git
    '''
    System.command(cmd_1)
    cmd_2 = f'''
cd 
cd {dir}
echo "# {a}" >> README.md
git init
git config --global --add safe.directory {dir}
sleep 1.0
git add .
git commit -m "{c}"
git branch -M main
git remote add origin {l}
git push -u origin main


    '''
    System.command('clear')
    
    try:
        System.main()
        System.command(cmd_2)
        
        #System.command('clear')            
        print ('Upload Concluido!')
    except:
        print ('Erro...')
        
if __name__ == '__main__':
  System.command('clear')
  System.command('mkdir check')
  System.main()
  System.options()
  try:
      response = System.cursor()
      if response == '01' or response == '1':
          arqs, link, commit, diretory = get_dados()
          push(link, arqs, commit, diretory)
      elif response == '02' or response == '2':
          cmd = 'cd check && wget https://raw.githubusercontent.com/SenhorLoock/Post_Git/main/config/profile/Profile.json'
          System.command(cmd)
          show_input = System.read_json('check/Profile.json')
          if profile[0] == show_input[0]:
              print ('Versão Atualizada')
              System.command('rm -rf check')  
          else:
              print ('Versão Ultrapassada\nBaixando arquivos Atualizados!')
              System.command('rm -rf check')
              System.command('sleep 1.0')
              cmd_up = 'cd config && python upgrade.py'
              System.command(cmd_up)
              exit()
      elif response == '03' or response == '3':
          System.main()
          print (f'\033[0;33mName Tool: {profile[1]}\nAuthor: {profile[2]}\nGitHub: {profile[3]}\033[0;m')  
      else:
          
          System.command('clear')
          System.command('rm -rf check')
          System.off()
          print ('Exit Programming...')
  
  except:
      System.command('clear')
      System.command('rm -rf check')
      System.off()