/* ***********************************************************************
 * Boris Wang
 * Assignment 2 - Paint by Dot
 * Block 3
 * October 10, 2020
 * This program is my own work - Digital Signature (B.W)   
 * Credit to user: linar, for undo and redo command using CTRL+Z and CTRL+SHIFT+Z
 * Link to forum: https://forum.processing.org/two/discussion/7953/redo-and-undo-button-in-paint-like-app 
 * Credit to Youtube user: Richie Byrne, for function to save image as .png and .jpg
 * Link to video: https://youtu.be/v67qwEsVB1k*/



//Variable Assignment
float x;
float y;
float z;
float radius = 5;
int num;
float transparency = 255;
boolean controlDown = false;
boolean shiftDown = false;

PImage colorReset;
PImage red;
PImage green;
PImage blue;
PImage frame;
PImage plus;
PImage plusSmall;
PImage minus;
PImage minusSmall;
PImage plusA;
PImage plusSmallA;
PImage minusA;
PImage minusSmallA;
PImage save;
PFont settingsFont;

Undo undo;

void setup() {
  size(1280, 720);
  smooth();
  background(255);
  noStroke();
  ellipseMode(RADIUS);
  fill(0);
  //Image +Font Assignment
  colorReset = loadImage("PixelArt.png");
  red = loadImage("clipart332678.png");
  green = loadImage("PinClipart.com_scribble-clipart_2898172.png");
  blue = loadImage("Blue-Scribble-PNG.png");
  frame = loadImage("pngkit_borders-png_50788.png");
  plus = loadImage("ClipartKey_1100494.png");
  plusSmall = loadImage("ClipartKey_1100494.png");
  minus = loadImage("pnghut_plus-and-minus-signs-plus-minus-sign-meno-symbol_xbfH2BLG4L.png");
  minusSmall = loadImage("pnghut_plus-and-minus-signs-plus-minus-sign-meno-symbol_xbfH2BLG4L.png");
  plusA = loadImage("ClipartKey_1100494.png");
  plusSmallA = loadImage("ClipartKey_1100494.png");
  minusA = loadImage("pnghut_plus-and-minus-signs-plus-minus-sign-meno-symbol_xbfH2BLG4L.png");
  minusSmallA = loadImage("pnghut_plus-and-minus-signs-plus-minus-sign-meno-symbol_xbfH2BLG4L.png");
  save = loadImage("Actions-document-save-icon.png");
  settingsFont = loadFont("ProcessingSansPro-Semibold-48.vlw");
  textFont(settingsFont);
  undo = new Undo(300);
}
//Clear canvas command
void draw() {
  if (keyPressed) {
    if ((key == 'c')||(key == 'C')) {
      background(255);
    }
  }
  colorPalette();
  dotSize();
  transparency();
  //Dot painting command
  if (mousePressed) {
    if (mouseX>-25 && mouseX<1050 && mouseY>-25 && mouseY<770) {
      noStroke();
      fill(x, y, z, transparency);
      ellipse(mouseX, mouseY, radius, radius);
    }
  }
  //Canvas
  frame.resize(1050, 770);
  image(frame, -25, -25);
  //Settings Area
  fill(255);
  rect(1000, 0, 280, 720);
  stroke(0);
  strokeWeight(3);
  line(1000, 0, 1000, 720);
  line(1000, 1, 1280, 1);
  line(1278, 0, 1278, 720);
  line(1000, 719, 1280, 719);
  dotImage();
  //Color Sections of Setting
  stroke(0);
  strokeWeight(3);
  line(1000, 60, 1280, 60); 
  line(1000, 210, 1280, 210);
  blue.resize(60, 60);
  image(blue, 1025, 68);
  red.resize(50, 50);
  image(red, 1115, 75);
  green.resize(50, 45);
  image(green, 1200, 75);
  colorReset.resize(75, 65);
  image(colorReset, 1100, 135);
  //Dot size sections of settings
  line(1000, 370, 1280, 370);
  minus.resize(50, 50);
  plus.resize(50, 50);
  image(plus, 1020, 270);
  image(minus, 1210, 270);
  plusSmall.resize(30, 30);
  minusSmall.resize(30, 30);
  image(minusSmall, 1160, 280);
  image(plusSmall, 1090, 280);
  //Transparency Images
  line(1000, 520, 1280, 520);
  minusA.resize(50, 50);
  plusA.resize(50, 50);
  image(plusA, 1020, 440); 
  image(minusA, 1210, 440);
  plusSmallA.resize(30, 30);
  minusSmallA.resize(30, 30);
  image(minusSmallA, 1160, 450);
  image(plusSmallA, 1090, 450);
  //Save file image
  save.resize(50, 50);
  image(save, 1010, 570);
  image(save, 1010, 650);
  line(1180, 520, 1180, 720);
  line(1000, 563, 1280, 563);
  //Text
  fill(0);
  textSize(36);
  text("Colors", 1090, 45);
  text("Size", 1110, 250);
  text("Transparency", 1030, 410);
  textSize(24);
  text("Save Image As:", 1010, 550);
  text(".png", 1070, 610);
  text(".jpg", 1070, 690);
  text("Dot", 1210, 550);
}
void mouseReleased() {
  // Save each line we draw to our stack of UNDOs
  undo.takeSnapshot();
}

