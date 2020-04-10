import csv
import string as st
        
def truck():
    filename="desktop/truckai.csv"
    fieds=[]
    rows=[]
    with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
 # extracting field names through first row 
        fields = next(csvreader) 
  
    # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
  
# printing the field names 
    print('Field names are:\n' + ', '.join(field for field in fields))
    print("\nWhich type of truck are u looking for?\nEnter a keyword to find trucks which suits you\n")
    keyword=input()
    print("\n\n")
    i=1
    for row in rows:
        for field in row:
            temp=field
            n=temp.find(keyword)
            if(n>-1) :
                i=i+1
                for x in row:
                    print(x)
                print('\n')
    if(i==1):
        print("\nTry to search with another keyword\n")
        truck()
        

def loader():
    filename="desktop/loaderai.csv"
    feids=[]
    rows=[]
    with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
 # extracting field names through first row 
        fields = next(csvreader) 
  
    # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
  
# printing the field names 
    print('Field names are:\n' + ', '.join(field for field in fields)) 
    print("\nWhich type of loader are u looking for?\nEnter a keyword to find loader which suits you\n")
    keyword=input()
    print("\n\n")
    
    i=1
    for row in rows:
        for field in row:
            temp=field
            n=temp.find(keyword)
            if (n>-1):
                i=i+1
                for x in row:
                    print(x)
                print('\n')
    if(i==1):
        print("\nTry to search with another keyword")
        loader()

def main():
    print("Welcome to section of  vehicles used to carry loads\n")
    print("Enter value:")
    print("1=> Trucks\n2=> Loaders\n")
    def entry():
        value=int(input())
        
        if(value==1):
            truck()
        elif(value==2):
            loader()
        else:
            print("Enter correct value\n")
            entry();
    entry()
main()
