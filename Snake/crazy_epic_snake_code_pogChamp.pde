/* ***********************************************************************
 * Boris Wang
 * Course Project - Snake
 * Block 3
 * January 15, 2021
 
 * This program is my own work - Boris Wang (B.W)   
 
 Instruction to Code:
 
 Interfaces:
 
 -Menu Page: Can pick three options, being play, help, and options
 -Play: Will bring you to level selector where you can pick the difficulty of the level of snake you will be playing (Higher score limit and faster snake)
 -Help: Will display instructions to game as well as controls
 -Options: Will have access to customization options 
 -Game Scene: When you select a level in the level selector, you will be put into a game of snake with the selected difficulty as well as any customization you made in the options screen
 -Win Scene: If you beat the level by eating a certain amount of food, you will have the win screen where you can either, retry the level, select a different level, go back to the main menu or quit the game
 -Lose Scene: If you die during the level, you will have the lose scene where it displays your score and you can either, retry the level, select a different level, go back to the main menu or quit the game
 
 Features:
 -Sound Effect when you die
 -Sound Effect when you get a point 
 -Back button to switch between some screens
 -Change Snake Color 
 -Change Food to different fruit
 -Change Background pattern
 -Pick what level you want 
 -Instruction Panel
 -Ability to retry a level, select a different level, go back to the main menu or quit the game
 -Mute the sound effects by clicking the right mouse button and unmute with the left mouse button in the options menu
 */

//Import libraries
import ddf.minim.*;

//Assign array lists
ArrayList<Integer> x = new ArrayList<Integer>();
ArrayList<Integer> y = new ArrayList<Integer>();

//int, float, array, String, boolean, PImage, PShape, PFont variable delcare 
int w = 30;
int h = 30;
int blocks = 20;
int dir = 2;
int dir2;
int c1 = 255;
int c2 = 255;
int c3 = 255;
int [] xdir={0, 0, 1, -1};
int [] ydir={1, -1, 0, 0};
int foodX = 15;
int foodY=15;
int limit;
int kick;
int size = 20;
int backC1 = 138;
int backC2 = 255;
int backC3 = 54;
int backC4 = 82;
int backC5 = 201;
int backC6 = 56;
int snakeC1 = 0;
int snakeC2 = 0;
int snakeC3 = 0;
float speed;
String screen = "main";
String level;
boolean lost = false;
boolean sound = true;
PImage backArrow;
PShape foodType;
PShape apple;
PShape banana;
PShape orange;
PShape cherry;
PFont font;
PFont font2;
PFont font3;
PFont font4;
PFont font5;
PFont font6;
PImage minus;
PImage plus;
PImage mute;
PImage unmute;
PImage vol;

//Sound effect declare 
AudioPlayer eat;
AudioPlayer hit;
Minim minim;

void setup() {
  size(600, 600);
  x.add(0);
  y.add(15);
  //Font creation
  font = createFont("commando.ttf", 48);
  font2 = createFont("American Captain.ttf", 48);
  font3 = createFont("ADAM.CG PRO.otf", 48);
  font4 = createFont("Toxico.otf", 48);
  font5 = createFont("LemonMilk.otf", 48);
  font6 = createFont("Peace Sans.otf", 48);

  //Shape creation
  apple = loadShape("apple-svgrepo-com.svg");
  banana = loadShape("banana-svgrepo-com.svg");
  cherry = loadShape("cherry-svgrepo-com.svg");
  orange = loadShape("orange-svgrepo-com.svg");

  //Image creation
  backArrow = loadImage("LidooqXeT.jpg");
  backArrow.resize(75, 50);
  minus = loadImage("kisspng-plus-and-minus-signs-plus-minus-sign-meno-symbol-s-dave-s-lounge-5b192f23787c48.1129353615283771234935.png");
  plus = loadImage("kisspng-plus-and-minus-signs-clip-art-5b1d241b912a93.5793820415286364435946.png");
  mute = loadImage("2c3ddf4bf13852db711dd1901fb517fa.png");
  unmute = loadImage("iconfinder_mute_298833.png");
  //Image resizing
  plus.resize(50, 50);
  minus.resize(25, 25);
  unmute.resize(68, 87);
  mute.resize(65, 56);

  textFont(font2);
  textAlign(CENTER);
  
  //Sound effect initialization
  minim = new Minim(this);
  hit = minim.loadFile("hitmarker_K7LsF3j.mp3");
  eat = minim.loadFile("Sound effect eat.mp3");
}

