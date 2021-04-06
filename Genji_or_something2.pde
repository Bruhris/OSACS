/* ***********************************************************************
* Boris Wang
* Exercise 4 - Robot 2: Variables
* B3
* September 23, 2020

* This program is my own work - Digital Signature (B.W)   */

PImage img;
void setup() {
img = loadImage("Hanamura_screenshot_13.png");
image(img,-700,-800);
size(1280, 720);
smooth();
ellipseMode(RADIUS);
int x = 15;
int y = 665;
int z = 540;
int b = 400;
int s = 5;
int q = 580;
int u = 310;
//Head
stroke(0);
strokeWeight(2);
fill(230,230,230);
square(z, 125, 125);
noStroke();
fill(0,255,0);
square(575, 185, x);
square(615, 185, x);
square(600, 200, x);
square(590, 200, x);
square(560, 185, x);
square(630, 185, x);
square(650, 170, x);
square(z, 170, x);
square(645, 170, x);
square(545, 170, x);
fill(0);
rect(z, 130, 125,25);
rect(575, 180, x, s);
rect(560, 180, x, s);
rect(560, 170, s, x);
rect(590, 180, s, 20);
rect(590, 195, 25, s);
rect(610, 180, s, x);
rect(610, 180, 35, s);
rect(640, 165, s, x);
rect(640, 165, 25, s);
rect(z, 165, 25, s);
rect(z, 185, 20, s);
rect(555, 185, s, x);
rect(555, b/2, 35, s);
rect(615, b/2, 30, s);
rect(615, b/2, s, x);
rect(585, b/2, s, x);
rect(585, 215, 35, s);
rect(645, 185, 20, s);
rect(645, 185, s, 20);
fill(233,233,233);
stroke(0);
strokeWeight(2);
arc(550, 125, 10, 20, radians(180), radians(270));
arc(655, 125, 10, 20, radians(270), radians(360));
noStroke();
fill(b/2,b/2,b/2);
square(542, 205, 18);
square(646, 205, 18);
square(629, 223, 18);
square(558, 223, 18);
fill(1,1,1);
triangle(y,130,665,155,730,120);
triangle(690,130, 800, 90, 860, 120);
triangle(705,125, 850, 140, 740, 160);
//Body
strokeWeight(2);
fill(230,230,230);
rect(z, 250, 125, 200);
fill(0,255,0);
rect(z,250,125,150);
fill(0);
ellipse(602, 293, 18,18);
fill(0,255,0);
ellipse(602, 293, 15,15);
fill(0,255,0);
strokeWeight(2);
stroke(0);
triangle(588,285, 615, 285, 602,308);
fill(125,125,125);
stroke(0);
quad(603, 250, 580, 275, z, 295, z, 250);
quad(603, 250, 625, 275, y, 295, y, 250);
quad(603, 340, 580, 310, z, 295, z, b);
quad(603, 340, y, b, y, 295, 625, 310);
fill(200,200,200);
quad(z, 250, q, 250, q, 275, z, 280);
quad(625, 250, y, 250, y, 280, 625, 275);
quad(q, u,z, 310,z, b, q, 361);
quad(625, u, y, u, y, b, 625, 361);
quad(q, 361,625, 361, y, b, z, b);
quad(q, 450, 625, 450, y,b, z, b);
fill(125,125,125);
triangle(z, b, z,450,580,450);
triangle(625,450, y,450, y,b);
fill(b/2,b/2,b/2);
triangle(q, 275, 625, 275,603, 250);
triangle(q, 275, 580, u,z, 295);
triangle(q, u,625, u, 603, 340);
triangle(625, 275, 625, u,665, 295); 
//Arms
noStroke();
fill(230,230,230);
strokeWeight(2);
stroke(0);
quad(665, 250,720, 225,798, 425,740, 450);
quad(480, 225, z, 250, 450, 450, 395, 425);
//Legs
quad(z, 450, 603, 450, 535, 625, 470 ,625);
quad(603, 450, y, 450, 725, 625, 665, 625);
//Sword1
stroke(0,255,123);
fill(0,255,0);
quad(75, 50, 105, 125, 355, 345, 365, 305);
stroke(255);
strokeWeight(2);
fill(0);
quad(320, 355, 380, 280, 390, 325, 366,355);
quad(366,355,390, 322, 475, 390, 450, 425);
//BroadSword
fill(0,255,0);
stroke(125,255,0);
strokeWeight(2);
quad(820,345,1080,125,1100,50,788,305);
fill(0);
stroke(255);
quad(835,355,780,280,770,325, 792,355); 
quad(770,325,792,355, 735, 400, 713, 370);
}
