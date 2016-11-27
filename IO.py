import os, subprocess, tempfile, time

class ShellManager:
    
    def __init__(self, bashPath):
        self.shell = subprocess.Popen(bashPath, bufsize=0, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    
    def getOutput(self, command):
        input1 = str.encode(command +'; echo "<>< end"' + '\n')
        self.shell.stdin.write(input1)
        outputString = []
        for line in self.shell.stdout:
            if line == b'<>< end\n':
                break
            outputString.append(line.decode("utf-8"))
        outputString = ''.join(outputString)
        return outputString

    def exitProgram(self):
        self.shell.kill()
        
            
    
