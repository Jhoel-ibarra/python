import random


def choose_options():
  user_option = input("piedra papel o tijera ")
  user_option = user_option.lower()
  
  if not user_option in options:
    print("esa option no es valida")
    #continue
    return None, None
    
  computer_optin = random.choice(options)
  
  print( "User option => ",user_option )
  print( "User option => ", computer_optin)
  return user_option, computer_optin 

def check_rules(user_option, computer_optin):
  win = 0
  if user_option == computer_optin:
      print("empate")
    
  elif user_option == "piedra":
    if computer_optin == "tijera":
      print("piedra gana tijera")
      print("gana el usuario")
      win = 1
    else:
      print("papel gana a piedra")
      print("el ganador es computer") 
      win = 2
      
  elif user_option == "papel":
    if computer_optin == "piedra":
      print("papel gana piedra")
      print("gana el usuario")
      win = 1
    else:
      print("tijera gana a papel")
      print("el ganador es computer") 
      win = 2
      
  elif user_option == "tijera":
    if computer_optin == "papel":
      print("tijera gana a papel")
      print("gana el usuario")
      win = 1
    else:
      print("piedra gana a tijera")
      print("el ganador es computer") 
      win = 2
      
  return win


  
options = ('piedra', 'tijera','papel')
rounds =1
win = 0
compu =0  
while True:
  print("*" *10)
  print("ROUND ", rounds)
  print("*" *10)
  
  user_option,computer_option=choose_options()
  ganador = check_rules(user_option, computer_option)
  if ganador == 1 or ganador == 2:
    if ganador == 1:
      win +=1
    else:
     compu +=1
    
  
  if win == 2 or compu == 2  :
    print("*" *10)
    if win > compu:
      print("El gandor es el usuario")
      break
    else:
      print("El gandor es la computadora")
      break
 
  rounds += 1