import os, subprocess, tempfile, time


command1 = ['cd', '/Users/yuji/Desktop']
command2 = ['open' , '/KCLHACKATHON3/output1.txt']
command3 = ['read' , '/Users/yuji/Desktop/KCLHACKATHON3/output1.txt']
command4 = ['chmod +x', '/Users/yuji/Desktop/KCLHACKATHON3/output.sh']
command5 = ['bash', '/Users/yuji/Desktop/KCLHACKATHON3/output.sh']
command6 = ['pwd']


shell = subprocess.Popen('/bin/bash', bufsize=0, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

while True:

    command = input("Enter command")

    input1 = str.encode(command +'; echo "<>< end"' + '\n')
    shell.stdin.write(input1)
    print('going to sleep')
    time.sleep(1)
    print('waking')
    for line in shell.stdout:
        if line == b'<>< end\n':
            break
        print('printing line')
        print(line)
    
#    proc = subprocess.Popen(command6, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#    print("chckpoint")
#    input1 = str.encode('pwd')
    
 #   proc.stdin.write(input1)
#    import time
#    time.sleep(2)
#    for line in shell.stdout:
#        print(line)
    
##   proc = subprocess.Popen(command4, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    
    
##    proc = subprocess.Popen(command3, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    ##stdout = subprocess.check_output(['ls'])

    ##print('Have %d bytes in output' % len(output))
#    print()
#    print(output)
