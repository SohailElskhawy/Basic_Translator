import tkinter as tk
from tkinter import ttk
from googletrans import Translator, constants


root = tk.Tk()
root.title("My Translator")
root.geometry("700x400")
root.config(bg="white")


app_name = tk.Label(root,text="My Translator",font=("arial",24,"bold"),bg="white")
app_name.place(x=250,y=0)

key_lang_list = list(constants.LANGUAGES.keys())
value_lang_list = list(constants.LANGUAGES.values())

def translate():
    output_label.delete("1.0",tk.END)
    translator = Translator()
    selected_lang = value_lang_list.index(user_out_lang.get())
    translation = translator.translate(user_input_box.get("1.0",tk.END),dest=key_lang_list[selected_lang])
    user_input_lang.set(constants.LANGUAGES[translation.src])
    output_label.insert("1.0",translation.text)




text_label = ttk.Label(root,text="Enter Text",font=("arial",18),background="white")
text_label.place(x=100,y=50)

user_input_lang = ttk.Combobox(root,values=value_lang_list,font=(10))
user_input_lang.place(x=100,y=90)
user_input_lang.set("choose language")

user_input_box = tk.Text(root,height=11,width=20,font=("arial", 18))
user_input_box.place(x=70,y=150)


user_out_lang = ttk.Combobox(root,values=value_lang_list,font=(10))
user_out_lang.set("choose language")
user_out_lang.place(x=370,y=90)

output_label = tk.Text(root,height=11,width=20,font=("arial", 18))
output_label.place(x=370,y=150)

translate_button = ttk.Button(root,text="Translate",command=translate)
translate_button.place(x=500,y=0)



root.mainloop()