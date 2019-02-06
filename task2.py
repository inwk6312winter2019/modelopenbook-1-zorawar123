book ="running-config.cfg"

book ='running-config.cfg'
with open(book, 'r') as fd:
  words = fd.read().split()
  def list_ifname_ip():
    d = {} 
    for i in words(): # will scane words from the book 
      if i not in d: #  chck the words present in empty dictionary
        d[i]=1 # will assign the values to the dictionary
      else:
        d[i]+=1
    print(d)# print dictinary
    g = d.items() # view of the dictionary in  items of  key, value
    l = []
    for key,value in g:     # as g is the dictionary and have values in term of keys and values becaus of function item()
      if str == "nameif" in g:
        l.append(key,value)
     print("The given list is",l)
     """ This is the program for Task 2 """
     for k in words:
       k=  k.replace('192', '10') # I am replacing the value 192 with 10 by using inbuilt replace function
       k = k.replace('172', '10')  # I am replacing the value 192 with 10 by using inbuilt replace function
       k = k.replace("255.255.0.0","255.0.0.0")
       k = k.replace("255.255.225.0","255.0.0.0")
     print(k)
list ifname_ip()
