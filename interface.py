import random

from senha import API_KEY
import tkinter as tk
import requests
import json
import threading
import random

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"


def JanelaPrincipal():
    global janela
    janela = tk.Tk()
    janela.title("Escolhe por mim!")
    # janela.geometry(f"{800}x{600}")

    # Criação dos widgets
    titulo = tk.Label(janela, text="Qual é a sua dúvida?", height=3)
    btn_filme = tk.Button(janela, text="Filmes e Séries", width=30, height=15, command=AbrirFilme_Serie)
    btn_comida = tk.Button(janela, text="Comidas", width=30, height=15, command=AbrirComidas)
    btn_viagem = tk.Button(janela, text="Viagens", width=30, height=15, command=AbrirViagens)
    btn_invest = tk.Button(janela, text="Investimentos", width=30, height=15, command=AbrirInvestimento)

    # Organização dos widgets na janela
    titulo.pack()
    btn_filme.pack(side="left")
    btn_comida.pack(side="left")
    btn_viagem.pack(side="left")
    btn_invest.pack(side="left")

    # Iniciar a interface gráfica
    janela.mainloop()


def Batepapo():
    global janela2
    global entrada2
    global resultado_text
    janela2 = tk.Toplevel()
    janela2.title("Escolha por mim!")

    titulo2 = tk.Label(janela2, text="Tire a sua dúvida", height=1)
    entrada2 = tk.Entry(janela2, width=50)
    btn_enviar = tk.Button(janela2, text="Enviar", width=42, height=5, command=lambda: RealizarBusca(entrada2, resultado_text))
    resultado_text = tk.Text(janela2, wrap=tk.WORD, height=10, width=50)  # Text para exibir resposta com quebras de linha
    resultado_text.config(state=tk.DISABLED)  # Inicialmente, desabilita a edição do Text

    titulo2.grid(row=0, column=1)
    entrada2.grid(row=1, column=1)
    btn_enviar.grid(row=2, column=1)
    resultado_text.grid(row=3, column=1)


def AbrirInvestimento():
    global janela_invest
    janela_invest = tk.Toplevel()
    janela_invest.title("Escolha por mim!")

    titulo_invest = tk.Label(janela_invest, text="Escolha o tipo de Investimento")
    btn_poupanca = tk.Button(janela_invest, text="Poupança", command=PerfilInvestidor)
    btn_cripto = tk.Button(janela_invest, text="Criptomoedas", command=PerfilInvestidor)
    btn_tesouro = tk.Button(janela_invest, text="Tesouro", command=PerfilInvestidor)
    btn_acoes = tk.Button(janela_invest, text="Ações", command=PerfilInvestidor)
    btn_random_invest = tk.Button(janela_invest, text="Escolha por mim", width=45)

    titulo_invest.grid(row=0, column=1)
    btn_poupanca.grid(row=1, column=0)
    btn_cripto.grid(row=1, column=2)
    btn_tesouro.grid(row=2, column=0)
    btn_acoes.grid(row=2, column=2)
    btn_random_invest.grid(row=3, column=0, columnspan=3)


def AbrirViagens():
    global janela_viagens
    janela_viagens = tk.Toplevel()
    janela_viagens.title("Escolha por mim!")

    titulo_viagens = tk.Label(janela_viagens, text="Pretende viajar pra onde?")
    btn_brasil = tk.Button(janela_viagens, text="Brasil", command=ExecutarViagemBrasil)
    btn_internacional = tk.Button(janela_viagens, text="Viagem Internacional", command=ExecutarViagemInternacional)
    btn_random_viagens = tk.Button(janela_viagens, text="Escolha por mim", width=45, command=SorteioViagem)

    titulo_viagens.grid(row=0, column=1)
    btn_brasil.grid(row=1, column=0)
    btn_internacional.grid(row=1, column=2)
    btn_random_viagens.grid(row=2,column=0, columnspan=3)


