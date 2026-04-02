login_correto = "Marcos555"
senha_correta = "35761"
usuario_digitado = input("Digite seu login: ")
senha_digitada = input("Digite sua senha: ")
if usuario_digitado == login_correto and senha_digitada == senha_correta:
   print("Bem Vindo!")
   estoque_total = 40
   estoque_azul = 20
   estoque_preta = 10
   estoque_branca = 10    
   resposta_azul = input(f"Temos {estoque_azul} azuis. Quantas desejas?")
   quantidade_azul = int(resposta_azul)
   if quantidade_azul > estoque_azul:
       print("Erro! Estoque de azuis insuficiente.")
   else:
       estoque_azul = estoque_azul - quantidade_azul
       print(f"Retirada OK. Restam {estoque_azul} azuis.")        
   resposta_preta = input(f"Temos {estoque_preta} pretas. Quantas desejas?")
   quantidade_preta = int(resposta_preta)
   if quantidade_preta > estoque_preta:
       print("Erro! Estoque de pretas insuficiente.")
   else:
       estoque_preta =estoque_preta - quantidade_preta
       print(f"Retirada OK. Restam {estoque_preta} pretas.")
else:
    print("Acesso Negado")       
    
input("\nFim. Aperte Enter para fechar.")

    
