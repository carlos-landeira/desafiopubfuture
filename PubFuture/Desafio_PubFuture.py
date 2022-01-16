import json
from timeit import repeat
from werkzeug import datastructures
from config import *
from sqlalchemy import String, Integer, Float, Boolean, Column


class Receitas(db.Model):

    #Atributos das receitas
    id_receita = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float(55))
    dataRecebimento = db.Column(db.String(55))
    dataRecebimentoEsperado = db.Column(db.String(55))
    descrição = db.Column(db.String(55))
    conta = db.Column(db.String(55))
    tipoReceita = db.Column(db.String(55))
    


    #Expressão da classe em forma de texto
    def __str__(self):
        return f"{self.id_receita}, {self.valor}, {self.dataRecebimento}, {self.dataRecebimentoEsperado}, {self.descrição}, {self.conta}, {self.tipoReceita}"

    #Expressão da classe no formato json
    def json(self):
        return{
            "id_receita": self.id_receita,
            "valor": self.valor,
            "dataRecebimento": self.dataRecebimento,
            "dataRecebimentoEsperado": self.dataRecebimentoEsperado,
            "descrição": self.descrição,
            "conta": self.conta,
            "tipoReceita": self.tipoReceita
        }


class Despesas(db.Model):
    #Atributos das despesas
    id_despesa = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float(55))
    dataPagamento = db.Column(db.String(55))
    dataPagamentoEsperado = db.Column(db.String(55))
    tipoDespesa = db.Column(db.String(55))
    conta = db.Column(db.String(55))
    


    #Expressão da classe em forma de texto
    def __str__(self):
    
        return f"{self.id_despesa}, {self.valor}, {self.dataPagamento}, {self.dataPagamentoEsperado}, {self.tipoDespesa}, {self.conta}"

    #Expressão da classe no formato json
    def json(self):
        return{
            "id_despesa": self.id_despesa,
            "valor": self.valor,
            "dataPagamento": self.dataPagamento,
            "dataPagamentoEsperado": self.dataPagamentoEsperado,
            "tipoDespesa": self.tipoDespesa,
            "conta": self.conta
        }
        
class Contas(db.Model):
    id_conta = db.Column(db.Integer, primary_key=True)
    saldo = db.Column(db.Float(55))
    tipoConta = db.Column(db.String(55)) 
    instituicaoFinanceira = db.Column(db.String(55))

    
    def __str__(self): 
        #Expressão da classe em forma de texto
        return f"{self.id_conta}, {self.saldo}, {self.tipoConta}, {self.instituicaoFinanceira} " 



    def json(self):
        #Expressão da classe no formato json
        return {
            "id_conta": self.id_conta,
            "saldo": self.saldo,
            "tipoConta": self.tipoConta,
            "instituicaoFinanceira": self.instituicaoFinanceira
        }