def AbrirComidas():
    global janela_comidas
    janela_comidas = tk.Toplevel()
    janela_comidas.title("Escolha por mim!")

    titulo_comida = tk.Label(janela_comidas, text="Escolha a Nacionalidade")
    btn_italiana = tk.Button(janela_comidas, text="Italiana", command=ExecutarComidaItaliana)
    btn_brasileira = tk.Button(janela_comidas, text="Brasileira", command=ExecutarComidaBrasileira)
    btn_mexicana = tk.Button(janela_comidas, text="Mexicana", command=ExecutarComidaMexicana)
    btn_chinesa = tk.Button(janela_comidas, text="Chinesa", command=ExecutarComidaChinesa)
    btn_francesa = tk.Button(janela_comidas, text="Francesa", command=ExecutarComidaFrancesa)
    btn_japonesa = tk.Button(janela_comidas, text="Japonesa", command=ExecutarComidaJaponesa)
    btn_random_comida = tk.Button(janela_comidas, text="Escolha por mim", width=45, command=ExecutarComidaRandom)

    titulo_comida.grid(row=0, column=1)
    btn_italiana.grid(row=1, column=0)
    btn_brasileira.grid(row=1, column=2)
    btn_mexicana.grid(row=2, column=0)
    btn_chinesa.grid(row=2, column=2)
    btn_francesa.grid(row=3, column=0)
    btn_japonesa.grid(row=3, column=2)
    btn_random_comida.grid(row=4, column=0, columnspan=3)


def AbrirFilme_Serie():
    global janela_filme_serie
    janela_filme_serie = tk.Toplevel()
    janela_filme_serie.title("Escolha por mim!")

    titulo_filme_serie = tk.Label(janela_filme_serie, text="Você quer assistir filme ou série?")
    btn_escolha_filme = tk.Button(janela_filme_serie, text="Filmes", command=GenerosFilme)
    btn_escolha_serie = tk.Button(janela_filme_serie, text="Séries", command=GeneroSerie)
    btn_random_fil_ser = tk.Button(janela_filme_serie, text="Escolha por mim", width=45, command=SorteioFilmeSerie)

    titulo_filme_serie.grid(row=0, column=1)
    btn_escolha_filme.grid(row=1, column=0)
    btn_escolha_serie.grid(row=1, column=2)
    btn_random_fil_ser.grid(row=2, column=0, columnspan=3)


def PerfilInvestidor():
    global janela_perfil_invest
    janela_perfil_invest = tk.Toplevel()
    janela_perfil_invest.title("Escolha por mim!")

    titulo_perfil_invest = tk.Label(janela_perfil_invest, text="Escolha o Risco do Investimento")
    btn_conservador = tk.Button(janela_perfil_invest, text="Conservador")
    btn_moderado = tk.Button(janela_perfil_invest, text="Moderado")
    btn_agressivo = tk.Button(janela_perfil_invest, text="Agressivo")
    btn_longo_prazo = tk.Button(janela_perfil_invest, text="Longo Prazo")
    btn_random_perfil_invest = tk.Button(janela_perfil_invest, text="Escolha por mim", width=45)

    titulo_perfil_invest.grid(row=0, column=1)
    btn_conservador.grid(row=1, column=0)
    btn_moderado.grid(row=1, column=2)
    btn_agressivo.grid(row=2, column=0)
    btn_longo_prazo.grid(row=2, column=2)
    btn_random_perfil_invest.grid(row=3, column=0, columnspan=3)

    janela_invest.destroy()


def GeneroSerie():
    global janela_serie_genero
    janela_serie_genero = tk.Toplevel()
    janela_serie_genero.title("Escolha por mim!")

    titulo_serie_genero = tk.Label(janela_serie_genero, text="Escolha o Gênero da Série")
    btn_esporte = tk.Button(janela_serie_genero, text="Esporte", command=ExecutarSerieEsporte)
    btn_teen = tk.Button(janela_serie_genero, text="Teen", command=ExecutarSerieTeen)
    btn_drama = tk.Button(janela_serie_genero, text="Drama", command=ExecutarSerieDrama)
    btn_acao = tk.Button(janela_serie_genero, text="Ação", command=ExecutarSerieAcao)
    btn_comedia = tk.Button(janela_serie_genero, text="Comédia", command=ExecutarSerieComedia)
    btn_romance = tk.Button(janela_serie_genero, text="Romance", command=ExecutarSerieRomance)
    btn_random_serie_genero = tk.Button(janela_serie_genero, text="Escolha por mim", width=45, command=ExecutarSerieRandom)

    titulo_serie_genero.grid(row=0, column=1)
    btn_esporte.grid(row=1, column=0)
    btn_teen.grid(row=1, column=2)
    btn_drama.grid(row=2, column=0)
    btn_acao.grid(row=2, column=2)
    btn_comedia. grid(row=3, column=0)
    btn_romance.grid(row=3, column=2)
    btn_random_serie_genero.grid(row=4, column=0, columnspan=3)

    janela_filme_serie.destroy()


