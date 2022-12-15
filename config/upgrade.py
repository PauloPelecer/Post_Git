import os



cmd ='''
cd && rm -rf Post_Git
git clone https://github.com/SenhorLoock/Post_Git
cd Post_Git
python post_git.py
'''
try:
    os.system(cmd)
except:
    print ('Erro 304')