void setup()
{
  pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(8,OUTPUT);
  
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(7,OUTPUT);

  pinMode(11,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(5,OUTPUT);
  Serial.begin(9600);
  // initialize control over the keyboard:
}

void loop()
{
  delay(5000);
  
  analogWrite(6,255);//TL
  analogWrite(5,255);//TR
  analogWrite(10,255);//BL
  analogWrite(11,255);//BR
  
  digitalWrite(2, LOW);//TR
  digitalWrite(3,HIGH);

  digitalWrite(4,LOW);//TL
  digitalWrite(7,HIGH);
  
  digitalWrite(8,HIGH);//BL
  digitalWrite(9,LOW);

  digitalWrite(12,HIGH);//BR
  digitalWrite(13,LOW);

    delay(1000);
 
}
