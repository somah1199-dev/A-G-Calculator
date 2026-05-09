import tkinter as tk
from tkinter import messagebox
#計算式
def A_G():
    try:
        TP=float(TP_entry.get())
        AL=float(AL_entry.get())
        if TP==AL:
            messagebox.showerror("エラー","TP,ALBが同じ値です")
            return
        AG=AL/(TP-AL)
        kekka.configure(text=f"A/G比={AG:.1f}")
    except ValueError:
        messagebox.showerror("エラー","数字を入力してください")
def clear():
    TP_entry.delete(0, tk.END)
    AL_entry.delete(0, tk.END)
    kekka.configure(text="")
#ウィンドウ作成
root=tk.Tk()
root.title("A/G比")
root.geometry("300x250")
#総蛋白
tk.Label(text="TP").pack(pady=10)
TP_entry=tk.Entry(root,width=4)
TP_entry.pack()
#アルブミン
tk.Label(text="ALB").pack(pady=10)
AL_entry=tk.Entry(root,width=4)
AL_entry.pack()
#実行ボタン
tk.Button(text="計算",command=A_G).pack(pady=10)
#クリアボタン
tk.Button(text="クリア",command=clear).pack(pady=10)
#結果
kekka=tk.Label()
kekka.pack(pady=10)
tk.mainloop()