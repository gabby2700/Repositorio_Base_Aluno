import pyautogui as at

    
at.hotkey("win","r") # Essa funçao aperta duas teclas ao mesmo tempo.
at.write("chrome",0.2) #Essa funçao escreve .
at.press("enter") # Essa funçao pressiona a tecla .
at.write("https ://www.github.com", 0.1)
at.press("enter")
at.sleep (5)
email = at.prompt("Digite seu e-mail ") 
at.write(email, 0.1)
at.press("tab")
senha = at.prompt("digite sua senha ")
at.write( senha, 0.1)
at.press("enter")