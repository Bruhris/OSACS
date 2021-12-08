/* ***********************************************************************
 * Boris Wang
 * Assignment 2 - Pong
 * Block 3
 * December 9, 2020
 
 * This program is my own work - B.W   */

/* 
-Click the ? box to see controls and instructions on how to play
-Click either the "Player vs Player" box to play against a friend or "Practice" to play by yourself
-Click the volume box to either mute or unmute sounds
-Click the exit box when in game to leave the game
-Can change paddle color by pressing '8' and change ball color '1'
-I used this forum to understand how to use the map function: https://forum.processing.org/two/discussion/22471/how-does-mapping-function-work
 */


//variable and class assignment
import ddf.minim.*;
Minim minim;
AudioPlayer point;
PFont font;
int leftScore;
int rightScore;
boolean box1 = false;
boolean box2 = false;
boolean back = false;
boolean check = true;
boolean help = false;
boolean sound = true;
PImage questionmark;
PImage unmute;
PImage mute;
ball pongBall;
Paddle leftP;
Paddle rightP;
practicePaddle g;

void setup() {
  //classes, audio and images
  g = new practicePaddle();
  pongBall = new ball();
  leftP = new Paddle(true);
  rightP = new Paddle(false);
  minim = new Minim(this);
  point = minim.loadFile("ding-sound-effect_2.mp3");
  questionmark = loadImage("pngfind.com-white-question-mark-png-24050.png");
  unmute = loadImage("2c3ddf4bf13852db711dd1901fb517fa.png");
  mute = loadImage("iconfinder_mute_298833.png");
  rectMode(CENTER);
  imageMode(CENTER);
  size(1280, 720);
  frameRate(90);
  font = loadFont("SegoeUI-Bold-48.vlw");
  textFont(font);
}

