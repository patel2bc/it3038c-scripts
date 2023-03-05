# A students worst nightmare is when your dad or mom walks in while your gaming when youre supposed to be doing your homework. 
# With this powerful powershell script, you no longer have to worry. It will instantly minimize all apps and open UCs main websites 
# along with a lecture and the some legit looking apps you may need for your homework. 

# Instructions, simply double click on the ps script or right click and "Run in Powershell" (you may have to run it via PS ISE or set Execution policy, see end of script)
# Pro tip Most gaming keyboards have a set of macro keys, I set mine to launch this script when pressed. 

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

# This script shouldve open your default broswer, then open the following sites, launched notepad, excel, and notepad apps. 
# If you get an error that says that you're not allowed to run scripts on this ccomptuer, type "Set-ExecutionPolicy RemoteSigned" or "Set-ExecutionPolicy Unrestricted" in Admin Powershell window and hit Enter 
# After running the script, be sure to type "Set-ExecutionPolicy Undefined" to reset the execution policy 

# By Bunci Patel 
# Sources: 
# https://stackoverflow.com/questions/70692306/need-to-minimize-a-particular-window
# https://www.youtube.com/watch?v=nePN6hPoLCg
