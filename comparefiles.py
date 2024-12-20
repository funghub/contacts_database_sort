import csv

# reading the eventbrite file and adding those emails into a list inside a dictionary
with open('eventbrite.csv', mode = 'r') as eb_file:
    eventbrite = csv.DictReader(eb_file)
    email_list = [line['Email'] for line in eventbrite]    
        
    eb_dict = dict()
    eb_dict['Email'] = email_list

    # print(eb_dict)

# reading the wix file and adding those emails and subscriber statuses as a tuple into a list
with open('wix.csv', mode = 'r', encoding='utf-8-sig') as wix_file:
    wix = csv.DictReader(wix_file)
    # email_list = [line['Email'] for line in wix]    

    wix_list = []
    for row in wix:
        wix_list.append((row['Email'], row['Email subscriber status']))
    
    # print(wix_list)

emails_in_wix = [e[0] for e in wix_list]

emails_not_in_wix1 = set(eb_dict['Email']).difference(set(emails_in_wix))
# print(emails_not_in_wix1)

emails_not_in_wix2 = [email for email in eb_dict['Email'] if email not in [e[0] for e in wix_list] ]
print('Emails in Eventbrite not in Wix')
print(emails_not_in_wix2)
# PRINT THESE INTO A NEW CSV


# print([entry for entry in wix_list if (entry[0] not in emails_not_in_wix1 and entry[0] in eb_dict['Email'] and entry[1] == 'Unsubscribed')]) # emails in wix and in eventbrite and unsubscribed
print('\nEmails in Eventbrite and Wix, but unsubscribed')
emails_eb_wix_not_sub = [entry for entry in wix_list if (entry[0] in emails_in_wix and entry[0] in eb_dict['Email'] and entry[1] == 'Unsubscribed')]
print(emails_eb_wix_not_sub) # emails in wix and in eventbrite and unsubscribed

# print([entry for entry in wix_list if (entry[0] in emails_in_wix and entry[0] in eb_dict['Email'] and entry[1] == 'Subscribed')]) # emails in wix and in eventbrite and subscribed