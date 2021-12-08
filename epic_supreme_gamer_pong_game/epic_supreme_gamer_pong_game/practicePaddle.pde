class practicePaddle
{
  float paddleX = width-25;
  float paddleY = height/2;
  float paddleW = 50;
  float paddleH = 525;
//creates practice paddle
  void paddleCreate() {
    rectMode(CENTER);
    rect(paddleX, paddleY, paddleW, paddleH);
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
