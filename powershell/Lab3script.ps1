#Lab 3 

#Functions 
function getIP{
(get-netipaddress).ipv4address | Select-String "192*"
}

function getUser{
(get-localuser).Name | Select-String "Admin*"
}

#Variables 
$IP = getIP
$USER = getUser
$PS = $HOST.Version.Major  
$HN = hostname
$DATE = get-date -format "MM/dd/yyyy"

#Output
$BODY = ("This machine's IP is $IP. User is $USER. Hostname is $HN. PowerShell Version is $PS. Today's Date is $DATE")

#Send-to-Email
Send-MailMessage -To "leonardf@ucmail.uc.edu" -From "someone@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)

# Bunci Patel