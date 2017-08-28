/*
  DigitalReadSerial
 Reads a digital input on pin 2, prints the result to the serial monitor 
 
 This example code is in the public domain.
 */

// digital pin 2 has a pushbutton attached to it. Give it a name:
int casillas[] = {2,3,4,5,6,7,8,9,10};
bool casillasState[] = {0,0,0,0,0,0,0,0,0};

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  // make the pushbutton's pin an input:
  int i=0;
  for (i=0;i<9;i++){
    pinMode(casillas[i], INPUT);
  }
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input pin:
  int k=0;
  for (k=0;k<9;k++){
    casillasState[k] = digitalRead(casillas[k]);
  }
  // print out the state of the button:
  Serial.println("");
  Serial.println("");
  Serial.println("");
  
  int l=0;
  for (l=0;l<9;l++){
    Serial.print(casillasState[l]);
    if ((l+1)%3==0){
      Serial.println("");
    }
    else{
      Serial.print(" ,");
    }
  }
  delay(1000);        // delay in between reads for stability
}