def GenerosFilme():
    global janela_filme_genero
    janela_filme_genero = tk.Toplevel()
    janela_filme_genero.title("Escolha por mim!")

    titulo_filme_genero = tk.Label(janela_filme_genero, text="Escolha o Gênero do Filme")
    btn_comedia = tk.Button(janela_filme_genero, text="Comédia", command=ExecutarFilmeComedia)
    btn_heroi = tk.Button(janela_filme_genero, text="heroi", command=ExecutarFilmeHeroi)
    btn_acao = tk.Button(janela_filme_genero, text="Ação", command=ExecutarFilmeAcao)
    btn_romance = tk.Button(janela_filme_genero, text="Romance", command=ExecutarFilmeRomance)
    btn_terror = tk.Button(janela_filme_genero, text="Terror", command=ExecutarFilmeTerror)
    btn_aventura = tk.Button(janela_filme_genero, text="Aventura", command=ExecutarFilmeAventura)
    btn_random_filme_genero = tk.Button(janela_filme_genero, text="Escolha por mim", width=45, command=ExecutarFilmeRandom)

    titulo_filme_genero.grid(row=0, column=1)
    btn_comedia.grid(row=1, column=0)
    btn_heroi.grid (row=1, column=2)
    btn_acao.grid(row=2, column=0)
    btn_romance.grid(row=2, column=2)
    btn_terror.grid(row=3, column =0)
    btn_aventura.grid(row=3, column=2)
    btn_random_filme_genero.grid(row=4, column=0, columnspan=3)

    janela_filme_serie.destroy()


def SorteioFilmeSerie():
    filme = 1
    serie = 2
    numero_sorteado = random.randint(filme, serie)
    if numero_sorteado == 1:
        GenerosFilme()
    elif numero_sorteado == 2:
        GeneroSerie()


def Obter_Resposta_ChatGpt(pergunta):       # faz o processamento para levar a mensagem até a API
    body_mensagem = {
        "model": id_modelo,
        "messages": [{"role": "user", "content": pergunta}]    # a variavel "pergunta" pode ser substituida por uma mensagem pré-definida
    }

    try:
        response = requests.post(link, headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, data=json.dumps(body_mensagem))
        response.raise_for_status()  # Lança uma exceção se a resposta não for bem-sucedida
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Erro na solicitação: {e}"


def RealizarBusca(entrada2, resultado_text):        # envia a mensagem desejada até o processamento para obter a resposta da API
    pergunta = entrada2.get()
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_resposta():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_resposta)
    t.start()


def RealizarBuscaFilmeComedia(entrada2, resultado_text):
    pergunta = "Eu quero apenas um filme de comedia, me recomende o filme e suas detalhações"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaFilmeComedia():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaFilmeComedia)
    t.start()


def ExecutarFilmeComedia():
    Batepapo()
    RealizarBuscaFilmeComedia(entrada2, resultado_text)




def RealizarBuscaFilmeHeroi(entrada2, resultado_text):
    pergunta = "Eu quero apenas um filme de super-Herói, me recomende o filme e suas detalhações"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaFilmeHeroi():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaFilmeHeroi)
    t.start()


def ExecutarFilmeHeroi():
    Batepapo()
    RealizarBuscaFilmeHeroi(entrada2, resultado_text)


def RealizarBuscaFilmeAcao(entrada2, resultado_text):
    pergunta = "Eu quero apenas um filme de ação, me recomende o filme e suas detalhações"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaFilmeAcao():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaFilmeAcao)
    t.start()


def ExecutarFilmeAcao():
    Batepapo()
    RealizarBuscaFilmeAcao(entrada2, resultado_text)


def RealizarBuscaFilmeRomance(entrada2, resultado_text):
    pergunta = "Eu quero apenas um filme de romance, me recomende o filme e suas detalhações"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaFilmeRomance():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaFilmeRomance)
    t.start()


