/* ***********************************************************************
 * Boris
 * Assignment 1 - Snowman
 * B3
 * October 14, 2020
 
 * This program is my own work - Digital Signature (BW)   */

//Variable Assignment
float a = 430;
float b = 350;
float c = 405;
float d = 354;
float e = 430;
float f = 330;
float g = 120;
float h = 330;
float i = 150;
float j = 353;
float x = 80;
float y = 325;
int radius = 40;
float ypos = -radius;
float speed = 3;
PImage img2;
PImage img3;
PImage img4;
PImage img5;
PImage img6;
PImage img7;
PImage img8;
PImage img9;
PImage img10;
PImage img11;
PImage img12;
PImage img0;
PFont font;
void setup() {
  //Setup
  size(1280, 720);
  frameRate(120);
  //Images
  img2 = loadImage("Daco_4563460.png");
  img3 = loadImage("pngfind.com-dbz-aura-png-1583674.png");
  img4 = loadImage("367252.jpg");
  img5 = loadImage("Snowy_Ground_PNG_Clipart_Image-505742315.png");
  img6 = loadImage("367288.jpg");
  img7 = loadImage("christmas-ornaments-pictures-46347.png");
  img8 = loadImage("christmas-ornaments-pictures-46356.png");
  img9 = loadImage("christmas-ornaments-pictures-46340.png");
  img10 = loadImage("Christmas-Ornament-Ring-PNG.png");
  img11 = loadImage("Christmas-Ornament-Sweet-Green-Ice-Pattern-PNG.png");
  img12 = loadImage("PinClipart.com_bethlehem-star-clipart_661010.png");
  img0 = loadImage("christmas-ornaments-pictures-46341.png");
  font = loadFont("SegoeScript-Bold-48.vlw");
  textFont(font);
  ellipseMode(RADIUS);
}
void draw() {
  backgroundChange();
  //Floor Snow
  noStroke();
  img5.resize(1280, 1200);
  image(img5, 0, 260);
  //Upper-Body + Buttons + Aura
  img3.resize(350, 550);
  image(img3, 78, 80);
  stroke(0);
  strokeWeight(6);
  fill(255);
  arc(250, 382, 75, 80, radians(-220), radians(40), OPEN);
  fill(0);
  noStroke();
  circle(250, 350, 6);
  circle(250, 380, 6);
  circle(250, 410, 6);
  //Head + Eyes + Mouth + Carrot
  stroke(0);
  strokeWeight(6);
  fill(255);
  arc(250, 282, 50, 50, radians(-220), radians(40), OPEN);
  noStroke();
  fill(0);
  circle(250, 262, 5);
  circle(270, 262, 5);
  fill(#FF7205);
  triangle(265, 275, 315, 286, 265, 290);
  fill(0);
  circle(240, 292, 2.5);
  circle(248, 299, 2.5);
  circle(260, 302, 2.5);
  circle(280, 292, 2.5);
  circle(272, 299, 2.5);
  //LowerBody + Buttons
  stroke(0);
  strokeWeight(6);
  fill(255);
  arc(250, 495, 90, 82, radians(-50), radians(230), OPEN);
  noStroke();
  fill(0);
  circle(250, 470, 6);
  circle(250, 500, 6);
  circle(250, 530, 6);
  //Scarf
  noStroke();
  fill(200, 130, 200);
  quad(205, 312, 296, 312, 296, 340, 180, 340);
  arc(296, 326, 14, 14, radians(-90), radians(90), OPEN);
  quad(205, 312, 180, 320, 150, 420, 175, 425);
  //Hair
  img2.resize(140, 150);
  image(img2, 190, 125); 
  //Christmas Tree
  fill(#4B3100);
  rect(813, 490, 75, 125);
  fill(#1FAF19);
  triangle(710, 490, 990, 490, 850, 340);
  triangle(725, 400, 975, 400, 850, 260);
  triangle(750, 310, 950, 310, 850, 170);
  triangle(775, 220, 925, 220, 850, 80);
  //Ornaments
  img7.resize(20, 37);
  img8.resize(20, 37);
  img9.resize(20, 37);
  img10.resize(35, 35);
  img11.resize(25, 28);
  img12.resize(100, 100);
  img0.resize(20, 37);
  image(img12, 800, 35);
  image(img7, 850, 156);
  image(img8, 800, 175);
  image(img9, 825, 125);
  image(img10, 880, 170);
  image(img11, 870, 230);
  image(img0, 830, 200);
  image(img7, 790, 240);
  image(img8, 840, 250);
  image(img9, 810, 280);
  image(img0, 880, 270);
  image(img11, 805, 335);
  image(img7, 850, 300);
  image(img8, 760, 360);
  image(img9, 840, 365);
  image(img0, 900, 350);
  image(img7, 800, 400);
  image(img11, 830, 440);
  image(img8, 880, 415);
  image(img0, 760, 440);
  image(img10, 910, 445);
  if (mousePressed) {
    if (mouseButton == RIGHT) {
      textSize(48);
      text("Merry Christmas", 340, 125);
    }
  }
  moveArms();
  if (keyPressed) {
    if ( key == 's'||key == 'S') {
      for(int i =0; i<10; i++){
        blizzard();
      }
    }
  }
}
void moveArms() { //Moves the stick arms
  stroke(#674300);
  strokeWeight(6);
  line(190, 380, x, y);
  line(310, 380, a, b);
  line(c, d, e, f);
  line(g, h, i, j);
  if (mouseButton != LEFT) {
    if (y==325)
      x++;
    if (y==300)
      x--;
    if (x==80)
      y++;
    if (x ==81)
      y--;
    if (b==350)
      a++;
    if (b==325)
      a--;
    if (a==430)
      b++;
    if (a==431)
      b--;
    if (d==354)
      c++;
    if (d==329)
      c--;
    if (c==405)
      d++;
    if (c==406)
      d--;
    if (f==330)
      e++;
    if (f==305)
      e--;
    if (e==430)
      f++;
    if (e==431)
      f--;
    if (h==330)
      g++;
    if (h==305)
      g--;
    if (g==120)
      h++;
    if (g==121)
      h--;
  }
}
void snowing() { 
  //Created Snowflakes
  if (keyPressed) {
    if ((key == 'S')||(key == 's')) {
      if (ypos > height+radius) {
        ypos = -radius;
      }
    }
  }
  noStroke();
  fill(255); 
  ypos += speed; 
  ellipse(random(0, 1281), ypos, 7, 7);
}
void backgroundChange() {
  img4.resize(1280, 720);
  image(img4, 0, 0);
  if (keyPressed) {
    if ((key == 'C')||(key == 'c')) {
      image(img6, 0, 0);
    }
  }
}
void blizzard() {//Repeats snow command to makes lots of snowflakes fall when command called
  for(int k = 0; k<20; k++){
    snowing();
  }
}
