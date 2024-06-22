# Script para organização de diretórios
Programa escrito em **python** com propósito de organizar diretorios cheios de arquivos de diferentes naturezas, mas específicamente a pasta de Downloads que geralmente está uma confusão.

## ⚒️ Requisitos
Para rodar este script você instalar essas duas ferramentas na sua máquina.

- [Python]("https://www.python.com/Downloads")

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" width="60">

- [Git]("https://git-scm.com/downloads")

<img src="https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png" width="60">

## ⚙️ Rodar localmente
Primeiramente você precisa ter o python instalado na sua máquina. Pode fazé-lo acessando o link [aqui](https://www.python.org/downloads).

Agora abra o seu terminal e clone o repositorio:
```bash
git clone https://github.com/ImaCod3r/Organizador-de-pastas.git
```
Ainda com o terminal aberto navegue até ao diretório do projeto:
```
cd "Organizador de pastas"
```
Em seguida, você precisa instalar as algumas dependências através do comando no:
```bash
pip install -r requirements.txt
```
Agora você pode executar o script com o comando:
```bash
python app.py
```
## 📝 Notas
Você precisará definir os diretórios manualmente no arquivo **app.py**, por ex.:
```python
# Main path
path = "C:\\Users\\LATITUDE7280i7\\Downloads"

# Destination path
destinations = {
   "Musicas": "C:\\Users\\LATITUDE7280i7\\Music",
   "Imagens": "C:\\Users\\LATITUDE7280i7\\OneDrive\\Imagens",
   "Documentos": "C:\\Users\\LATITUDE7280i7\\OneDrive\\Documentos",
   "Videos": "C:\\Users\\LATITUDE7280i7\\Videos"
}
```
Pode agendar a execução automática do script, não sabe como? 
- [Clique aqui](https://youtube.com/watch?v=SxEjHAlCqmo)

## 👷‍♂️ Autor
- Edson Rodrigues - **Imacod3r**
