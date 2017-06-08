import os,sys
def load(argv):
    try:
        exec(open(argv[0]+'.py').read(),globals())
        global mod
        mod = module()
    except:
        print('[-] No or not existent module to load provided')
def h(argv):
    try:
        print(mod.help)
    except:
        print('[-] No module loaded')
def info(argv):
    try:
        print(mod.description)
        print(mod.help)
    except:
        print('[-] No module loaded')
def run(argv):
    try:
        mod.main()
    except:
        print('[-] No module loaded')
def loaded(argv):
    try:
        print(mod.name)
    except:
        print('[-] No module loaded')
def cmdl(argv):
    for cmd in commands:
        print(cmd)
def clear(argv):
    os.system('clear')
def exit(argv):
    print('Shutdown')
    sys.exit(1)
def set(argv):
    try:
        exec('mod.'+argv[0]+'='+argv[1])
        print(argv[0]+' = '+argv[1])
    except:
        print('[-] Eroor')
commands = {'load':load,'help':h,'info':info,'run':run,'loaded':loaded,'cmdl':cmdl,'clear':clear,'exit':exit,'set':set}
def runner():
        useri = input('z > ')
        command = useri.split(' ')[0]
        if command in commands:
            commands[command](useri.split(' ')[1:])
        elif useri == '':
            pass
        else:
            print('[-] Command not found')
while True:
    runner()
    
