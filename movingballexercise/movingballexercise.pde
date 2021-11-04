/* ***********************************************************************
* Boris Wang
* Exercise 2 - Moving Ball
* B3
* October 17, 2020

* This program is my own work - Digital Signature (B.W)   */


float xspeed = 2;
float easing = 0.95;
float circleX;
boolean start = false;

void setup() {
  size(800, 400);
  circleX = width/2;
  ellipseMode(DIAMETER);
}

void draw() {
  background(0);
  fill(255);
  ellipse(circleX, height/2, 50, 50);
  if (start) { // True
    circleX = circleX + xspeed * easing;

    if (circleX > width-25) {
      xspeed = -xspeed * easing;
    }

    if (circleX < 25) {
      xspeed = 2 * easing;
    }
  }
}

void mousePressed() {
  if (start) { // If true, turn back false (make it stop)
    start = false;
  } 
  else { // If false, make it true (make it move)
    start = true;
  }
}
