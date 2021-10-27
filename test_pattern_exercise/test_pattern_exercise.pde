/* ***********************************************************************
* Boris Wang
* Exercise 4 - Test Pattern
* Block 3
* Completed November 24, 2020

* This program is my own work - B.W   */

void setup() {
  size(400, 300);
  strokeWeight(2);
  stroke(255);
  for (int y=0; y<300; y+=20) {
    for (int x=0; x<400; x+=20) {
      fill(int(random(255)), int(random(255)), int(random(255)));
      rect(x, y, 20, 20);
    }
  }
}
  
