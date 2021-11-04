/* ***********************************************************************
 * Boris Wang
 * Big Piano
 * Block 3
 * Completed November 20, 2020
 
 * This program is my own work - B.W   */


/* 
 -Hover over keys to make them rapidly change color
 -Press them to make noise
 -Left click box "Notes" to see the notes on the keyboard, right click to hide 
 -Press 'w' to increase volume and 's' to decrease and 'm' to mute
 -Press 'Sound Demo' box to hear a small song played by the piano
 -Microphone Tester: the louder noise you make, the bigger the ball will be, the smaller noise you make, the smaller the ball will be
 -Credit to user: Violet Whitney, for Microphone Tester function
 Link to code: https://medium.com/measuring-the-great-indoors/sounds-speech-in-processing-df1e908940c
 */




import processing.sound.*;
PFont font;
boolean clickedOn = false;
boolean clickOn1 = false;
AudioIn input;
Amplitude analyzer;
whitePianoKeysBoth key2, key5, key6, key9;
whitePianoKeysRight key1, key4, key8;
whitePianoKeysLeft key3, key7, key10;
blackKeys key11, key12, key13, key14, key15, key16, key17;
demo demo1;
//SoundFile assignment
SoundFile C1_note;
SoundFile Db1_note;
SoundFile D1_note;
SoundFile Eb1_note;
SoundFile E1_note;
SoundFile F1_note;
SoundFile Gb1_note;
SoundFile G1_note;
SoundFile Ab1_note;
SoundFile A1_note;
SoundFile Bb1_note;
SoundFile B1_note;
SoundFile C2_note;
SoundFile Db2_note;
SoundFile D2_note;
SoundFile Eb2_note;
SoundFile E2_note;


void setup()
{
  size(1280, 720);
  fill(0);
  smooth();
  input = new AudioIn(this, 0);
  input.start();
  analyzer = new Amplitude(this);
  analyzer.input(input);
  //Import Sound Effects
  C1_note = new SoundFile(this, "Piano.mf.C3.aiff");
  Db1_note = new SoundFile(this, "Piano.mf.Db3.aiff");
  D1_note = new SoundFile(this, "Piano.mf.D3.aiff");
  Eb1_note = new SoundFile(this, "Piano.mf.Eb3.aiff");
  E1_note = new SoundFile(this, "Piano.mf.E3.aiff");
  F1_note = new SoundFile(this, "Piano.mf.F3.aiff");
  Gb1_note = new SoundFile(this, "Piano.mf.Gb3.aiff");
  G1_note = new SoundFile(this, "Piano.mf.G3.aiff");
  Ab1_note = new SoundFile(this, "Piano.mf.Ab3.aiff");
  A1_note = new SoundFile(this, "Piano.mf.A3.aiff");
  Bb1_note = new SoundFile(this, "Piano.mf.Bb3.aiff");
  B1_note = new SoundFile(this, "Piano.mf.B3.aiff");
  C2_note = new SoundFile(this, "Piano.mf.C4.aiff");
  Db2_note = new SoundFile(this, "Piano.mf.Db4.aiff");
  D2_note = new SoundFile(this, "Piano.mf.D4.aiff");
  Eb2_note = new SoundFile(this, "Piano.mf.Eb4.aiff");
  E2_note = new SoundFile(this, "Piano.mf.E4.aiff");  
  
  //Using constructor
  key1 = new whitePianoKeysRight(0, 150, 128, 400, 0.5, C1_note);
  key2 = new whitePianoKeysBoth(128, 150, 128, 400, 0.5, D1_note);
  key3 = new whitePianoKeysLeft(256, 150, 128, 400, 0.5, E1_note);
  key4 = new whitePianoKeysRight(384, 150, 128, 400, 0.5, F1_note);
  key5 = new whitePianoKeysBoth(512, 150, 128, 400, 0.5, G1_note);
  key6 = new whitePianoKeysBoth(640, 150, 128, 400, 0.5, A1_note);
  key7 = new whitePianoKeysLeft(768, 150, 128, 400, 0.5, B1_note);
  key8 = new whitePianoKeysRight(896, 150, 128, 400, 0.5, C2_note);
  key9 = new whitePianoKeysBoth(1024, 150, 128, 400, 0.5, D2_note);
  key10 = new whitePianoKeysLeft(1152, 150, 128, 400, 0.5, E2_note);
  key11 = new blackKeys(103, 150, 50, 250, 0.5, Db1_note);
  key12 = new blackKeys(231, 150, 50, 250, 0.5, Eb1_note);
  key13 = new blackKeys(487, 150, 50, 250, 0.5, Gb1_note);
  key14 = new blackKeys(615, 150, 50, 250, 0.5, Ab1_note);
  key15 = new blackKeys(743, 150, 50, 250, 0.5, Bb1_note);
  key16 = new blackKeys(999, 150, 50, 250, 0.5, Db2_note);
  key17 = new blackKeys(1127, 150, 50, 250, 0.5, Eb2_note);
  demo1 = new demo(D1_note, D1_note, D2_note, A1_note, Ab1_note, G1_note, F1_note, D1_note, F1_note, G1_note);
  //Font assignment
  font = loadFont("Ebrima-Bold-48.vlw");
  textFont(font);
  textSize(30);
}

