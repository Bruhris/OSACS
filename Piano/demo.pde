class demo
{  
  PFont font;
  SoundFile note1;
  SoundFile note2;
  SoundFile note3;
  SoundFile note4;
  SoundFile note5;
  SoundFile note6;
  SoundFile note7;
  SoundFile note8;
  SoundFile note9;
  SoundFile note10;
  

  demo(SoundFile n1, SoundFile n2, SoundFile n3,SoundFile n4,SoundFile n5,SoundFile n6,SoundFile n7,SoundFile n8,SoundFile n9,SoundFile n10) {
    note1 = n1;
    note2 = n2;
    note3 = n3;
    note4 = n4;
    note5 = n5;
    note6 = n6;
    note7 = n7;
    note8 = n8;
    note9 = n9;
    note10 = n10;
    
  }
  //When you click "Click to play demo!" box, will play demo 
  void playD() {
    if (mouseX>=887 && mouseX<=1187 && mouseY>=605 && mouseY<=685 && mousePressed) {
      note1.play();
      delay(1000);  
      note2.play();
      delay(1000);   
      note3.play();
      delay(1000);
      note4.play();
      delay(1000); 
      note5.play();
      delay(1000);
      note6.play();
      delay(1000);
      note7.play();
      delay(1000);
      note8.play();
      delay(1600);
      note9.play();
      delay(1000);
      note10.play();
      delay(3200);
      note1.stop();
      note2.stop();
      note3.stop();
      note4.stop();
      note5.stop();
      note6.stop();
      note7.stop();      
      note8.stop();      
      note9.stop();      
      note10.stop(); 
    }
  }
}
