class ball
{
  float ballX = width/2;
  float ballY = height/2;
  float xspeed = 4;
  float yspeed = 2;
  float r = 15;


  ball() {
    float direction = random(-PI/4, PI/4);
    xspeed = 5 * cos(direction);
    yspeed = 5 * sin(direction);
  }
//how the ball will interactive when it hits the left paddle
  void paddleTouchLeft(Paddle p) {
    if (ballY < p.paddleY + p.paddleH/2 && ballY > p.paddleY-p.paddleH/2 && ballX - r < p.paddleX + p.paddleW/2) {
      if (ballX > p.paddleX) {
        xspeed = -xspeed;
        yspeed = map(ballY - p.paddleY, -p.paddleH/2, p.paddleH/2, -7, 7);
      }
    }
  }
  //how the ball will intereact when it hits the right paddle 
  void paddleTouchRight(Paddle p) {
    if (ballY < p.paddleY + p.paddleH/2 && ballY > p.paddleY-p.paddleH/2 && ballX + r > p.paddleX - p.paddleW/2) {
      if (ballX < p.paddleX) {
        xspeed = -xspeed;
        yspeed = map(ballY - p.paddleY, -p.paddleH/2, p.paddleH/2, -7, 7);
      }
    }
  } 
  //how the ball will intereact when it hits the practice paddle 
  void practice(practicePaddle p) {
    if (ballY < p.paddleY + p.paddleH/2 && ballY > p.paddleY-p.paddleH/2 && ballX + r > p.paddleX - p.paddleW/2) {
      if (ballX < p.paddleX) {
        xspeed = -xspeed;
        yspeed = map(ballY - p.paddleY, -p.paddleH/2, p.paddleH/2, -7, 7);
      }
    }
  } 
  //ball creation
  void ballCreate() {
    circle(ballX, ballY, r*2);
  }
  //how the ball will move when created 
  void ballMove() {
    ballX = ballX + xspeed;
    ballY = ballY + yspeed;
  }
  //when ball hits the bottom of the window
  void pongArea() {
    if (ballY-r < 0|| ballY+r > height) {
      yspeed *= -1;
    }
  }
  //what happens when the ball hits one of the sides of the window
  void points() {
    if (ballX+r > width) {
      rightScore++;
      point.setGain(-21);
      point.rewind();
      point.play();
      ballRestart();
    }
    if (ballX-r < 0) {
      leftScore++;
      ballRestart();
      point.setGain(-21);
      point.rewind();
      point.play();
    }
  }
  //resets the ball when side is hit in the middle
  void ballRestart() {
    ballX = width/2;
    ballY= height/2;
    float direction = random(-PI/4, PI/4);
    xspeed = 5 * cos(direction);
    yspeed = 5 * sin(direction);

    if (random(1) < 0.5 ) {
      xspeed *= -1;
    }
  }
  //changing the ball speed using '1' and '8'
  void changeballColor(){
    if (key == '1'){
      float c1 = random(255);
      float c2 = random(255);
      float c3 = random(255);
      fill(c1,c2,c3);
    }
  }
}
