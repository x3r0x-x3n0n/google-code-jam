### Problem 2 -- You can go your own way
import sys

def mirror(path):
    mypath = ''
    for p in path:
        if p == 'E':
            mypath += 'S'
        if p == 'S':
            mypath += 'E'
            
    return mypath
    
def main():
    test = int(sys.stdin.readline())
    
    for t in range(test):
        n = int(sys.stdin.readline())
        p = sys.stdin.readline()
        print "Case #%s: %s" %(t+1, mirror(p))
        


if __name__ == '__main__':
    main()
