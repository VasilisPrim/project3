###########################################
# Μην αλλάξετε τη συνάρτηση contact2csv   #
###########################################
def contact2csv(name, info):
        
	'''Takes the name (key) and info (value) of a phonebook contact,
	converts it to a string of comma separated values and returns it'''

	return  name[0] + ',' + name[1] + ','\
			+ str(info['email']) + ","\
			+ str(info['phone']['mobile']) + ','\
			+ str(info['phone']['home']) + ','\
			+ str(info['phone']['other']) + ','\
			+ "+".join(sorted(info['tags'])) + '\n'



###########################################
# Υλοποιήστε τις παρακάτω συναρτήσεις και #
# όσες δικές σας κρίνετε πως χρειάζονται. #
###########################################
def charposition(string, char):# Συνάρτηση για να εντοπίζει τη θέση της τελείας στο email
        pos = [n for n in range(len(string)) if string[n] == char]
        return pos
def email_check(email):# Συνάρτηση για να ελέγχει την τρίτη απαίτηση του μεϊλ
        partmail = email[(email.index('@') + 1):]
        pos = charposition(partmail,'.')
        if len(pos) > 1:
                for i in range(len(pos) - 1):
                        if pos[0] >= 2 and (len(partmail) - pos[len(pos) - 1]) >= 3 and abs(pos[i] - pos[i+1]) >= 3:
                                x = True
                        else:
                                return None
                return x    
        else:
                if pos[0] >= 2 and (len(partmail) - pos[len(pos) - 1]) >= 3:
                        return True
                else:
                        return None

def add_contact(phbook):
        entered_contact = input('Enter contact in CSV format: ').split(',')
        print()
        name = (entered_contact[0],entered_contact[1])
        info = dict()
        info['phone'] = dict()
        if name in phbook:
                print('Contact',entered_contact[0]+','+entered_contact[1],'already exists.')
        else:
                info['email'] = entered_contact[2]
                info['phone']['mobile'] = entered_contact[3]
                info['phone']['home'] = entered_contact[4]
                info['phone']['other'] = entered_contact[5]
                info['tags'] = entered_contact[6].split('+')
                phbook[name] = info
                print('Contact',entered_contact[0]+','+entered_contact[1],'added.')

def search_by_name(phbook):
        partial_name = input('Enter partial name: ').lower()
        print()
        names_list = []
        for (last,first) in phbook:
                if partial_name  in last.lower() or partial_name in first.lower():
                        names_list.append((last,first))
        
        if names_list == []:
                print('No results.')
                return None
        names_found = sorted(names_list)
        k = 1
        for i in names_found:
                print(str(k)+'.',i[0]+', '+i[1])
                k += 1
        while True:
                result = int(input('Choose result: '))
                print()
                if result > k-1 or result < 1:
                        print('Choose between 1 and',str(k-1)+'.')
                        continue
                else:
                        print(contact2csv(names_found[result-1],phbook[names_found[result-1]]))
                        return names_found[result-1]
         

def update_contact(phbook):
        search_value = search_by_name(phbook)
        fields = ['email','phone','tags']
        if search_value == None:
                print('Contact not found.')
        else:
                while True:
                        field = input('Field to update: ')
                        print()
                        if field not in fields:
                                print('Invalid field',field+'.')
                                continue
                        else:
                                new_value = input('New value: ')
                                print()
                                break
                if field == 'email':
                        if new_value.count('@') == 1 and '.' in new_value[(new_value.index('@')+ 1):] and email_check(new_value) is True:
                                phbook[search_value]['email'] = new_value
                                print('Email updated.')
                                
                        else:
                                print('Invalid email',new_value+'.')
        
                elif field == 'phone':
                        
                        if new_value.isdigit() is False:
                                
                                print('Invalid phone',new_value+'.')
                        else:
                                if new_value[0] == '2':
                                        phbook[search_value]['phone']['home'] = new_value
                                elif new_value[0] == '6':
                                        phbook[search_value]['phone']['mobile'] = new_value
                                else:
                                      phbook[search_value]['phone']['other'] = new_value  
                                print('Phone updated.')

                else:
                        if phbook[search_value]['tags'] == ['-']:
                                phbook[search_value]['tags'].remove('-')
                        
                        if new_value.lower() not in phbook[search_value]['tags']:
                                
                                phbook[search_value]['tags'].append(new_value)
                                print('Tags updated.')
                        else:
                                print('Tag',new_value,'exists.')

def lower_list(lista):# Έκανα αυτή τη συνάρτηση γιατί η conta2csv μου επέστρεφε τα tags αλλαγμένα
        empty = []# Η empty είναι κενή λίστα για αποθήκευση των τιμών της λίστας των tags
        for tag in lista:
                empty.append(tag)
        for i in range(len(lista)):
                empty[i] = empty[i].lower()
        return empty        

def search_tag(phbook):
        tags = input('Enter tags: ').split(',')
        print()
        for tag in sorted(tags):
                k = 0
                print(tag+':')
                for (name,value) in sorted(phbook.items()):
                        if tag.lower() in lower_list(list(value.values())[2]):
                                print('\t',contact2csv(name, value),sep='')
                                k += 1
                if k == 0:
                        print('\tNo results.\n')
                        

	
###########################################
# Μην αλλάξετε τίποτα από εδώ και κάτω.   #
###########################################

def phonebook2csv(phbook):
	'''Takes a project3 phonebook, converts it to a string of 
	comma separated values and returns the string'''

	contact = 'Last,First,Email,Mobile,Home,Other,Tags\n'
	for (name, info) in sorted(phbook.items()):
		contact += contact2csv(name, info)
	return contact
  
def menu():
	'''Prints menu'''

	print('\n--------------------')
	print('[A/a]dd contact')
	print('[U/u]pdate contact')
	print('Search by [N/n]ame')
	print('Search by [T/t]ags')
	print('[P/p]rint')
	print('[F/f]inish\n')


def main():
	phonebook = dict()
	while True:
		menu()
		action = input().strip().lower()
		if action == 'a':
			add_contact(phonebook)
		elif action == 'u':
			update_contact(phonebook)
		elif action == 'n':
			search_by_name(phonebook)
		elif action == 't':
			search_tag(phonebook)
		elif action == 'p':
			print(phonebook2csv(phonebook))
		elif action == 'd': # special delimiter for autolab
			print('\n##')
		elif action == 'f':
			return
		else: 
			print('\nInvalid action. Try again.')
			

if __name__ == '__main__':
	main()
        
    
