const int A = 5;
const int B = 6;
const int C = 9;
const int D = 10;


void setup(){
  pinMode(A, OUTPUT);
  pinMode(B, OUTPUT);
  pinMode(C, OUTPUT);
  pinMode(D, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  char command;
  if(Serial.available()>0){
    command = Serial.read();
    if(command == 'a')
    {
      analogWrite(5, 230);
      analogWrite(6, 255);
      analogWrite(9, 190);
      analogWrite(10, 220);
    }
    else if (command == 'b')
    {
      analogWrite(5, 0);
      analogWrite(6, 0);
      analogWrite(9, 0);
      analogWrite(10, 0);
    }
  }
}
