import os as bot
import shutil as explorer
from colorama import Fore
import time

# Main path
path = "C:\\Users\\LATITUDE7280i7\\Downloads"

# Destination path
destinations = {
   "Musicas": "C:\\Users\\LATITUDE7280i7\\Music",
   "Imagens": "C:\\Users\\LATITUDE7280i7\\OneDrive\\Imagens",
   "Documentos": "C:\\Users\\LATITUDE7280i7\\OneDrive\\Documentos",
   "Videos": "C:\\Users\\LATITUDE7280i7\\Videos"
}

def main(path=path, destinations=destinations):
   # List directory
   arquivos = bot.listdir(path=path)
   # Verify all file extensions
   for arquivo in arquivos:
      name, extension = bot.path.splitext(arquivo)
      # For images
      if extension in [".jpg", ".png", ".jpeg", ".gif"]:
         destination = destinations["Imagens"]
         moveFile(arquivo, destination)
         
      # For Audio
      elif extension in [".mp3", ".m4a", ".ogg", ".wav"]:
         destination = destinations["Musicas"]
         moveFile(arquivo, destination)
         
      # For Docs
      elif extension in [".pdf", ".docx", ".xlsx", ".txt", ".pptx", ".zip", ".rar", ".7z"]:
         destination = destinations["Documentos"]
         moveFile(arquivo, destination)   
         
      # For Videos
      elif extension in [".mp4", ".m4v", ".mov", ".avi"]:
         destination = destinations["Videos"]
         moveFile(arquivo, destination)
 
      # For another extensions
      else:
         print(f"{Fore.YELLOW} Arquivo com extensao desconhecida!")

# A function that moves files
def moveFile(arquivo, destination):
   try:
      explorer.move(path + "\\" + arquivo, destination)
   except Exception as e:
      print(f"{Fore.RED} Erro: {e}")
   else:
      print(f"\n{Fore.GREEN} {arquivo} movido de {path} para {destination} com sucesso")
 
# Execute script
try:
   now = time.time()
   main()
except:
   print(f"{Fore.BLUE} Nao foi possivel iniciar o script")
else:
   pasted = time.time() - now
   print(f"{Fore.BLUE}\n Script finalizado em {pasted:.3f}s {Fore.RESET}")
   time.sleep(10)
   
# Code by Imacod3r, My english is so weird lol ;-;