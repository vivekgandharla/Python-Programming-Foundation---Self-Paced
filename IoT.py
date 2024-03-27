Python Program (Using For Loop):
i=1
print ("enter the name")
name=input()
print ("enter the no of time" )
num=int(input())
for i in range(1,num+1):
print (i , name)
i=i+1

print ("enter the name")
name=input()
print ("enter the no of time" )
num=int(input() )
print (type(num))
i=1
while(i<=num):
print (name)
i=i+1


b) Word and character count of a given string
solution:
def char_frequency(str1):
dict = {}
for n in str1:
keys = dict.keys()
if n in keys:
dict[n] += 1
else:
dict[n] = 1
return dict
str=input('enter a string\n')
value=char_frequency(str)
print(value)


c) Area of a given shape (rectangle, triangle and circle) reading
shape and appropriate values
Solution:
a = 3
b = 6
c = 8
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)


d) Handle Divided by Zero Exception.
Solution:
print ("enter two no n1 and n2")
n1=int(input())
n2=int(input())
try:
div=n1/n2
print (div)
except ZeroDivisionError:
print ("zero division is handled")
print ("out of try catch block ")



e) Print current time for 10 times with an interval of 10 seconds.
Solution:
import datetime
import time
for i in range(0,10):
print(datetime.datetime.now().time())
time.sleep(10)


f) Read a file line by line and print the word count of each line.
Solution:
file=open("abc.txt","r")
line=1
for i in file:
print ("print the line no=" , line , "and line is =" , i)
z=i.split()
print ("no of word in line =" , line ,"is = " , len(z))
line = line+1



2nd prog:
Solution:
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
button=18 #physical pin 12
led=17 #physical pin 11
Mini Project with IOT Lab(22MCAL37) 13
GPIO.setup(led,GPIO.OUT)
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
if GPIO.input(button)==False:
GPIO.output(led,True)
print('LED ON')
time.sleep(1)
else:
GPIO.output(led,False)
print('LED OFF')
time.sleep(1)



3.Solution:
import RPi.GPIO as GPIO
import datetime
import time
Mini Project with IOT Lab(22MCAL37) 15
pin=11 #GPIO 17 as BCM
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)
while True:
time_str=datetime.datetime.now().strftime("%H:%M")
print(time_str)
fo=open("on.txt","r")
on= fo.read()
fc=open("off.txt","r")
off= fc.read()
fo.close()
fc.close()
if on==time_str:
GPIO.output(pin,True)
print("same time")
print("LED ON")
elif off==time_str:
time.sleep(1)
GPIO.output(pin,False)
print("LED off")


4.
Solution:
#Switch on relay at a given time using cron
import RPi.GPIO as GPIO # Import Library to access GPIO PIN
import time # To access delay function
import datetime
GPIO.setmode(GPIO.BOARD) # Consider complete raspberry-pi board
GPIO.setwarnings(False) # To avoid same PIN use warning
Relay_PIN = 11 # Define PIN for Relay
GPIO.setup(Relay_PIN,GPIO.OUT) # Set pin function as output
while True:
time1_str=datetime.datetime.now().strftime("%H:%M")
print(time1_str)
if time1_str=="11:09":
print("Bulb on")
GPIO.output(Relay_PIN,GPIO.LOW) #Relay ON
# time.sleep(15) # Give 1 second delay
else:
print("Bulb off")
GPIO.output(Relay_PIN,GPIO.HIGH) # Relay OFF
#time.sleep(1) # Give 1 second delay
gpio.cleanall()

5.
Solution:
from picamera import PiCamera
import time
camera=PiCamera()
camera.start_preview()
time.sleep(10)
camera.capture('/home/pi/Desktop/program5/image.jpg')
print('image detected')
camera.stop_preview()

6.
#app.py
from flask import Flask,render_template
import RPi.GPIO as GPIO
import time
LED_PIN=11 #GPIO 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
app=Flask( name )
@app.route('/')
def index():
return render_template('/index.html')
@app.route('/ledon')
def on():
GPIO.output(LED_PIN,GPIO.HIGH)
Mini Project with IOT Lab(22MCAL37) 24
return "LED ON"
@app.route('/ledoff')
def off():
GPIO.output(LED_PIN,GPIO.LOW)
return "LED OFF"
if name ==' main ':
app.run(debug='true',host='0.0.0.0')#ip address of raspberry pi
• In the directory called templates . create a file called index.html :
index.html
<html>
<body>
<title>Raspberry pi Demo</title>
<h1>Raspberry pi Demo</h1>
<form action="/ledon">
<input type="submit" value="LED ON" >
</form>
<form action="/ledoff">
<input type="submit" value="LED OFF" >
</form>
</body>
</html>
• Run app.py in python editor, where it will redirect to server IP
address. Which opens in the browser.

