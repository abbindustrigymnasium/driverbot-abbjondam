#include <EspMQTTClient.h>
//Install libraries PubSubClient and EspMQTTClient
#include <Servo.h>

Servo servo;

void onConnectionEstablished();

EspMQTTClient client(
  "ASUS_Guest1",           // Wifi ssid
  "jondriverbot",           // Wifi password
  "maqiatto.com",  // MQTT broker ip
  1883,             // MQTT broker port
  "jonathan.damsgaardfalck@abbindustrigymnasium.se",            // MQTT username
  "jondriverbot",       // MQTT password
  "JonathanClient",          // Client name
  onConnectionEstablished, // Connection established callback
  true,             // Enable web updater
  true              // Enable debug messages
);


#define motorPinRightDir  0//D2
#define motorPinRightSpeed 5//D1
#define motorPinLeftDir 2
#define motorPinLeftSpeed 4

int degrees = 90; 

void setup() {
  servo.attach(14); //D5
  pinMode(motorPinRightDir, OUTPUT);
  pinMode(motorPinRightSpeed, OUTPUT);
  Serial.begin(115200);
  servo.write(90);
}

bool off = false;

void turn(bool left, int svang) {

  if (left == true)
  {
    degrees -= svang;

    if (degrees < 0)
    {
      degrees = 0;
    }
    servo.write(degrees);
    Serial.println("Svänger vänster");
  }
  else
  {

    degrees += svang;
    if (degrees > 180)
    {
      degrees = 180;
    }
    servo.write(degrees);
    Serial.println("Svänger höger");

  }
  Serial.println(degrees);


}

void drive(bool dir, int speed) {

  servo.write(90);
  Serial.println("Åker");
  Serial.println(speed);
  digitalWrite(motorPinRightDir, dir);
  analogWrite(motorPinRightSpeed, speed);
}

void onConnectionEstablished()
{

  client.subscribe("jonathan.damsgaardfalck@abbindustrigymnasium.se/driverbot", [] (const String & payload)
  {

    int length = payload.length();
    int commaIndex = payload.indexOf(',');
    String turnstring = payload.substring(0,commaIndex);
    String drivestring = payload.substring(commaIndex + 2,length);
    int turnlength = turnstring.length();
    int drivelength = drivestring.length();
    char info = payload.charAt(0);
    char info2 = payload.charAt(commaIndex+1);
    bool fb = false;
    bool dir = false;
    if (drivelength > 0)
    {
      String hastighet = drivestring,substring(1,drivelength);
      int speed = hastighet.toInt();
      if (info2 == 'f')
        fb = true;
      else if (info2 == 'b'){
        fb = false;  
      }
      drive(fb, speed);
    }
    if (turnlength > 0)
    {
      String thastighet = turnstring.substring(1,turnlength);
      int tspeed = thastighet.toInt();
      if (info == 'v')
        dir = true;
      else if (info == 'h'){
        dir = false;  
      }
      turn(dir, tspeed);
    }
   
    Serial.println(payload); 

  });

  client.publish("jonathan.damsgaardfalck@abbindustrigymnasium.se/driverbot", "Connected");
}


void loop() {
  client.loop();
}