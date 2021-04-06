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
  if (start) {
    circleX = circleX + xspeed * easing;

    if (circleX > width-25) {
      xspeed = -xspeed * easing;
    }

    if (circleX < 0+25) {
      xspeed = 2 * easing;
    }
  }
}

void mousePressed() {
  if (start) {
    start = false;
  } else {
    start = true;
  }
}