#Execução do programa
if __name__ == "__main__":  
     
    #Cria as tabelas
    db.create_all()

    menu=1
    while menu!=0:
        print("Bem-vindo(a) ao sistema de gerenciamento de finanças! Qual menu você gostaria de acessar?")
        print("1 - Receitas")
        print("2 - Despesas")
        print("3 - Contas")
        print("0 - Sair do programa")
        menu = int(input("> "))

        if menu == 1:
            print("Qual das seguintes operações você quer realizar?")
            print("1 - Cadastrar receitas")
            print("2 - Editar receitas")
            print("3 - Remover receitas")
            print("4 - Listar receitas")
            menu2 = int(input("> "))

            if menu2 == 1:
                def cadastrar_receita():
                    
                    v = float(input("Digite o valor: "))
                    datareceb = str(input("Digite a data de recebimento (DD-MM-AAAA): "))
                    dataesperada = str(input("Digite a data de recebimento esperado (DD-MM-AAAA): "))
                    desc = str(input("Digite a descrição da receita: "))
                    acc = str(input("Digite a conta: "))
                    tipo = str(input("Digite qual o tipo de receita: "))
                    print("")
                
                    receita = Receitas(valor=v, dataRecebimento=datareceb, dataRecebimentoEsperado=dataesperada, descrição=desc, conta=acc, tipoReceita=tipo)
                    db.session.add(receita)
                    db.session.commit()
                    print("Receita cadastrada com sucesso!")
                    print(" ")

                cadastrar_receita()
            
            elif menu2 == 2:
                def editar_receita():
                    print("Qual das seguintes receitas você gostaria de editar? (Selecione pelo ID)")
                    receita = db.session.query(Receitas)
                    for receitas in receita:
                        print("ID:",receitas.id_receita, "||Valor: R$",receitas.valor, "||Data de recebimento:",receitas.dataRecebimento, "||Data de recebimento esperado:",receitas.dataRecebimentoEsperado, "||Descrição:",receitas.descrição, "||Conta:",receitas.conta, "||Tipo de receita:",receitas.tipoReceita)
                        print("")
                    x = int(input("> "))
                    atualizar = Receitas.query.filter_by(id_receita=x).first()

                    print("Receita",x,"selecionada, qual informação você gostaria de editar?")
                    print("1 - Valor")
                    print("2 - Data de recebimento")
                    print("3 - Data de recebimento esperado")
                    print("4 - Descrição")
                    print("5 - Conta")
                    print("6 - Tipo de receita")
                    y = int(input("> "))

                    if y == 1:
                        z = float(input("Insira o novo valor da receita: "))
                        atualizar.valor = z
                        db.session.commit()
                        print("Valor atualizado com sucesso!")
                    
                    elif y == 2:
                        z = str(input("Insira a nova data de recebimento da receita: "))
                        atualizar.dataRecebimento = z
                        db.session.commit()
                        print("Data de recebimento atualizada com sucesso!")
                    
                    elif y == 3:
                        z = str(input("Insira a nova data de recebimento esperado da receita: "))
                        atualizar.dataRecebimentoEsperado = z
                        db.session.commit()
                        print("Data de recebimento esperada atualizada com sucesso!")                    

                    elif y == 4:
                        z = str(input("Insira a nova descrição da receita: "))
                        atualizar.descrição = z
                        db.session.commit()
                        print("Descrição atualizada com sucesso!")                    

                    elif y == 5:
                        z = str(input("Insira a nova conta da receita: "))
                        atualizar.conta = z
                        db.session.commit()
                        print("Conta atualizada com sucesso!")

                    elif y == 6:
                        z = str(input("Insira o novo tipo da receita: "))
                        atualizar.tipoReceita = z
                        db.session.commit()
                        print("Tipo da receita atualizado com sucesso!")
                    
                    else:
                        print("Escolha uma operação válida.")

                    
                editar_receita()

            elif menu2 == 3:
                def remover_receita():
                    print("Qual das seguintes receitas você gostaria de remover? (Selecione pelo ID)")
                    receita = db.session.query(Receitas)
                    for receitas in receita:
                        print("ID:",receitas.id_receita, "||Valor R$:",receitas.valor, "||Data de recebimento:",receitas.dataRecebimento, "||Data de recebimento esperado:",receitas.dataRecebimentoEsperado, "||Descrição:",receitas.descrição, "||Conta:",receitas.conta, "||Tipo de receita:",receitas.tipoReceita)
                        print("")
                    x = int(input("> "))
                    remover = Receitas.query.filter_by(id_receita=x).first()
                    db.session.delete(remover)
                    db.session.commit()
                    print("Receita",x,"removida com sucesso!")

                remover_receita()

            elif menu2 == 4:
                def listar_receitas():
                    receita = db.session.query(Receitas)
                    print("Listando todas as receitas:")
                    print("")
                    for receitas in receita:
                            print("ID:",receitas.id_receita, "||Valor: R$",receitas.valor, "||Data de recebimento:",receitas.dataRecebimento, "||Data de recebimento esperado:",receitas.dataRecebimentoEsperado, "||Descrição:",receitas.descrição, "||Conta:",receitas.conta, "||Tipo de receita:",receitas.tipoReceita)
                            print("")
                listar_receitas()

            else:
                print("Selecione uma operação válida.")

        elif menu == 2:
            print("Qual das seguintes operações você quer realizar?")
            print("1 - Cadastrar despesas")
            print("2 - Editar despesas")
            print("3 - Remover despesas")
            print("4 - Listar despesas")
            menu2 = int(input("> "))

            if menu2 == 1:
                def cadastrar_despesa():
                    
                    v = float(input("Digite o valor: "))
                    datapag = str(input("Digite a data de pagamento (DD-MM-AAAA): "))
                    dataesperada = str(input("Digite a data de pagamento esperado (DD-MM-AAAA): "))
                    tipo = str(input("Digite qual o tipo de despesa: "))
                    acc = str(input("Digite a conta: "))
                    print("")
                
                    despesa = Despesas(valor=v, dataPagamento=datapag, dataPagamentoEsperado=dataesperada, tipoDespesa=tipo, conta=acc)
                    db.session.add(despesa)
                    db.session.commit()
                    print("Despesa cadastrada com sucesso!")
                    print(" ")

                cadastrar_despesa()
            
            elif menu2 == 2:
                def editar_despesa():
                    print("Qual das seguintes despesas você gostaria de editar? (Selecione pelo ID)")
                    despesa = db.session.query(Despesas)
                    for despesas in despesa:
                        print("ID:",despesas.id_despesa, "||Valor: R$",despesas.valor, "||Data de recebimento:",despesas.dataPagamento, "||Data de recebimento esperado:",despesas.dataPagamentoEsperado, "||Tipo de despesa:",despesas.tipoDespesa, "||Conta:",despesas.conta)
                        print("")
                    x = int(input("> "))
                    atualizar = Despesas.query.filter_by(id_despesa=x).first()


                    print("Despesa",x,"selecionada, qual informação você gostaria de editar?")
                    print("1 - Valor")
                    print("2 - Data de pagamento")
                    print("3 - Data de pagamento esperado")
                    print("4 - Tipo de receita")
                    print("5 - Conta")
                    y = int(input("> "))

                    if y == 1:
                        z = float(input("Insira o novo valor da despesa: "))
                        atualizar.valor = z
                        db.session.commit()
                        print("Valor atualizado com sucesso!")
                    
                    elif y == 2:
                        z = str(input("Insira a nova data de pagamento da despesa: "))
                        atualizar.dataPagamento = z
                        db.session.commit()
                        print("Data de pagamento atualizada com sucesso!")
                    

                    elif y == 3:
                        z = str(input("Insira a nova data de pagamento esperado da despesa: "))
                        atualizar.dataPagamentoEsperado = z
                        db.session.commit()
                        print("Data de pagamento esperada atualizada com sucesso!")
                    

                    elif y == 4:
                        z = str(input("Insira o novo tipo da despesa: "))
                        atualizar.tipoDespesa = z
                        db.session.commit()
                        print("Tipo da despesa atualizado com sucesso!")
                        
                
                    elif y == 5:
                        z = str(input("Insira a nova conta da despesa: "))
                        atualizar.conta = z
                        db.session.commit()
                        print("Conta atualizada com sucesso!")
                    

                    else:
                        print("Escolha uma operação válida.")

                    
                editar_despesa()

            elif menu2 == 3:
                def remover_despesa():
                    print("Qual das seguintes despesas você gostaria de remover? (Selecione pelo ID)")
                    despesa = db.session.query(Despesas)
                    for despesas in despesa:
                        print("ID:",despesas.id_despesa, "||Valor: R$",despesas.valor, "||Data de pagamento:",despesas.dataPagamento, "||Data de pagamento esperado:",despesas.dataPagamentoEsperado, "||Tipo de despesa:",despesas.tipoDespesa, "||Conta:",despesas.conta)
                        print("")
                    x = int(input("> "))
                    remover = Despesas.query.filter_by(id_despesa=x).first()
                    db.session.delete(remover)
                    db.session.commit()
                    print("Despesa",x,"removida com sucesso!")

                remover_despesa()

            elif menu2 == 4:
                def listar_despesas():
                    despesa = db.session.query(Despesas)
                    print("Listando todas as despesas:")
                    print("")
                    for despesas in despesa:
                            print("ID:",despesas.id_despesa, "||Valor: R$",despesas.valor, "||Data de pagamento:",despesas.dataPagamento, "||Data de pagamento esperado:",despesas.dataPagamentoEsperado, "||Tipo de despesa:",despesas.tipoDespesa, "||Conta:",despesas.conta)
                            print("")
                listar_despesas()

            else:
                print("Selecione uma operação válida.")

        
        elif menu == 3:
            print("Qual das seguintes operações você quer realizar?")
            print("1 - Cadastrar contas")
            print("2 - Editar contas")
            print("3 - Remover contas")
            print("4 - Listar contas")
            print("5 - Transferir saldo entre contas")
            print("6 - Listar saldo total")
            menu2 = int(input("> "))

            if menu2 == 1:
                def cadastrar_conta():
                    
                    sal = float(input("Digite o saldo da conta: "))
                    tipo = str(input("Digite o tipo da conta: "))
                    instituicao = str(input("Digite a instituição financeira da conta: "))
                    print("")
                
                    conta = Contas(saldo=sal, tipoConta=tipo, instituicaoFinanceira=instituicao)
                    db.session.add(conta)
                    db.session.commit()
                    print("Conta cadastrada com sucesso!")
                    print(" ")

                cadastrar_conta()
            
            elif menu2 == 2:
                def editar_conta():
                    print("Qual das seguintes contas você gostaria de editar? (Selecione pelo ID)")
                    conta = db.session.query(Contas)
                    for contas in conta:
                        print("ID:",contas.id_conta, "||Saldo: R$",contas.saldo, "||Tipo da conta:",contas.tipoConta, "||Instituição financeira:",contas.instituicaoFinanceira)
                        print("")
                    x = int(input("> "))
                    atualizar = Contas.query.filter_by(id_conta=x).first()


                    print("Conta",x,"selecionada, qual informação você gostaria de editar?")
                    print("1 - Saldo")
                    print("2 - Tipo da conta")
                    print("3 - Instituição financeira")
                    y = int(input("> "))

                    if y == 1:
                        z = float(input("Insira o novo saldo da conta: "))
                        atualizar.saldo = z
                        db.session.commit()
                        print("Saldo atualizado com sucesso!")
                    
                    elif y == 2:
                        z = str(input("Insira o novo tipo da conta: "))
                        atualizar.tipoConta = z
                        db.session.commit()
                        print("Tipo da conta atualizado com sucesso!")
                    

                    elif y == 3:
                        z = str(input("Insira a nova instituição financeira da conta: "))
                        atualizar.instituicaoFinanceira = z
                        db.session.commit()
                        print("Instituição financeira atualizada com sucesso!")
                    

                    else:
                        print("Escolha uma operação válida.")

                    
                editar_conta()

            elif menu2 == 3:
                def remover_conta():
                    print("Qual das seguintes contas você gostaria de remover? (Selecione pelo ID)")
                    conta = db.session.query(Contas)
                    for contas in conta:
                        print("ID:",contas.id_conta, "||Saldo: R$",contas.saldo, "||Tipo da conta:",contas.tipoConta, "||Instituição financeira:",contas.instituicaoFinanceira)
                        print("")
                    x = int(input("> "))
                    remover = Contas.query.filter_by(id_conta=x).first()
                    db.session.delete(remover)
                    db.session.commit()
                    print("Conta",x,"removida com sucesso!")

                remover_conta()

            elif menu2 == 4:
                def listar_contas():
                    conta = db.session.query(Contas)
                    print("Listando todas as contas:")
                    print("")
                    for contas in conta:
                        print("ID:",contas.id_conta, "||Saldo: R$",contas.saldo, "||Tipo da conta:",contas.tipoConta, "||Instituição financeira:",contas.instituicaoFinanceira)
                        print("")
                listar_contas()

            elif menu2 == 5:
                def transferir_saldo():
                    conta = db.session.query(Contas)
                    for contas in conta:
                        print("ID:",contas.id_conta, "||Saldo: R$",contas.saldo, "||Tipo da conta:",contas.tipoConta, "||Instituição financeira:",contas.instituicaoFinanceira)
                        print("")
                    x = int(input("Digite a conta que vai dar o saldo: "))
                    y = float(input("Digite o valor a ser transferido: "))
                    z = int(input("Digite a conta que vai receber o saldo: "))
                    doa = Contas.query.filter_by(id_conta=x).first()
                    doa.saldo = doa.saldo - y
                    recebe = Contas.query.filter_by(id_conta=z).first()
                    recebe.saldo = recebe.saldo + y
                    db.session.commit()
                    print("Saldo transferido com sucesso!")
                transferir_saldo()

            elif menu2 == 6:
                def listar_saldo():
                    conta = db.session.query(Contas)
                    print("Listando o saldo total:")
                    print("")
                    x = 0
                    for contas in conta:
                        x = x + contas.saldo
                    print("Saldo total:",x)
                    print("")
                listar_saldo()
            
            else:
                print("Selecione uma operação válida.")