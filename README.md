# Assistente Virtual com Reconhecimento de Voz

Este projeto é um **assistente virtual** que utiliza **Processamento de Linguagem Natural (PLN)** para interagir com o usuário por meio de comandos de voz.

## Funcionalidades

- Texto para Fala (TTS): Converte texto em áudio.
- Fala para Texto (STT): Captura áudio e converte para texto.
- Pesquisa Inteligente: Pesquisa no **Google Maps** para encontrar locais próximos.
- Abertura de Sites: Comandos de voz para abrir YouTube, Google, Facebook e mais.

---

## Instalação

### 1. Baixar o projeto

Clone este repositório ou baixe os arquivos manualmente.

```txt
git clone https://github.com/matheusparaujo1515/Sistema-assistente-virtual.git
cd Sistema-assistente-virtual
```

### 2. Criar ambiente virtual (opcional, recomendado)

```txt
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Instalar as dependências

```txt
pip install -r requirements.txt
```

Caso tenha problemas com `SpeechRecognition`, baixe manualmente:

```txt
pip install https://github.com/Uberi/speech_recognition/releases/download/3.8.1/SpeechRecognition-3.14.1-py3-none-any.whl
```

### 4. Instalar PyAudio (caso necessário)

Se o comando `pip install pyaudio` falhar, siga os passos abaixo:

- **Windows**: Baixe e instale a versão correspondente do [PyAudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

### 5. Instalar FLAC (para melhor reconhecimento de voz)

Para Windows, baixe [FLAC](https://xiph.org/flac/download.html) e adicione ao PATH.

---

## Como Usar

Após a instalação, execute o assistente:

```txt
python app.py
```

### Menu de opções:

1. Transformar texto em áudio
2. Transformar áudio em texto
3. Pesquisar por áudio (ex: "abrir Google", "pesquisar farmácia próxima")
999. Finalizar o assistente

---

## Exemplos de Comandos

### Acessar sites:
- Para acessar um site, diga: **"Ir para" + Nome do site**.
- O nome do site deve estar na tabela dos 20 sites suportados.
- **Exemplo:**
  - **"Ir para YouTube"** → Abre `https://www.youtube.com`
  - **"Ir para Facebook"** → Abre `https://www.facebook.com`

### Buscar locais próximos:
- Para encontrar locais próximos, diga o nome do local seguido de **"próximo(a)"**.
- **Exemplo:**
  - **"Farmácia próxima"** → Pesquisa farmácias no Google Maps
  - **"Hospital próximo"** → Pesquisa hospitais no Google Maps
  - **"Mercado próximo"** → Pesquisa mercados no Google Maps
  - **"Restaurante próximo"** → Pesquisa restaurantes no Google Maps
  - **"Shopping próximo"** → Pesquisa shoppings no Google Maps
  - **"Padaria próxima"** → Pesquisa padarias no Google Maps
  - **"Posto próximo"** → Pesquisa postos de combustível no Google Maps

---

## Tabela de Sites Suportados

| Nome do Site        | URL                         |
|---------------------|----------------------------|
| Google             | https://www.google.com     |
| YouTube            | https://www.youtube.com    |
| Facebook          | https://www.facebook.com   |
| Globo              | https://www.globo.com      |
| Mercado Livre      | https://www.mercadolivre.com.br |
| UOL                | https://www.uol.com.br     |
| Instagram          | https://www.instagram.com  |
| Twitter           | https://twitter.com        |
| LinkedIn           | https://www.linkedin.com   |
| WhatsApp           | https://web.whatsapp.com   |
| Maps               | https://www.google.com/maps |
| GitHub             | https://www.github.com     |
| Amazon             | https://www.amazon.com.br  |
| Netflix            | https://www.netflix.com    |
| OLX                | https://www.olx.com.br     |
| Terra              | https://www.terra.com.br   |
| G1                 | https://g1.globo.com       |
| Tik Tok            | https://www.tiktok.com     |
| Folha              | https://www.folha.uol.com.br |

---

## Bibliotecas Utilizadas

- **SpeechRecognition** - [Documentação](https://pypi.org/project/SpeechRecognition/)
- **pyttsx3** - [Documentação](https://pypi.org/project/pyttsx3/)
- **webbrowser** - [Documentação](https://docs.python.org/3/library/webbrowser.html)
- **time** - [Documentação](https://docs.python.org/3/library/time.html)

---

## Licença

Este projeto é distribuído sob a licença MIT. Sinta-se livre para modificar e melhorar.