void draw() {
  textFont(font);
  if (screen == "gameScene") {
    //switch determines level that user picks 
    switch(level) {
    case "1":
      speed = 9;
      limit = 10;
      break;
    case "2":
      speed = 6;
      limit = 15;
      break;
    case "3":
      speed = 3;
      limit = 20;
      break;
    case "4":
      speed = 1;
      limit = 25;
      break;
    default:
      limit = 1;
      speed = 25;
    }
    for (int h = 0; h < width; h += size) {
      for (int v = 0; v < height; v += size) { 
        if ((h+v) % 8 ==0) {
          //chooses colors of checker rectangles
          noStroke();
          fill(backC1, backC2, backC3);
        } else { 
          noStroke();
          fill(backC4, backC5, backC6);
        } 
        //creates checker pattern with squares
        rect (h, v, size, size);
      }
    }
    //creates snake character
    for (int i = 0; i < x.size(); i++) {
      noStroke();
      fill(snakeC1, snakeC2, snakeC3);
      rect(x.get(i)*blocks, y.get(i)*blocks, blocks, blocks);
    }
    if (!lost) {
      //switch picks what food is used in the game 
      switch(kick) {
      case 1:
        shape(foodType, foodX*blocks, foodY*blocks, blocks, blocks);
        break;
      case 2:
        shape(foodType, foodX*blocks, foodY*blocks, blocks, blocks);
        break;
      case 3:
        shape(foodType, foodX*blocks, foodY*blocks, blocks, blocks);
        break;
      case 4: 
        shape(foodType, foodX*blocks, foodY*blocks, blocks, blocks);
        break;
      case 5:
        noStroke();
        fill(255);
        rect(foodX*blocks, foodY*blocks, blocks, blocks);
      default:
        noStroke();
        fill(255);
        rect(foodX*blocks, foodY*blocks, blocks, blocks);
      }
      textAlign(LEFT);
      textSize(25);
      fill(255);
      text("Score "+ x.size()+"                                               Score needed to win "+limit, 10, 10, width-20, 50);
      if (frameCount%speed==0) {
        //makes the tail longer
        x.add(0, x.get(0) + xdir[dir]);
        y.add(0, y.get(0) + ydir[dir]); 
        //if snake hits wall, loses game 
        if (x.get(0) <0 || y.get(0) < 0 || x.get(0) >= w || y.get(0) >=h) {
          hit.play();
          hit.rewind();
          lost = true;
        }
        for (int i = 1; i<x.size(); i++) {
          if (x.get(0) == x.get(i) && y.get(0) == y.get(i)) {
            // if snake hits own tail, loses game
            hit.play();
            hit.rewind();
            lost = true;
          }
        }
        if (x.get(0)==foodX && y.get(0) == foodY) {
          //spawns food and plays eat noise
          eat.play();
          eat.rewind();
          foodX = (int)random(0, w);
          foodY = (int)random(0, h);
        } else {
          //makes it so the tail moves as the snake moves
          x.remove(x.size()-1);
          y.remove(y.size()-1);
        }
      } else if (x.size() == limit) {
        //when reaches certain size, will show win scene
        screen = "win";
      }
    } else {
      //when loses, shows lose scene
      screen = "lose";
    }
  }
  //main menu scene
  if (screen == "main") {
    textAlign(CENTER);
    textFont(font2);
    background(23, 125, 176);
    fill(#304DFC);
    rect(236, 240, 136, 50);
    rect(236, 310, 136, 50);
    rect(236, 380, 136, 50);
    fill(255);
    textSize(96);
    stroke(0);
    fill(6, 191, 44);
    text("Snake", 300, 125);
    textSize(32);
    text("By: Boris Wang", 300, 175);
    fill(255);
    text("Play", 300, 275);
    text("Help", 305, 345);
    text("Options", 305, 415);
  }
  //lose scene
  if (screen == "lose") {
    background(1, 8, 43);
    fill(200, 200, 0); 
    textSize(96); 
    textAlign(CENTER); 
    text("GAME OVER ", 304, 90);
    textSize(32);
    text("Your score was " + x.size(), 304, 155);
    textSize(24);
    text("Retry", 304, 230);
    text("Play\ndifferent\nlevel", 304, 295);
    text("Main Menu", 304, 423);
    text("Close Game", 304, 493);
  }
  //level selector scene
  if (screen == "levelSelector") {
    textAlign(CENTER);
    stroke(0);
    background(177, 29, 194);
    textFont(font2);
    fill(0, 0, 0, 0);
    rect(35, 180, 175, 175);
    rect(35, 375, 175, 175);
    rect(385, 180, 175, 175);
    rect(385, 375, 175, 175);
    textSize(108);
    fill(0);
    text("Select A Level:", 300, 125);
    textSize(56);
    fill(29, 219, 44);
    text("Easy", 120, 285);
    fill(245, 194, 10);
    text("Medium", 473, 285);
    fill(255, 80, 5);
    text("Hard", 120, 485);
    fill(255, 5, 5);
    textSize(42);
    text("Impossible", 473, 475);
  }
  //win scene
  if (screen == "win") {
    stroke(0);
    background(255, 119, 0);
    fill(255, 119, 0);
    fill(255);
    textFont(font4);
    textAlign(CENTER);
    textSize(96);
    text("You Won!", 300, 125);
    textSize(22);
    text("Retry", 304, 230);
    text("Play\ndifferent\nlevel", 304, 295);
    text("Main Menu", 304, 423);
    text("Close Game", 304, 493);
  }
  // help scene
  if (screen == "help") {
    background(5, 81, 153);
    rect(497, 490, 80, 80);
    textAlign(LEFT);
    textFont(font6);
    textSize(42);
    text("How to Play Snake:", 10, 50);
    textSize(22);
    text("As the player, you control a snake that moves\naround on the game plane. Your goal is move\nalong the game plane and collect as many\nfruits as you can and increaseyour score\nin doing so. Fruits will spawn at random\nlocation on the map and as you eat fruits,\nyour tail length will increase. You can lose\nthe game by crashing into the borders of\nthe plane or if you hit your own tail if it is\nlong enough.", 15, 90);
    textSize(42);
    text("Controls:", 10, 435);
    textSize(26);
    text("Use W, A, S, D or UP, DOWN,\nLEFT, RIGHT arrow keys to\nmove your snake.", 15, 480);
    image(backArrow, 500, 505);
  }
  //options scene
  if (screen == "options") {
    background(245, 66, 108);
    fill(255);
    stroke(0);
    rect(497, 490, 80, 80);
    fill(255, 255, 255, 0);
    stroke(255);
    rect(225, 185, 155, 60);
    fill(255);
    textFont(font3);
    textAlign(CENTER);
    textSize(42);
    text("Food", 300, 55);
    text("Background", 300, 300);
    text("Snake Color", 300, 460);
    fill(199, 23, 0);
    text("R", 180, 580);
    fill(0, 255, 0);
    text("G", 300, 580);
    fill(0, 0, 255);
    text("B", 420, 580);
    noStroke();
    fill(255, 89, 64);
    rect(75, 330, 37.5, 37.5);
    rect(112.5, 367.5, 37.5, 37.5);
    fill(191,59,40);
    rect(112.5, 330, 37.5, 37.5);
    rect(75, 367.5, 37.5, 37.5);
    fill(245, 78, 228);
    rect(200, 330, 37.5, 37.5);
    rect(237.5, 367.5, 37.5, 37.5);
    fill(201, 48, 186);
    rect(237.5, 330, 37.5, 37.5);
    rect(200, 367.5, 37.5, 37.5);
    fill(56, 169, 255);
    rect(325, 330, 37.5, 37.5);
    rect(362.5, 367.5, 37.5, 37.5);
    fill(35, 125, 194);
    rect(325, 367.5, 37.5, 37.5);
    rect(362.5, 330, 37.5, 37.5);
    fill(138, 255, 54);
    rect(450, 330, 37.5, 37.5);
    rect(487.5, 367.5, 37.5, 37.5);
    fill(82, 201, 56);
    rect(487.5, 330, 37.5, 37.5);
    rect(450, 367.5, 37.5, 37.5);
    fill(snakeC1, snakeC2, snakeC3);
    stroke(0);
    rect(280, 480, 40, 40);
    image(plus, 120, 540);
    image(plus, 240, 540);
    image(plus, 365, 540);
    image(minus, 200, 555);
    image(minus, 320, 555);
    image(minus, 440, 555);
    textSize(32);
    fill(255);
    text("Default", 302, 230);
    image(backArrow, 500, 505);
    shape(apple, 75, 80, 75, 75);
    shape(banana, 200, 80, 75, 75);
    shape(cherry, 325, 80, 75, 75);
    shape(orange, 450, 80, 75, 75);
  }
  //will change color of snake when pressing the plus and minus signs for the rgb color selection
  if (screen == "options") {
    if (mousePressed == true && mouseX >= 120 && mouseY >=540 && mouseX<= 170 && mouseY<=590 && snakeC1<=255) {
      snakeC1++;
    }
    if (mousePressed == true && mouseX >= 200 && mouseY >=555 && mouseX<= 225 && mouseY<=580 && snakeC1>=0) {
      snakeC1--;
    }
    if (mousePressed == true && mouseX >= 240 && mouseY >=540 && mouseX<= 290 && mouseY<=590 && snakeC1<=255) {
      snakeC2++;
    }
    if (mousePressed == true && mouseX >= 320 && mouseY >=555 && mouseX<= 345 && mouseY<=580 && snakeC1>=0) {
      snakeC2--;
    }
    if (mousePressed == true && mouseX >= 365 && mouseY >=540 && mouseX<= 415 && mouseY<=590 && snakeC1<=255) {
      snakeC3++;
    }
    if (mousePressed == true && mouseX >= 440 && mouseY >=555 && mouseX<= 465 && mouseY<=580 && snakeC1>=0) {
      snakeC3--;
    }
    //will mute and unmute the sound effects if sound is true or false
    if (sound == true) {
      vol = unmute;
      image(vol, 25, 480);
      eat.setGain(-17);
      hit.setGain(-17);
    } else if (sound == false) {
      vol = mute;
      image(vol, 25, 500);
      eat.setGain(-100);
      hit.setGain(-100);
    }
  }
}
//makes it so pressing wasd or the arrow keys moves the snake 
void keyPressed() {
  if (xdir[dir] != 0 && ydir[dir] != -1) {
    if (keyCode == DOWN||key == 's') {
      dir2 = 0;
    }
  }
  if (xdir[dir] != 0 && ydir[dir] != 1) {
    if (keyCode == UP||key == 'w') {
      dir2 = 1;
    }
  }
  if (xdir[dir] != -1 && ydir[dir] != 0) {
    if (keyCode == RIGHT||key == 'd') {
      dir2 = 2;
    }
  }
  if (xdir[dir] != 1 && ydir[dir] != 0) {
    if (keyCode == LEFT||key == 'a') {
      dir2 = 3;
    }
  }
  if (dir2 != -1) {
    dir = dir2;
  }
}
void mousePressed() {
  //changes the scene when pressing the buttons on the menu
  if (screen == "main") {
    if (mouseX>=236 && mouseY >=240 && mouseX <=372 && mouseY <=290) {
      screen = "levelSelector";
    }
    if (mouseX>=236 && mouseY >= 310 && mouseX <= 372 && mouseY <=360) {
      screen = "help";
    }
    if (mouseX>= 236 && mouseY >=380 && mouseX <= 372 && mouseY <=430) {
      screen = "options";
    }
  }
  //makes the back button work
  if (screen == "options" || screen == "help") {
    if (mouseX >= 485 && mouseY >= 480 && mouseX <=585 && mouseY <=580) {
      screen = "main";
    }
  }
  //makes it so that when you click the options on the win scene, they work as intended
  if (screen == "win") {
    if (mouseX >= 236 && mouseY >= 200 && mouseX <= 372 && mouseY <=250) {
      foodX = (int)random(0, w);
      foodY = (int)random(0, h);
      x.clear(); 
      y.clear(); 
      x.add(0);  
      y.add(15);
      dir = 2;
      lost = false;
      screen = "gameScene";
    }
    if (mouseX >= 236 && mouseY >= 270 && mouseX <= 372 && mouseY <= 331) {
      x.clear(); 
      y.clear(); 
      x.add(0);  
      y.add(15);
      dir = 2;
      screen = "levelSelector";
    }
    if (mouseX >= 236 && mouseY >= 390  && mouseX <=372 && mouseY <=440) {
      x.clear(); 
      y.clear(); 
      x.add(0);  
      y.add(15);
      dir = 2;
      screen = "main";
    }
    if (mouseX >=  236 && mouseY >= 460 && mouseX <=372 && mouseY <=510) {
      exit();
    }
  }
  //changes the level and makes the switch work
  if (screen == "levelSelector") {
    if (mouseX >=35 && mouseY >= 180 && mouseX <= 210 && mouseY <= 355) {
      level = "1";    
      screen = "gameScene";
      lost = false;
    }
    if (mouseX >= 385 && mouseY >= 180 && mouseX <= 560 && mouseY <= 355) {
      level = "2";     
      screen = "gameScene";
      lost = false;
    }
    if (mouseX >= 35 && mouseY >= 375 && mouseX <= 210 && mouseY <= 550) {
      level = "3";
      screen = "gameScene";
      lost = false;
    }
    if (mouseX >= 385 && mouseY >= 375 && mouseX <= 560 && mouseY <=550) {
      level = "4";
      screen = "gameScene";
      lost = false;
    }
  }
  //allows the options on the lose scene to work
  if (screen == "lose") {
    if (mouseX >= 236 && mouseY >= 200 && mouseX <= 372 && mouseY <=250) {
      foodX = (int)random(0, w);
      foodY = (int)random(0, h);
      x.clear(); 
      y.clear(); 
      x.add(0);  
      y.add(15);
      dir = 2;
      lost = false;
      screen = "gameScene";
    }
    if (mouseX >= 236 && mouseY >= 270 && mouseX <= 372 && mouseY <= 331) {
      x.clear(); 
      y.clear(); 
      x.add(0);  
      y.add(15);
      dir = 2;
      screen = "levelSelector";
    }
    if (mouseX >= 236 && mouseY >= 390  && mouseX <=372 && mouseY <=440) {
      x.clear(); 
      y.clear(); 
      x.add(0);  
      y.add(15);
      dir = 2;
      screen = "main";
    }
    if (mouseX >=  236 && mouseY >= 460 && mouseX <=372 && mouseY <=510) {
      exit();
    }
  }
  //makes the customization in the options scene work
  if (screen == "options") {
    if (mouseX >= 75 && mouseY >= 80 && mouseX<= 150 && mouseY <= 155) {
      foodType = apple;
      kick = 1;
    }
    if (mouseX >= 200 && mouseY >= 80 && mouseX<= 275 && mouseY <= 155) {
      foodType = banana;
      kick = 2;
    }
    if (mouseX >= 325 && mouseY >= 80 && mouseX<= 400 && mouseY <= 155) {
      foodType = cherry;
      kick = 3;
    }
    if (mouseX >= 450 && mouseY >= 80 && mouseX<= 525 && mouseY <= 155) {
      foodType = orange;
      kick = 4;
    }
    if (mouseX >= 225 && mouseY >= 185 && mouseX<= 380 && mouseY <= 245) {
      kick = 5;
    }
    if (mouseX >= 75 && mouseY >= 330 && mouseX<= 150 && mouseY <= 405) {
      backC1 = 255;
      backC2 = 89;
      backC3 = 64;
      backC4 = 191;
      backC5 = 59;
      backC6 = 40;
    }
    if (mouseX >= 200 && mouseY >= 330 && mouseX<= 275 && mouseY <= 405) {
      backC1 = 245;
      backC2 = 78;
      backC3 = 228;
      backC4 = 201;
      backC5 = 48;
      backC6 = 186;
    }
    if (mouseX >= 325 && mouseY >= 330 && mouseX<= 400 && mouseY <= 405) {
      backC1 = 56;
      backC2 = 169;
      backC3 = 255;
      backC4 = 35;
      backC5 = 125;
      backC6 = 194;
    }
    if (mouseX >= 450 && mouseY >= 330 && mouseX<= 525 && mouseY <= 405) {
      backC1 = 138;
      backC2 = 255;
      backC3 = 54;
      backC4 = 82;
      backC5 = 201;
      backC6 = 56;
    }
    if (mouseButton == LEFT && mouseX >= 25 && mouseY >= 500 && mouseX<= 90 && mouseY <= 560 && vol != unmute) {
      sound = true;
    }
    if (mouseButton == RIGHT && mouseX >= 25 && mouseY >= 500 && mouseX<= 90 && mouseY <= 560 && vol == unmute) {
      sound = false;
    }
  }
}
