import shelve

with shelve.open('shelve_file') as sh_file:
  sh_file['miller'] = 'a person who owns or works in corn mill'
  sh_file['programmer'] = 'a person who writes computer programs'
  sh_file['app'] = 'an application, especially as downloaded by a user to a mobile device'
  for value in sh_file.values():
      print(value)