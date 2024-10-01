import shelve

with shelve.open('shelve_file') as sh_file:
  sh_file['my_list'] = [1, 2, 3, 4, 5]
  print(sh_file['my_list'])
