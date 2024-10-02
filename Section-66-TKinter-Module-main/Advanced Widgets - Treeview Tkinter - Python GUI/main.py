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
print(tree_view.item('node2', 'open'))
tree_view.detach('node3')
tree_view.move('node3', 'node2', '0')
tree_view.delete('node3')
tree_view.move('node3', 'node2', '0')

main_window.mainloop()