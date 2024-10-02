from tkinter import *
from tkinter import ttk


main_window = Tk()
tree_view = ttk.Treeview(main_window)
tree_view.pack()
tree_view.insert('', '0', 'node1', text='First Node')
tree_view.insert('', '1', 'node2', text='Second Node')
tree_view.insert('', 'end', 'node3', text='Third Node')
logo = PhotoImage(file='python.gif').subsample(10,10)
tree_view.insert('node2', 'end', 'python', text='Python', image=logo)
tree_view.config(height=5)
tree_view.move('node2', 'node1', 'end')
tree_view.item('node1', open=True)
# print(tree_view.item('node2', 'open'))
# tree_view.detach('node3')
# tree_view.move('node3', 'node2', '0')
# tree_view.delete('node3')
# tree_view.move('node3', 'node2', '0')

tree_view.config(columns=('version'))
tree_view.column('version', width=100, anchor='center')
tree_view.column('#0', width=150)
tree_view.heading('version', text='Version')
tree_view.set('python', 'version', '3.10.7')
tree_view.set('node1', 'version', '0.0.1')
tree_view.item('python', tags=('programming'))
tree_view.tag_configure('programming', background='green')


def callback(event):
    print(tree_view.selection())


tree_view.bind('<<TreeviewSelect>>', callback)
tree_view.selection_add('node1')
tree_view.selection_remove('node1')







main_window.mainloop()