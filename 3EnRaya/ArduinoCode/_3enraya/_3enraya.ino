int Button = 12;
int previousButtonState = 0;
int currentButtonState = 0;

int casillas[] = {2,3,4,5,6,7,8,9,10};
int casillasState[] = {0,0,0,0,0,0,0,0,0};

String message = String();

void setup() {
  Serial.begin(9600);
  int i=0;
  for (i=0;i<9;i++){
    pinMode(casillas[i], INPUT);
  }
  pinMode(Button, INPUT);

}

void loop() {
  currentButtonState = digitalRead(Button);
  if (currentButtonState==1 && previousButtonState==0){
      int k=0;
      for (k=0;k<9;k++){
        casillasState[k] = digitalRead(casillas[k]);
      }
      message = message + casillasState[0] + casillasState[1] + casillasState[2] + casillasState[3] + casillasState[4] + casillasState[5] + casillasState[6] + casillasState[7] + casillasState[8];
      Serial.println(message);
      message="";
  }
  previousButtonState = currentButtonState;
  delay(100);
}
//          Serial.print(casillasState[l]);
//        }
//        Serial.println("");


        /*int l=0;                           // Graphically
        for (l=0;l<9;l++){
          Serial.print(casillasState[l]);
          if ((l+1)%3==0){
            Serial.println("");
          }
          else{
            Serial.print(" ,");
          }
        }*/
          