void draw()
{
  //Initial piano background
  background(#FFC8C6);
  fill(255);
  noStroke();
  rect(0, 150, 1280, 400);
  stroke(0);
  strokeWeight(1);
  line(0, 150, 1280, 150);
  line(0, 550, 1280, 550);
  //Run class functions
  key1.volume();
  key1.mouseInt();
  key1.keyCreate();
  key2.volume();
  key2.mouseInt();
  key2.keyCreate();
  key3.volume();
  key3.mouseInt();
  key3.keyCreate();
  key4.volume();
  key4.mouseInt();
  key4.keyCreate();
  key5.volume();
  key5.mouseInt();
  key5.keyCreate();
  key6.volume();
  key6.mouseInt();
  key6.keyCreate();
  key7.volume();
  key7.mouseInt();
  key7.keyCreate();
  key8.volume();
  key8.mouseInt();
  key8.keyCreate();
  key9.volume();
  key9.mouseInt();
  key9.keyCreate();
  key10.volume();
  key10.mouseInt();
  key10.keyCreate();
  //Black Key Functions
  key11.volume();
  key11.keyCreate();
  key11.mouseInt();
  key12.volume();
  key12.keyCreate();
  key12.mouseInt();
  key13.volume();
  key13.keyCreate();
  key13.mouseInt();
  key14.volume();
  key14.keyCreate();
  key14.mouseInt();
  key15.volume();
  key15.keyCreate();
  key15.mouseInt();
  key16.volume();
  key16.keyCreate();
  key16.mouseInt();
  key17.volume();
  key17.keyCreate();
  key17.mouseInt();
  demo1.playD();
  //Piano Overlay
  float vol = analyzer.analyze();
  stroke(0);
  strokeWeight(1);
  fill(255);
  rect(75, 610, 100, 100);
  stroke(0);
  strokeWeight(1);
  fill(127);
  ellipse(125, 665, 17+vol*150, 17+vol*150);
  fill(255);
  rect(585, 13, 100, 32);
  fill(255);
  rect(887, 605, 300, 80);
  fill(0);
  text("Notes:", 590, 40);
  text("Microphone Tester", 25, 590);
  text("Volume", 580, 590);
  text("Sound Demo", 945, 590);
  text("Click to play demo!", 900, 660);
  /*If leftmousePressed on the "Notes" Box, shows all notes on Piano, and if right mouse is clicked,
   removed the notes
   */
  if (clickedOn) {
    fill(0);
    text("C", 50, 90);
    text("Db", 110, 120);
    text("D", 185, 90);
    text("Eb", 240, 120);
    text("E", 320, 90);
    text("F", 440, 90);
    text("Gb", 495, 120);
    text("G", 565, 90);
    text("Ab", 620, 120);
    text("A", 690, 90);
    text("Bb", 750, 120);
    text("B", 815, 90);
    text("C", 940, 90);
    text("Db", 1000, 120);
    text("D", 1080, 90);
    text("Eb", 1140, 120);
    text("E", 1200, 90);
  }
}
//Changes the value of clickedOn for the box "Notes"
void mouseClicked() {
  if (mouseX>=585 && mouseX<=685 && mouseY>=13 && mouseY <=45 && mouseButton == LEFT) {
    clickedOn = true;
  } else if (mouseX>=585 && mouseX<=685 && mouseY>=13 && mouseY <=45 && mouseButton == RIGHT) {
    clickedOn= false;
  }
}
