class blackKeys
{
  float dimensionX;
  float dimensionY;
  float dimensionX2;
  float dimensionY2;
  float volume;
  PFont font;
  SoundFile note;

  blackKeys(float dX1, float dY1, float dX2, float dY2, float v1, SoundFile n) {
    dimensionX = dX1;
    dimensionY = dY1;
    dimensionX2 = dX2;
    dimensionY2 = dY2;
    volume = v1;
    note = n;
  }
  //Creates Key using field
  void keyCreate() {
    font = loadFont("Ebrima-Bold-48.vlw");
    textFont(font);
    textSize(30);
    fill(255);
    rect(570, 600, 125, 100);
    fill(0);
    text(volume*100, 576, 660);
    stroke(0);
    strokeWeight(1);
    rect(dimensionX, dimensionY, dimensionX2, dimensionY2);
  }
  //When mouse hovers over the key, changes color rapidly
  void mouseInt() {
    fill(0);
    if ((mouseX >= dimensionX && mouseX <= dimensionX+dimensionX2 && mouseY >= dimensionY && mouseY <= dimensionY+dimensionY2)) {
      float C1 = random(255);
      float C2 = random(255);
      float C3 = random(255);
      fill(C1, C2, C3);
      rect(dimensionX, dimensionY, dimensionX2, dimensionY2);
      //When mouse is pressed on key, plays a noise as long as mouse is pressed
      if (mousePressed == true && mouseButton == LEFT) {
        note.play();
        note.amp(volume);
      }
    }
  }
  //Adjusts volume of key by holding 'w' to increase volume or 's' to decrease the volume and 'm' to mute volume
  void volume() {
    if (keyPressed) {
      if ((key == 'W' && volume<1)|| (key == 'w') && volume<0.99) {
        volume += 0.01;
        note.amp(volume);
      }
      if ((key == 'S' && volume>0)||(key == 's') && volume>0.01) {
        volume -= 0.01;
        note.amp(volume);
      }
      if ((key == 'M' && volume>0)||(key == 'm') && volume>0) {
        volume = 0;
        note.amp(volume);
      }
    }
  }
}