void keyPressed() {
  // Remember if CTRL or SHIFT are pressed or not
  if (key == CODED) {
    if (keyCode == CONTROL)
      controlDown = true;
    if (keyCode == SHIFT)
      shiftDown = true;
    return;
  }
  // Check if we pressed CTRL+Z or CTRL+SHIFT+Z
  if (controlDown) {
    if (keyCode == 'Z') {
      if (shiftDown)
        undo.redo();
      else
        undo.undo();
    }
    return;
  }
  // Check if we pressed the S key
  if (key=='s') {
    saveFrame("image####.png");
  }
}


void keyReleased() {
  // Remember if CTRL or SHIFT are pressed or not
  if (key == CODED) {
    if (keyCode == CONTROL)
      controlDown = false;
    if (keyCode == SHIFT)
      shiftDown = false;
  }
}


class Undo {
  // Number of currently available undo and redo snapshots
  int undoSteps=0, redoSteps=0; 
  CircImgCollection images;

  Undo(int levels) {
    images = new CircImgCollection(levels);
  }

  public void takeSnapshot() {
    undoSteps = min(undoSteps+1, images.amount-1);
    // each time we draw we disable redo
    redoSteps = 0;
    images.next();
    images.capture();
  }
  public void undo() {
    if (undoSteps > 0) {
      undoSteps--;
      redoSteps++;
      images.prev();
      images.show();
    }
  }
  public void redo() {
    if (redoSteps > 0) {
      undoSteps++;
      redoSteps--;
      images.next();
      images.show();
    }
  }
}


class CircImgCollection {
  int amount, current;
  PImage[] img;
  CircImgCollection(int amountOfImages) {
    amount = amountOfImages;

    // Initialize all images as copies of the current display
    img = new PImage[amount];
    for (int i=0; i<amount; i++) {
      img[i] = createImage(width, height, RGB);
      img[i] = get();
    }
  }
  void next() {
    current = (current + 1) % amount;
  }
  void prev() {
    current = (current - 1 + amount) % amount;
  }
  void capture() {
    img[current] = get();
  }
  void show() {
    image(img[current], 0, 0);
  }
}
//Save painting command by clicking on icons
void mouseClicked() { // 1010, 570, 1010, 650
  if (mouseX>1010 && mouseX<1060 && mouseY>570 && mouseY<620 && mouseButton == LEFT) {
    selectFolder("Select a folder to save image:", "folderSelectedPNG");
  }
  if (mouseX>1010 && mouseX<1060 && mouseY>650 && mouseY<700 && mouseButton == LEFT) {
    selectFolder("Select a folder to save image:", "folderSelectedJPG");
  }
}
//Transparency Settings by clicking on icons
public void transparency() { //1020, 440, 1210, 440, 1160, 450, 1090, 450
  if (mousePressed) {
    if (mouseX>1020 && mouseX<1070 && mouseY>440 && mouseY<470 && transparency<255 && mouseButton == LEFT) {
      transparency+=1;
    }
    if (mouseX>1090 && mouseX<1120 && mouseY>450 && mouseY<480 && transparency<255 && mouseButton == LEFT) {
      transparency+=0.5;
    }
    if (mouseX>1210 && mouseX<1260 && mouseY>440 && mouseY<470 && transparency>0 && mouseButton == LEFT) {
      transparency-=1;
    }
    if (mouseX>1160 && mouseX<1190 && mouseY>450 && mouseY<480 && transparency>0 && mouseButton == LEFT) {
      transparency-=0.5;
    }
  }
}
//Size of dot settings by clicking on icons
public void dotSize() {
  if (mousePressed) {
    if (mouseX>1020 && mouseX<1070 && mouseY>270 && mouseY<320 && radius<25 && mouseButton == LEFT) {
      radius+=0.1;
    }
  }
  if (mouseX>1090 && mouseX<1120 && mouseY>280 && mouseY<310 && radius<25 && mouseButton == LEFT) {
    radius+=0.05;
  }
  if (mouseX>1210 && mouseX<1260 && mouseY>270 && mouseY<320 && radius>1 && mouseButton == LEFT) {
    radius-=0.1;
  }
  if (mouseX>1160 && mouseX<1190 && mouseY>280 && mouseY<310 && radius>1 && mouseButton == LEFT) {
    radius-=0.05;
  }
}
//Change color of dot settings by clicking on icons
public void colorPalette() {
  if (mousePressed) {
    if (mouseX>1115 && mouseX<1165 && mouseY>75 && mouseY<125 && mouseButton == LEFT ) {
      x+=0.7;
    }
  }
  if (mousePressed) {
    if (mouseX>1200 && mouseX<1250 && mouseY>75 && mouseY<120 && mouseButton == LEFT ) {
      y+=0.7;
    }
  }
  if (mousePressed) {
    if (mouseX>1025 && mouseX<1075 && mouseY>68 && mouseY<128 && mouseButton == LEFT ) {
      z+=0.7;
    }
  }
  if (mousePressed) {
    if (mouseX>1100 && mouseX<1175 && mouseY>135 && mouseY<200 && mouseButton == LEFT) {
      x = 0;
      y = 0;
      z = 0;
    }
  }
}
//Dot in bottom right corner of screen to see what your current dot looks like
public void dotImage() {
  noStroke();
  fill(x, y, z, transparency);
  ellipse(1230, 640, radius, radius);
}
//Code used to save files to folder
void folderSelectedJPG(File selection) 
{
  if (selection == null)
  {
    return;
  } else
  {
    String dir2 = selection.getPath()+"\\";
    save(dir2 + "masterpiece("+num+").jpg");
    num++;
  }
}
void folderSelectedPNG(File selection) 
{
  if (selection == null)
  {
    return;
  } else
  {
    String dir2 = selection.getPath()+"\\";
    save(dir2 + "masterpiece("+num+").png");
    num++;
  }
}
