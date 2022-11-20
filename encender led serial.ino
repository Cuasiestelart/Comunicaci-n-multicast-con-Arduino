int option;

void setup(){
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
}

void loop(){
  if (Serial.available() > 0){
    option = Serial.read();
    Serial.println(option);

    if(option == 'P'){
      digitalWrite(13, HIGH);                 
    }

    if(option == 'N'){
    digitalWrite(13, LOW);  
    }  
  }
}