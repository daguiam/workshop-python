import script1
def print_message():
    print 'Hello this is script 2'

if __name__ == "__main__":
    print 'Executing from script2'
    print_message()
    script1.print_message()