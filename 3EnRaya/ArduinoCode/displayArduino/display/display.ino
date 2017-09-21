#include <EEPROM.h>
#include "SevSeg.h"

int eeAddress = 0;

SevSeg sevseg; //Instantiate a seven segment controller object
int wins;
int anteswins;
void setup() {
  Serial.begin(9600);
  int myTimeout = 5;  // milliseconds for Serial.readString
  Serial.setTimeout(myTimeout);
  byte numDigits = 8;
  byte digitPins[] = {2,3,4,5,9,8,7,6};
  byte segmentPins[] = {10, 11, A0, A1, A2, A3, A4, A5};
  bool resistorsOnSegments = false; // 'false' means resistors are on digit pins
  byte hardwareConfig = 2; // See README.md for options
  bool updateWithDelays = false; // Default. Recommended
  bool leadingZeros = false; // Use 'true' if you'd like to keep the leading zeros
  
  sevseg.begin(hardwareConfig, numDigits, digitPins, segmentPins, resistorsOnSegments, updateWithDelays, leadingZeros);
  sevseg.setBrightness(90);
  EEPROM.get(eeAddress,wins);
  sevseg.setNumber(wins, 0);
  Serial.print("init");
}

void loop() {
  anteswins=wins;
  if (Serial.available()>0){
    String x = Serial.readString();
    //Serial.println(x);
    String mode = getValue(x, ':', 0);
    String number = getValue(x, ':', 1);
    int numberval = number.toInt();
    Serial.print(mode);
    //char modeval=mode.toChar();
    if (mode=="t\n" || mode=="t"){
      TramposoFull();
      sevseg.setNumber(wins, 0);
    }
    if (mode=="w\n" || mode=="w"){
      ThorWinsFull();
    }
    if (mode=="l\n" || mode=="l"){
      wins--;
    }
    if (mode=="s\n" || mode=="s"){
      wins=numberval;
    }
    if (mode=="r\n" || mode=="r"){
      wins=0;
    }
  }
  if(anteswins!=wins){
    sevseg.setNumber(wins, 0);
    EEPROM.put( eeAddress, wins );
  }

  sevseg.refreshDisplay(); // Must run repeatedly
}

String getValue(String data, char separator, int index)
{
    int found = 0;
    int strIndex[] = { 0, -1 };
    int maxIndex = data.length() - 1;

    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == separator || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i+1 : i;
        }
    }
    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}
void ThorWins(){
  bool ThorWinsTime=true;
  bool ThorWinsFraseUno=false;
  bool ThorWinsFraseDos=false;
  bool ThorWinsFraseBlank=false;
  unsigned long temporizador = millis();
  while (ThorWinsTime){
    char fraseWinUno[8]={'t','h','o','r','g','a','n','a'};
    char fraseBlank[8]={' ',' ',' ',' ',' ',' ',' ',' '};
    char fraseWinDos[8]={'t','h','o','r','g','a','n','a'};
    if (millis()-temporizador<2000 && ThorWinsFraseUno==false){
      sevseg.setChars(fraseWinUno);
      ThorWinsFraseUno=true;
    }
    if (millis()-temporizador>2000 && ThorWinsFraseBlank==false){
      sevseg.setChars(fraseBlank);
      ThorWinsFraseBlank=true;
    }
    if (millis()-temporizador>2300 && ThorWinsFraseDos==false){
      sevseg.setChars(fraseWinDos);
      ThorWinsFraseDos=true;
    }
    if (millis()-temporizador>4000){
    wins++;
    ThorWinsTime=false;
    }
    sevseg.refreshDisplay();
   }
}

void ThorWinsFull(){
  bool ThorWinsTime=true;
  bool ThorWinsFrase=false;
  bool ThorWinsFraseBlank=false;
  unsigned long temporizador = millis();
  int showTime=500;
  char fraseThorWins[8] = {'t','h','o','r','g','a','n','a'};
  char fraseBlank[8]={' ',' ',' ',' ',' ',' ',' ',' '};
  for (int i=0; i<10; i++){
    ThorWinsTime=true;
    temporizador = millis();
    while (ThorWinsTime){
      if (millis()-temporizador<showTime && ThorWinsFrase==false){
        sevseg.setChars(fraseThorWins);
        ThorWinsFrase=true;
      }
      if (millis()-temporizador>showTime && ThorWinsFraseBlank==false){
        sevseg.setChars(fraseBlank);
        ThorWinsFraseBlank=true;
      }
      if (millis()-temporizador>(showTime+showTime)){
        ThorWinsTime=false;
        ThorWinsFrase=false;
        ThorWinsFraseBlank=false;
      }
      sevseg.refreshDisplay();
    }
  }
  wins++;
  sevseg.refreshDisplay();
}

void TramposoFull(){
  bool TramposoTime=true;
  bool TramposoFrase=false;
  bool TramposoFraseBlank=false;
  bool TramposoFraseDos=false;
  unsigned long temporizador = millis();
  int showTime=500;
  char fraseTramposo[8] = {'t','r','a','m','p','o','s','o'};
  char fraseBlank[8]={' ',' ',' ',' ',' ',' ',' ',' '};
  for (int i=0; i<10; i++){
    TramposoTime=true;
    temporizador = millis();
    while (TramposoTime){
      if (millis()-temporizador<showTime && TramposoFrase==false){
        sevseg.setChars(fraseTramposo);
        TramposoFrase=true;
      }
      if (millis()-temporizador>showTime && TramposoFraseBlank==false){
        sevseg.setChars(fraseBlank);
        TramposoFraseBlank=true;
      }
      if (millis()-temporizador>(showTime+showTime)){
        TramposoTime=false;
        TramposoFrase=false;
        TramposoFraseBlank=false;
      }
      sevseg.refreshDisplay();
    }
  }
}
