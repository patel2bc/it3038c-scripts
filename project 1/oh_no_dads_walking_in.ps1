# A student's worst nightmare is when your dad or mom walks in while your gaming when you're supposed to be doing your homework. 
# With this powerful powershell script, you no longer have to worry! It will instantly minimize all apps and open UC's main websites 
# along with a lecture and the some legit looking apps you may need for your homework. 

# Minimize all apps
$shell = New-Object -ComObject Shell.Application
$shell.MinimizeAll()

# Open websites in default browser and maximize window
Start-Process "https://uc.instructure.com" -WindowStyle Maximized
Start-Process "https://catalyst.uc.edu" -WindowStyle Maximized
Start-Process "https://www.khanacademy.org" -WindowStyle Maximized
Start-Process "https://youtu.be/nePN6hPoLCg?t=179" -WindowStyle Maximized

# Open Calculator, Notepad, and Excel applications and minimize them
Start-Process calc -WindowStyle Minimized
Start-Process notepad -WindowStyle Minimized
Start-Process excel -WindowStyle Minimized

# By Bunci Patel 
# Sources: 
# https://stackoverflow.com/questions/70692306/need-to-minimize-a-particular-window
# https://www.youtube.com/watch?v=nePN6hPoLCg

# Most gaming keyboards have a set of macro keys, I set mine to launch this script when pressed. 