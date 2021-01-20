#include "SoftwareSerial.h"
SoftwareSerial serial_connection(5, 6);//Create a serial connection with TX and RX on these pins
#define BUFFER_SIZE 64//This will prevent buffer overruns.
int value1= 0;
int value2= 0;
int value3= 0;
int value4= 0;
int var;
void setup() {
  // put your setup code here, to run once:
  pinMode(7, INPUT);
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  //Serial.begin(9600);
  serial_connection.begin(9600);
  serial_connection.println("Ready!!!");//Send something to just start comms. This will never be seen.
  //Serial.println("Started");//Tell the serial monitor that the sketch has started.
  digitalWrite(12 , HIGH);
  digitalWrite(11 , HIGH);
  delay(1000);
  digitalWrite(12 , LOW);
  digitalWrite(11 , LOW);
}

void loop() {
  //if (Serial.available()>0) 
  //{Serial.flush () // }
  
    char option = serial_connection.read();
    if(option=='1'){
        digitalWrite(10 , HIGH);
        digitalWrite(11 , LOW);
    }else if(option=='2'){
        digitalWrite(10 , LOW);
        digitalWrite(11 , HIGH);
    }else if(option=='3'){ 
        for (int i = 0; i <= 4; i++) {
        digitalWrite(10 , LOW);
        delay(50);
        digitalWrite(10 , HIGH);
        delay(50);  
        }
    }else if(option=='4'){ 
      for (int i = 0; i <= 4; i++) {
              digitalWrite(10 , LOW);
              digitalWrite(11 , HIGH);
              delay(50);
              digitalWrite(10 , HIGH);
              digitalWrite(11 , LOW);
              delay(50);  
        }
    }

  value1= digitalRead(7);
  value2= digitalRead(8);
  value3= digitalRead(9);
  value4= digitalRead(10);
  if (value3 == HIGH){
    var=3;
    
  }else if(value1 == HIGH){
    var=1;
    
  }else if (value2 == HIGH){
    var=2;
    
  }else if (value4 == HIGH){
    var=4;
    
  }else{
    var=0;
    
  }
  serial_connection.println(var);
}