7.Solution:
import RPi.GPIO as gpio
import time
from picamera import PiCamera
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
fromaddr = "iotmcarnsit@gmail.com"#change the email address
accordinglytoaddr = "iotmcarnsit@gmail.com"
mail = MIMEMultipart()
mail['From'] = fromaddr
mail['To'] = toaddr
mail['Subject'] = "Attachment"
body = "Please find the attachment"
pir=7 #GPIO 4
HIGH=1
LOW=0
Mini Project with IOT Lab(22MCAL37) 29
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD). # initialize GPIO Pin as outputs
gpio.setup(pir, gpio.IN) # initialize GPIO Pin as input
data="object detected"
def sendMail(data):
mail.attach(MIMEText(body, 'plain'))
print (data)
dat='%s.jpg'%data
print (dat)
attachment = open(dat, 'rb')
image=MIMEImage(attachment.read())
attachment.close()
mail.attach(image)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "********") #give the password of the email
text = mail.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
def capture_image():
data= time.strftime("%d_%b_%Y|%H:%M:%S") 
camera.start_preview()
time.sleep(6)
print (data)
camera.capture('%s.jpg'%data)
camera.stop_preview()
time.sleep(1)
sendMail(data)
camera = PiCamera()
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55
while 1:
if gpio.input(pir)==1:
capture_image()
while(gpio.input(pir)==1):
time.sleep(1)
else:
print('no motion')
time.sleep(0.01)

8.Solution:
app.py
from flask import Flask,render_template
import RPi.GPIO as GPIO
import time
LED_PIN=17 # Physical PIN 11
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
app=Flask( name )
@app.route('/')
def index():
return render_template('/index.html')
@app.route('/on')
def on():
GPIO.output(LED_PIN,GPIO.HIGH)
return "LED ON"
@app.route('/off')
def off():
GPIO.output(LED_PIN,GPIO.LOW)
return "LED OFF"
@app.route('/ledgetstatus')
def ledgetstatus():
while True:
status=GPIO.input(LED_PIN)
if status==True:
GPIO.output(LED_PIN,GPIO.HIGH)
return "status of bulb : ON"
else:
Mini Project with IOT Lab(22MCAL37) 32
GPIO.output(LED_PIN,GPIO.LOW)
return "status of bulb: OFF"
GPIO.cleanup()
if name ==' main ':
app.run(debug='true',host='192.168.0.110',port=8080)#ip address of
raspberry pi
index.html
<html>
<body>
<title>Raspberry pi Demo</title>
<h1>Raspberry pi Demo of controlling status of bulb at a remote place</h1>
<form action="http://192.168.0.110:8080/on">
<input type="submit" value="ON">
</form>
<form action="http://192.168.0.110:8080/off">
<input type="submit" value="OFF">
</form>
<form action="http://192.168.0.110:8080/ledgetstatus">
<input type="submit" value="getstatus">
</form>
</body>
</html>

8.
Solution:
import time
import botbook_mcp3002 as mcp #
smokeLevel= 0
def readSmokeLevel():
global smokeLevel
smokeLevel= mcp.readAnalog()
def main():
while True: #
readSmokeLevel() #
print ("Current smoke level is %i " % smokeLevel) #
if smokeLevel > 120:
print("Smoke detected")
time.sleep(0.5) # s
if_name_=="_main_":
main()

Solution:
int buzzer = 10;
intsmokeA0 = A5;
// Your threshold value
intsensorThres = 400;
void setup() {
pinMode(buzzer, OUTPUT);
pinMode(smokeA0, INPUT);
Serial.begin(9600);
}
void loop() {
int analogSensor = analogRead(smokeA0);
Serial.print("Pin A0: ");
Serial.println(analogSensor);
// Checks if it has reached the threshold value
if (analogSensor > sensorThres)
{
tone(buzzer, 1000, 200);
Serial.println("Smoke detected");
}
else
{
noTone(buzzer);
Serial.println("Smoke not detected");
}
delay(100);
}