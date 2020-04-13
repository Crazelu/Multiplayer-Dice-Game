import 'dart:io';
import 'dart:math';

void main(){
 Cradice cradice = new Cradice();
  cradice.start();
}

class Cradice{

  void start(){
    try{
      print("Enter number of players:");
      var players = int.parse(stdin.readLineSync());
      
      while (players < 2){
      print('Minimum of two players allowed');
      players = int.parse(stdin.readLineSync());
    }//While loop

    var namelist = [];

    for(int i=0; i<players; i++){
      print("Enter player ${i+1}'s name:");
      var name = stdin.readLineSync();

      if (name.isNotEmpty){
        namelist.add(name);
      }

      bool empty = name.isEmpty;

      while (empty){
        print('Enter a valid name.');
        var name = stdin.readLineSync();
        if (name.isEmpty){
          continue;
        }
        else{
          namelist.add(name);
          break;
        }
      }
      
    }

    Cradice cradice =  new Cradice();
    cradice.play(players, 3, namelist);

    }
    catch (FormatException){
      print('Invalid input');
      Cradice cradice = new Cradice();
      cradice.start();
    }
    
  }//start method

  void play(int players, int rounds, List namelist){
    //Initialize two lists to hold players' scores and names
    var scorelist = [];

    for (int i=0; i<players; i++){
      scorelist.add(0);
    }//for loop

    int round = 1;
    
    while (round <= rounds){

    if (scorelist.every((score) => score == null)){
      break;
    }

      print('Round $round!\n');
      for (int i=0; i<players; i++){
        if(scorelist[i] != null){
          print("${namelist[i]}, it's your turn to roll the dice");
          print('Do you want to roll the dice? [Y/N]');
          var choice = stdin.readLineSync();

          if (choice == 'y' || choice == 'Y'){
            var score = [];
            score.add(Random().nextInt(7));
            score.add(Random().nextInt(7));
            scorelist[i] += score[0] + score[1];
            print('${namelist[i]} rolled and got [${score[0]}, ${score[1]}]\n');
          }//if condition
          
          else{
            print('${namelist[i]} left the game.\n');
            scorelist[i] = null;

          }//else condition
        }//if condition
      }//for loop

      round++;
    }//while loop

    print('\n############### RESULT ###############\n');

    if (scorelist.every((score) => score == null)){
      print('No winner!');
      Cradice cradice = new Cradice();
      cradice.playAgain();
    }
    else{

      int winner = 0; 
      int highscore = 0;
      for (int i=0; i<players; i++){
          if(scorelist[i] != null){
            print("${namelist[i]} has a total score of ${scorelist[i]}.");
          }
          if(scorelist[i] != null){
            if(scorelist[i] > highscore){
              winner = i;
              highscore = scorelist[i];
          }
        }
    }//for loop

    Cradice cradice =  new Cradice();
    if(cradice.count(scorelist, highscore) > 1 && cradice.count(scorelist, highscore) == cradice.withoutNullLength(scorelist)){
      print("\nIt's a tie!\nTie Breaker!\n");
      cradice.play(cradice.withoutNullLength(scorelist), 2, namelist);
    }
    else{
      print("\n${namelist[winner]} wins with $highscore points.");
      cradice.playAgain();
    }
    

    }
    
  }//play method

  int count(List scorelist, int element){
    int count = 0;
    for (int i=0; i<scorelist.length; i++){
      if(element== scorelist[i]){
        count++;
      }
    }
    return count;
  }//count method

  int withoutNullLength(List scorelist){
    for(int i=0; i<scorelist.length; i++){
      if(scorelist[i] == null){
        scorelist.remove(scorelist[i]);
      }
    }
    return scorelist.length;
  }//withoutNullLength method

  void playAgain(){
    print("Do you want to play again? [Y/N]:");
    var choice = stdin.readLineSync();

    if (choice == 'Y' || choice == 'y'){
      Cradice cradice =  new Cradice();
      cradice.start();
    }
    else{
      print("Thanks for playing.");
    }
  }//playAgain method

}//Cradice class