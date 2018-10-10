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
  if (Serial.available() > 0)
  {
 char    inChar = Serial.read();
 if( inChar == 'w') //For
 {
  analogWrite(6,120);//TL
  analogWrite(5,120);//TR
  analogWrite(10,120);//BL
  analogWrite(11,120);//BR
  
  digitalWrite(2, LOW);//TR
  digitalWrite(3,HIGH);

  digitalWrite(4,LOW);//TL
  digitalWrite(7,HIGH);
  
  digitalWrite(8,HIGH);//BL
  digitalWrite(9,LOW);

  digitalWrite(12,HIGH);//BR
  digitalWrite(13,LOW);

    delay(200);

  digitalWrite(2, LOW);//TR
  digitalWrite(3,LOW);

  digitalWrite(4,LOW);//TL
  digitalWrite(7,LOW);
  
  digitalWrite(8,LOW);//BL
  digitalWrite(9,LOW);

  digitalWrite(12,LOW);//BR
  digitalWrite(13,LOW);

 }

 if( inChar == 's') //Back
 {
  analogWrite(6,120);//TL
  analogWrite(5,120);//TR
  analogWrite(10,120);//BL
  analogWrite(11,120);//BR
  digitalWrite(2, HIGH);//TR
  digitalWrite(3,LOW);

  digitalWrite(4,HIGH);//TL
  digitalWrite(7,LOW);
  
  digitalWrite(8,LOW);//BL
  digitalWrite(9,HIGH);

  digitalWrite(12,LOW);//BR
  digitalWrite(13,HIGH);
  
   delay(300);

  digitalWrite(2, LOW);//TR
  digitalWrite(3,LOW);

  digitalWrite(4,LOW);//TL
  digitalWrite(7,LOW);
  
  digitalWrite(8,LOW);//BL
  digitalWrite(9,LOW);

  digitalWrite(12,LOW);//BR
  digitalWrite(13,LOW);
 }

 if( inChar == 'a') //Left
 {
  analogWrite(6,180);//TL
  analogWrite(5,120);//TR
  analogWrite(10,120);//BL
  analogWrite(11,180);//BR
  
  digitalWrite(2, LOW);//TR
  digitalWrite(3,HIGH);

  digitalWrite(4,HIGH);//TL
  digitalWrite(7,LOW);
  
  digitalWrite(8,LOW);//BL
  digitalWrite(9,HIGH);

  digitalWrite(12,HIGH);//BR
  digitalWrite(13,LOW);
  
   delay(200);

  digitalWrite(2, LOW);//TR
  digitalWrite(3,LOW);

  digitalWrite(4,LOW);//TL
  digitalWrite(7,LOW);
  
  digitalWrite(8,LOW);//BL
  digitalWrite(9,LOW);

  digitalWrite(12,LOW);//BR
  digitalWrite(13,LOW);
 }

 else if( inChar == 'd') //Right
 {
  analogWrite(6,120);//TL
  analogWrite(5,155);//TR
  analogWrite(10,155);//BL
  analogWrite(11,120);//BR
  
  digitalWrite(2, HIGH);//TR
  digitalWrite(3,LOW);

  digitalWrite(4,LOW);//TL
  digitalWrite(7,HIGH);
  
  digitalWrite(8,HIGH);//BL
  digitalWrite(9,LOW);

  digitalWrite(12,LOW);//BR
  digitalWrite(13,HIGH);

  delay(200);

  digitalWrite(2, LOW);//TR
  digitalWrite(3,LOW);

  digitalWrite(4,LOW);//TL
  digitalWrite(7,LOW);
  
  digitalWrite(8,LOW);//BL
  digitalWrite(9,LOW);

  digitalWrite(12,LOW);//BR
  digitalWrite(13,LOW);
  
 }

  else if( inChar == 'x') //Right
 {
  digitalWrite(2, LOW);//TR
  digitalWrite(3,LOW);

  digitalWrite(4,LOW);//TL
  digitalWrite(7,LOW);
  
  digitalWrite(8,LOW);//BL
  digitalWrite(9,LOW);

  digitalWrite(12,LOW);//BR
  digitalWrite(13,LOW);
 }
 
}
}
