from redminelib import *
redmine = Redmine(r"https://redmine.it-alnc.ru", username = 'i.konkin', password = '12345678')
project = redmine.project.get('fbid_support')
print(type(project))