#Liv Sutton
#3061407
#Lab 02 9/18/22
# To simulate a CPU scheduler 



from executive import Executive

def main():
    #access and run the file
    filename = "test2.txt"
    my_exec = Executive(filename)
    my_exec.run()   

if __name__ == '__main__':
    main()