from tkinter import *


main_window = Tk()
text = Text(main_window, width=50, height=20)
text.pack()
text.config(wrap='word')
text.insert("1.0", 'This is a text for insertion into 1st line the text field\n')
text.insert("2.0", 'This is a text for insertion into the 2nd line text field')
text.insert("3.0 lineend", '\nThis is a text for.. \ninsertion into the text field')
print(text.get('2.0', '2.end'))
# text.delete('3.0', '3.0 lineend + 1 chars')
text.replace('1.0', '1.0 lineend', 'This is line that replaces the first')
# text.config(state='disabled')
# text.delete('1.0', 'end')

text.tag_add('custom_tag', '1.0', '1.8 wordend')
text.tag_config('custom_tag', background='red')
text.tag_remove('custom_tag', '1.0', '1.5')
print(text.tag_names())
text.tag_delete('custom_tag')
print(text.mark_names())
# text.insert('insert', '__')
# text.insert('current', '__')
text.mark_set('custom_mark', '1.3')
text.insert('custom_mark', '--mark insert--')
text.mark_gravity('custom_mark', 'left')
# text.mark_unset('custom_mark')
logo = PhotoImage(file='python.gif')
text.image_create('custom_mark', image=logo)
button = Button(text, text='Click me')
text.window_create('3.0', window=button)





main_window.mainloop()