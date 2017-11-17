/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
#include <IRremote.h>

const int directionA = 12;
const int directionB = 13;
const int pwmA = 3;
const int pwmB = 11;
const int receiver = 9;

IRrecv irrecv(receiver);
decode_results results;


// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  Serial.begin(9600);
  pinMode(directionA, OUTPUT);  
  pinMode(directionB, OUTPUT);
  pinMode(pwmA, OUTPUT);
  pinMode(pwmB, OUTPUT);  
  irrecv.enableIRIn();
}

// the loop routine runs over and over again forever:
void loop() {
 if (irrecv.decode(&results)) { //we have received an IR
 Serial.println (results.value, HEX); //display HEX
 irrecv.resume(); //next value
 }
}
