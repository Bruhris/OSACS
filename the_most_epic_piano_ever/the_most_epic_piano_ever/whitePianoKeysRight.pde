class whitePianoKeysRight
{
  float dimensionX;
  float dimensionY;
  float dimensionX2;
  float dimensionY2;
  float volume;
  SoundFile note;

  whitePianoKeysRight(float dX1, float dY1, float dX2, float dY2, float v1, SoundFile n) {
    dimensionX = dX1;
    dimensionY = dY1;
    dimensionX2 = dX2;
    dimensionY2 = dY2;
    volume = v1;
    note = n;
  }
  void keyCreate() {
    stroke(0);
    strokeWeight(1);
    rect(dimensionX, dimensionY, dimensionX2, dimensionY2);
  }
  void mouseInt() {
    fill(255);
    if ((mouseX >= dimensionX && mouseX <= dimensionX+dimensionX2-25 && mouseY >= dimensionY && mouseY <= dimensionY+dimensionY2)||(mouseX >= dimensionX+dimensionX2-25 && mouseX <= dimensionX+dimensionX2 && mouseY >= 400 && mouseY <= 550)) {
      float C1 = random(255);
      float C2 = random(255);
      float C3 = random(255);
      fill(C1, C2, C3);
      if (mousePressed == true && mouseButton == LEFT) {
        note.play();
        note.amp(volume);
      }
    }
  }
  //Adjusts volume of key by holding M to increase volume or N to decrease the volume
  void volume() {
    if (keyPressed) {
      if ((key == 'W')|| (key == 'w') && volume<1) {
        volume += 0.01;
        note.amp(volume);
      }
      if ((key == 'S'&& volume>0.01)|| (key == 's') && volume>0) {
        volume -= 0.01;
        note.amp(volume);
      }if ((key == 'M' && volume>0)||(key == 'm') && volume>0) {
        volume = 0;
        note.amp(volume);
      }
    }
  }
}