def ExecutarFilmeRomance():
    Batepapo()
    RealizarBuscaFilmeRomance(entrada2, resultado_text)


def RealizarBuscaFilmeTerror(entrada2, resultado_text):
    pergunta = "Eu quero apenas um filme de terror, me recomende o filme e suas detalhações"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaFilmeTerror():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaFilmeTerror)
    t.start()


def ExecutarFilmeTerror():
    Batepapo()
    RealizarBuscaFilmeTerror(entrada2, resultado_text)


def RealizarBuscaFilmeAventura(entrada2, resultado_text):
    pergunta = "Eu quero apenas um filme de aventura, me recomende o filme e suas detalhações"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaFilmeAventura():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaFilmeAventura)
    t.start()


def ExecutarFilmeAventura():
    Batepapo()
    RealizarBuscaFilmeAventura(entrada2, resultado_text)


def RealizarBuscaFilmeRandom(entrada2, resultado_text):
    pergunta = "Estou em dúvida de qual filme escolher, selecione apenas um genero de filme entre comédia, super=herói, ação, romance, terror, aventura, me recomende o filme e suas detalhações"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaFilmeRandom():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaFilmeRandom)
    t.start()


def ExecutarFilmeRandom():
    Batepapo()
    RealizarBuscaFilmeRandom(entrada2, resultado_text)


def RealizarBuscaSerieEsporte(entrada2, resultado_text):
    pergunta = "Eu quero apenas uma série de esporte, me recomende a série e suas detalhações"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaSerieEsporte():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaSerieEsporte)
    t.start()


def ExecutarSerieEsporte():
    Batepapo()
    RealizarBuscaSerieEsporte(entrada2, resultado_text)


def RealizarBuscaSerieTeen(entrada2, resultado_text):
    pergunta = "Eu quero apenas uma série de teen, me recomende a série e suas detalhações"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaSerieTeen():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaSerieTeen)
    t.start()


def ExecutarSerieTeen():
    Batepapo()
    RealizarBuscaSerieTeen(entrada2, resultado_text)


def RealizarBuscaSerieDrama(entrada2, resultado_text):
    pergunta = "Eu quero apenas uma série de drama, me recomende a série e suas detalhações"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaSerieDrama():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaSerieDrama)
    t.start()


def ExecutarSerieDrama():
    Batepapo()
    RealizarBuscaSerieDrama(entrada2, resultado_text)


def RealizarBuscaSerieAcao(entrada2, resultado_text):
    pergunta = "Eu quero apenas uma série de ação, me recomende a série e suas detalhações"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaSerieAcao():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaSerieAcao)
    t.start()


def ExecutarSerieAcao():
    Batepapo()
    RealizarBuscaSerieAcao(entrada2, resultado_text)


def RealizarBuscaSerieComedia(entrada2, resultado_text):
    pergunta = "Eu quero apenas uma série de comédia, me recomende a série e suas detalhações"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaSerieComedia():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaSerieComedia)
    t.start()


def ExecutarSerieComedia():
    Batepapo()
    RealizarBuscaSerieComedia(entrada2, resultado_text)


def RealizarBuscaSerieRomance(entrada2, resultado_text):
    pergunta = "Eu quero apenas uma série de esporte, me recomende a série e suas detalhações"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaSerieRomance():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaSerieRomance)
    t.start()


def ExecutarSerieRomance():
    Batepapo()
    RealizarBuscaSerieRomance(entrada2, resultado_text)


def RealizarBuscaSerieRandom(entrada2, resultado_text):
    pergunta = "Estou em dúvida de qual série escolher, selecione apenas um genero de série entre esporte, teen, drama, ação, comédia, romance, me recomende a série e suas detalhações"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaSerieRandom():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaSerieRandom)
    t.start()


def ExecutarSerieRandom():
    Batepapo()
    RealizarBuscaSerieRandom(entrada2, resultado_text)


def RealizarBuscaComidaItaliana(entrada2, resultado_text):
    pergunta = "Me recomende comidas da cultura italiana e restaurantes italianos aqui no Brasil com detalhes"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaComidaItaliana():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaComidaItaliana)
    t.start()


def ExecutarComidaItaliana():
    Batepapo()
    RealizarBuscaComidaItaliana(entrada2, resultado_text)


