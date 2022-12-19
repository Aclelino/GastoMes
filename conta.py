import time
import sqlite3


conn = sqlite3.connect("conta.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS contas(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,nome TEXT NOT NULL, valor INTEGER NOT NULL, data TEXT NOT NULL)")

def inserir(x,y):
    c.execute("INSERT INTO contas(nome,valor,data)VALUES(?,?,?)",(x,y,time.strftime("%B")))
    conn.commit()
    print("Salvo com sucesso!")
def consulta():
    f = c.execute("SELECT * FROM contas")
    for i in f:
        print(f"🆔️: {i[0]}\nCONTA: {i[1]}\nVALOR: {i[2]}\nDATA: {i[3]}")
        

def main():

    menu = input(" \n\n\n\n        CONTAS A PAGAR 💳 \n          ____________\n\n 1.➕ Adicionar  \n 2.⏳ Histórico \n 3.📉 Total \n 4.❌ Excluir \n 5.🔄 Atualizar \n\nOpção: ")

    if menu =="1":
        x = str(input("➕ Adicionar: "))
        y = float(input("#️⃣ Valor: "))
        inserir(x,y)
        main()
    elif menu =="2":
        consulta()
        print()
        main()
        
    elif menu == "3":
        total()
        print()
        main()
    elif menu =="4":
        consulta()
        x = input("Digite o ID a ser Excluido: ")
        delet(x)
    elif menu =="5":
        consulta()
        y = input("🆔️ Digite o ID a ser Atualizado: ")
        x = input("#️⃣ Valor: ")
        update(x,y)
        
def update(x,y):
    consulta()
    c.execute("UPDATE contas SET valor = {} WHERE id = {} ".format(x,y))
    conn.commit()
    print("Salvo")
    
def delet(x):
    
    c.execute("DELETE FROM contas WHERE id = {}".format(x))
    conn.commit()
    print("❌ Excluído com Sucesso !")
    
    
def total():
    a = []
    f = c.execute("SELECT * FROM contas")
    for i in f:
        b =  (i[2])
        a.append(b)
        
    print("\nTotal a pagar R${:.2f}".format(sum(a)))
       
main()
        
