from redminelib import *
redmine = Redmine(r"https://redmine.it-alnc.ru", username = 'i.konkin', password = '12345678')
project = redmine.project.get('support')
issues = project.issues

def get_issue_url(issue):
    return 'https://redmine.it-alnc.ru/issues/{}'.format(issue.id)

def get_issue_message(issue):
    result = '<a href="{}">{}</a>'.format(get_issue_url(issue), '#'+str(issue.id) + ' ' + issue.subject)
    return result

def get_support_info():
    result = ''
    for res in issues.__iter__():
        result = result + get_issue_message(res)+'\n'
    return result