def RealizarBuscaComidaBrasileira(entrada2, resultado_text):
    pergunta = "Me recomende comidas da cultura brasileira e restaurantes com detalhes"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaComidaBrasileira():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaComidaBrasileira)
    t.start()


def ExecutarComidaBrasileira():
    Batepapo()
    RealizarBuscaComidaBrasileira(entrada2, resultado_text)


def RealizarBuscaComidaMexicana(entrada2, resultado_text):
    pergunta = "Me recomende comidas da cultura mexicana e restaurantes mexicanos aqui no Brasil com detalhes"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaComidaMexicana():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaComidaMexicana)
    t.start()


def ExecutarComidaMexicana():
    Batepapo()
    RealizarBuscaComidaMexicana(entrada2, resultado_text)


def RealizarBuscaComidaChinesa(entrada2, resultado_text):
    pergunta = "Me recomende comidas da cultura chinesa e restaurantes chineses aqui no Brasil com detalhes"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaComidaChinesa():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaComidaChinesa)
    t.start()


def ExecutarComidaChinesa():
    Batepapo()
    RealizarBuscaComidaChinesa(entrada2, resultado_text)


def RealizarBuscaComidaFrancesa(entrada2, resultado_text):
    pergunta = "Me recomende comidas da cultura francesa e restaurantes franceses aqui no Brasil com detalhes"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaComidaFrancesa():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaComidaFrancesa)
    t.start()


def ExecutarComidaFrancesa():
    Batepapo()
    RealizarBuscaComidaFrancesa(entrada2, resultado_text)


def RealizarBuscaComidaJaponesa(entrada2, resultado_text):
    pergunta = "Me recomende comidas da cultura japonesa e restaurantes japoneses aqui no Brasil com detalhes"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaComidaJaponesa():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaComidaJaponesa)
    t.start()


def ExecutarComidaJaponesa():
    Batepapo()
    RealizarBuscaComidaJaponesa(entrada2, resultado_text)


def RealizarBuscaComidaRandom(entrada2, resultado_text):
    pergunta = "Estou em dúvida de qual nacionalidade eu vou pedir comida, selecione apenas uma nacionalidade entre italiana, brasileira, mexicana, chinesa, francesa, japonesa, me recomende uma comida do pais selecionado e um restaurante do pais aqui no Brasil com suas detalhações"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaComidaRandom():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaComidaRandom)
    t.start()


def ExecutarComidaRandom():
    Batepapo()
    RealizarBuscaComidaRandom(entrada2, resultado_text)


def RealizarBuscaViagemBrasil(entrada2, resultado_text):
    pergunta = "Me recomende lugares turisticos para viajar no Brasil, com detalhes"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaViagemBrasil():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaViagemBrasil)
    t.start()


def ExecutarViagemBrasil():
    Batepapo()
    RealizarBuscaViagemBrasil(entrada2, resultado_text)


def RealizarBuscaViagemInternacional(entrada2, resultado_text):
    pergunta = "Me recomende lugares turisticos para viajar fora do Brasil, com detalhes"
    entrada2.delete(0, tk.END)  # Limpa o campo de entrada
    resultado_text.config(state=tk.NORMAL) # Habilita a edição do Text
    resultado_text.delete(1.0, tk.END) # Limpa o conteúdo atual
    resultado_text.insert(tk.END, "Aguarde...")  # Adicione um feedback visual

    def buscar_e_exibir_respostaViagemInternacional():
        resposta = Obter_Resposta_ChatGpt(pergunta)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, resposta) # Insere a resposta no Text

    # thread para fazer a solicitação para não bloquear a interface do usuário
    t = threading.Thread(target=buscar_e_exibir_respostaViagemInternacional)
    t.start()


def ExecutarViagemInternacional():
    Batepapo()
    RealizarBuscaViagemInternacional(entrada2, resultado_text)


def SorteioViagem():
    Brasil = 1
    Internacional = 2
    sortear_numero = random.randint(Brasil, Internacional)
    if sortear_numero == 1:
        ExecutarViagemBrasil()
    elif sortear_numero ==2:
        ExecutarViagemInternacional()


# O programa irá iniciar com a função de abrir a janela principal
JanelaPrincipal()

