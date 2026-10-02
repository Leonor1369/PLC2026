import re
### 1. Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"
# In: `# Exemplo`
# out: `<h1>Exemplo</h1>`

def cab(str):
    regex= re.match(r"(#|##|###)\s([\w\s]+)", str)
    return f"<h{regex.group(1).count('#')}>{regex.group(2)}</h{regex.group(1).count('#')}>"

cab("# Exemplo")

### 2. Bold: pedaços de texto entre "**":
#In: `Este é um **exemplo** ...`
#Out: `Este é um <b>exemplo</b> ...`


def bold(str):
    regex= re.match(r"\*\*([\w\s]+)\*\*", str)
    return f"<b>{regex.group(1)}</b>"

bold("**exemplo**")

### 3. Itálico: pedaços de texto entre "*":
#In: `Este é um *exemplo* ...`
#Out: `Este é um <i>exemplo</i> ...`

def ita(str):
    regex= re.match(r"\*([\w\s]+)\*", str)
    return f"<i>{regex.group(1)}</i>"

ita("*exemplo*")

### 4. Lista numerada:

#In:
#```
#1. Primeiro item
#2. Segundo item
#3. Terceiro item
#```

#Out:
#```
#<ol>
#<li>Primeiro item</li>
#<li>Segundo item</li>
#<li>Terceiro item</li>
#</ol>
#```

from ntpath import join

def numblist(texto):
    itens = re.findall(r"^\s*\d+\.\s+(.*?)\s*$", texto, re.MULTILINE)
    elementos = "\n".join(f"<li>{item}</li>" for item in itens)
    return f"<ol>\n{elementos}\n</ol>"

text = """1. Primeiro item
2. Segundo item
3. Terceiro item"""
print(numblist(text))

### 5. Link: [texto](endereço URL)
#In: `Como pode ser consultado em [página da UC](http://www.uc.pt)`
#Out: `Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>`

def link(str):
    regex= re.match(r"\[(\s*\w+\s*)\]\((https?://[^\s]+)\)", str)
    if regex:
        return f"<a href='{regex.group(2)}'>{re.sub(r'^\s+|\s+$', '', regex.group(1))}</a>"
    return str

link("[   Google    ](https://www.google.com)")


### 6. Imagem: ![texto alternativo](path para a imagem)
#In: Como se vê na imagem seguinte: `![imagem dum coelho](http://www.coellho.com) ...`
#Out: `Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...`

def image(str):
    regex= re.match(r"!\[(\s*\w+\s*)\]\((https?://[^\s]+)\)", str)
    if regex:
        return f"<img src='{regex.group(2)}' alt='{re.sub(r'^\s+|\s+$', '', regex.group(1))}'>"
    return str


image("![imagem dum coelho](http://www.coellho.com) ...")
