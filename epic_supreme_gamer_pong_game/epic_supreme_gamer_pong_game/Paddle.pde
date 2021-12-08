class Paddle
{
  float paddleX;
  float paddleY = height/2;
  float paddleW = 25;
  float paddleH = 120;
  float ychange = 0;
  float r = 10;

  Paddle(boolean left) {
    if (left) {
      paddleX = paddleW + 30;
    } else {
      paddleX = width - paddleW - 30;
    }
  }
  //creates paddle
  void paddleCreate() {
    rectMode(CENTER);
    rect(paddleX, paddleY, paddleW, paddleH);
  }
  //allows paddle to move
  void movement() {
    paddleY += ychange;
    paddleY = constrain(paddleY, paddleH/2, height-paddleH/2);
  }
  void movementInc(float moves) {
    ychange = moves;
  }
  void changepaddleColor(){
    if (key == '8'){
      float c1 = random(255);
      float c2 = random(255);
      float c3 = random(255);
      fill(c1,c2,c3);
    }
  }
}
