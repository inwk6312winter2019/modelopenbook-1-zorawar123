fout=open('running-config.cfg','r')
def get_access_list(fout): # fuction defined with  Parameter 
  fout.seek(0)
  transit_list=[] # empty list 
  global_list=[]
  fw_access_in=[]
  for i  in fout: #stripping the list  
    i=i.strip()
    if str == 'access-list' in i:
      if str == 'transit_access_in' in i:
        transit_list.append(line)
      elif str == 'global_access' in i:
        global_list.append(line)
      elif 'fw-management_access_in' in i:
        fw_access_in.append(line)
        print(transit_list)
        print(global_list)
        print(fw_access_in)
      
print(get_access_list(fout))