void draw() {
  help();
  soundmute();
  //main page
  background(0);
  textSize(60);
  text("Pong", 570, 150);
  textSize(36);
  text("By: Boris Wang", 520, 250);
  rect(width/2, 335, 250, 75);
  fill(0);
  textSize(30);
  text("Player vs Player", 532, 350);
  fill(255);
  rect(width/2, 460, 250, 75);
  fill(0);
  textSize(36);
  text("Practice", 571, 475);
  fill(255);
  questionmark.resize(30, 55);
  unmute.resize(49, 40);
  mute.resize(50, 60);
  rect(480, 45, 70, 70);
  rect(800, 45, 70, 70);
  image(questionmark, 800, 45);
  //changes sound when box is clicked
  if (sound) {
    image(mute, 480, 45);
    point.setGain(-21);
  } else {
    image(unmute, 480, 45);
    point.setGain(-100);
  }
  //checks which box is clicked 
  if (check) {
    checkBox();
    if (box1 == true || box2 == true) {
      check = false;
    }
  }
  //plays multiplayer
  if (box1) {
    playerVsPlayer();
    if (back) {
      exit();
    }
  }
  //players single player
  if (box2) {
    practice();
    if (back) {
      exit();
    }
  }
  //instructions page
  if (help) {
    rect(width/2, height/2, 600, 600);
    fill(0);
    text("Instructions to Pong", 465, 100);
    textSize(30);
    text("How to play:\n", 350, 150);
    textSize(24);
    text("A ball will appear and go towards one of the two\nplayer sides. Your goal is to prevent the ball from\nhitting your side and get the ball to hit the other\nplayers side. Use your paddles to defend your side\nand hit the ball to the other players side. The\npaddles can only move up and down and are\ncontrolled using keys. Remember to try your best\nand GLHF!", 350, 190);
    textSize(30);
    text("Controls:", 350, 450);
    textSize(25);
    text("P1 (LEFT SIDE):   W = UP\n                            S = DOWN", 350, 510);
    text("P2 (RIGHT SIDE):  UP ARROW KEY = UP\n                             DOWN ARROW KEY = DOWN", 350, 600);
  }
}
//function to play playervsplayer
void playerVsPlayer() {
  background(0);
  rect(width/2, 50, 150, 50);
  fill(0);
  text("Exit", 605, 62);
  fill(255);
  text(leftScore, 200, 100);
  text(rightScore, 1000, 100);
  rect(480, 45, 70, 70);
  rect(800, 45, 70, 70);
  image(questionmark, 800, 45);

  leftP.changepaddleColor();
  leftP.paddleCreate();
  rightP.changepaddleColor();
  rightP.paddleCreate();
  pongBall.paddleTouchRight(rightP);
  pongBall.paddleTouchLeft(leftP);

  if (keyPressed == true && key == 'w') {
    leftP.movementInc(-6);
    leftP.movement();
  }
  if (keyPressed == true && key == 's') {
    leftP.movementInc(6);
    leftP.movement();
  }
  if (keyPressed == true && keyCode == UP) {
    rightP.movementInc(-6);
    rightP.movement();
  }
  if (keyPressed == true && keyCode == DOWN) {
    rightP.movementInc(6);
    rightP.movement();
  }
  pongBall.changeballColor();
  pongBall.pongArea();
  pongBall.ballCreate();
  pongBall.ballMove();
  pongBall.points();
  if (mouseX >= 565 && mouseX <= 715 && mouseY >= 50 && mouseY <= 100 && mousePressed == true) {
    back = true;
  }
  if (sound) {
    image(mute, 480, 45);
    point.setGain(-21);
  } else {
    image(unmute, 480, 45);
    point.setGain(-100);
  }
}
//functions to play practice
void practice() {
  background(0);
  rect(width/2, 50, 150, 50);
  fill(0);
  text("Exit", 605, 62);
  fill(255);
  rect(480, 45, 70, 70);
  rect(800, 45, 70, 70);
  image(questionmark, 800, 45);
  leftP.changepaddleColor();
  leftP.paddleCreate();
  g.changepaddleColor();
  g.paddleCreate();
  pongBall.practice(g);
  pongBall.paddleTouchLeft(leftP);

  if (keyPressed == true && key == 'w') {
    leftP.movementInc(-6);
    leftP.movement();
  }
  if (keyPressed == true && key == 's') {
    leftP.movementInc(6);
    leftP.movement();
  }
  pongBall.changeballColor();
  pongBall.points();
  pongBall.pongArea();
  pongBall.ballCreate();
  pongBall.ballMove();

  if (mouseX >= 565 && mouseX <= 715 && mouseY >= 50 && mouseY <= 100 && mousePressed == true) {
    back = true;
  }
  if (sound) {
    image(mute, 480, 45);
    point.setGain(-21);
  } else {
    image(unmute, 480, 45);
    point.setGain(-100);
  }
}
//function to activate player box or practice box
void checkBox() {
  if (mouseX >= 520 && mouseX <=770 && mouseY >= 300 && mouseY <=375 && mousePressed == true) {
    box1 = true;
  }
  if (mouseX >= 520 && mouseX <=770 && mouseY >= 425 && mouseY <= 500 && mousePressed == true) {
    box2 = true;
  }
}
//open the instruction page and close it using right mouse click
void help() {
  if (mouseButton == LEFT && mouseX >= 765 && mouseX <=835 && mouseY >= 15 && mouseY <=80) {
    help = true;
  } else if (mouseButton == RIGHT && mouseX >= 765 && mouseX <=835 && mouseY >= 15 && mouseY <=80) {
    help = false;
  }
}
//mute using right click and unmute using left click
void soundmute() {
  if (mouseButton == LEFT && mouseX >= 445 && mouseX <= 515 && mouseY >= 15 && mouseY <=80) {
    sound = true;
  } else if (mouseButton == RIGHT && mouseX >= 445 && mouseX <= 515 && mouseY >= 15 && mouseY <=80) {
    sound = false;
  }
}
