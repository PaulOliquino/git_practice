from msilib.schema import PublishComponent
import java.io.InputStreamReader;
import java.util.Random;

PublishComponent class DiceRoll {
  public static void main(String[] args) throws Exception {
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    Random rand = new Random();
    int diceCount = 1;

    while (true) {
      System.out.println("Enter 'roll' to roll the dice, 'add dice' to add another dice, 'remove dice' to remove a dice, or 'check dice' to check the number of dice: ");
      String command = reader.readLine();

      if (command.equals("roll")) {
        int roll = 0;
        for (int i = 0; i < diceCount; i++) {
          roll += rand.nextInt(6) + 1;
        }
        System.out.println("The dice rolled: " + roll);
      } else if (command.equals("add dice")) {
        diceCount++;
        System.out.println("Another dice has been added");
      } else if (command.equals("remove dice")) {
        if (diceCount > 1) {
          diceCount--;
          System.out.println("A dice has been removed");
        } else {
          System.out.println("Cannot remove the last dice");
        }
      } else if (command.equals("check dice")) {
        System.out.println("You currently have " + diceCount + " dice(s)");
      }
    }
  }
}
