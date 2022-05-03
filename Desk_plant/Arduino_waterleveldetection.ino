#include "TM1637.h"

//Set up 4*7 seg display
const int CLK = 4;
const int DIO = 5;
TM1637 tm1637(CLK, DIO);

int sensorPin = A0;    // select the input pin for the potentiometer
int pump_1 = 8;      // select the pin for the LED
int sensorValue = 0;  // variable to store the value coming from the sensor

void setup() {
  tm1637.init();
  tm1637.set(2);//BRIGHT_TYPICAL = 2,BRIGHT_DARKEST = 0,BRIGHTEST = 7;
  // declare the ledPin as an OUTPUT:
  pinMode(pump_1, OUTPUT);
  Serial.begin(9600);
  pinMode(A0,INPUT);
  digitalWrite(pump_1,HIGH);
  delay(10000);
}

void loop() {
  // read the value from the sensor:
  //350 dry 520 very wet
  sensorValue = map(analogRead(sensorPin),200,600,100,0);
  Serial.println(sensorValue);
  tm1637.displayNum(sensorValue);
  //CODE FOR ACTIVATING RELAY CONNECTED TO PUMP. COMMENTED FOR TESTING
  /*if (sensorValue < 50)
  {
    digitalWrite(pump_1,LOW);
    delay(2000);
    digitalWrite(pump_1,HIGH);
  }*/
  delay(1000*30);
}