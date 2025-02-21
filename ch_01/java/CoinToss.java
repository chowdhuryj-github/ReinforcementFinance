
// all necessary imports
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;


/**
 * class for CoinToss
 */
public class CoinToss {

    // initializing a random object
    public static Random random = new Random();

    // the state space is discrete and describes the possible outcomes
    public static List<Integer> StateSpace = Arrays.asList(1, 1, 1, 1, 0);

    // the action space is the discrete actions that can be taken
    public static List<Integer> ActionSpace = Arrays.asList(0, 1);


    /**
     * the main method
     * @param args arguments
     */
    public static void main(String[] args) {

        // initializing an array of the results of 100 coin tosses vs betting
        List<Integer> rewards = new ArrayList<>();

        // a for loop of 250 iterations
        for(int i = 0; i < 250; i++) {
            rewards.add(epoch());
        }
        
        // calculating the total reward
        int sumRewards = 0;
        for(int reward :rewards) {
            sumRewards += reward;
        }

        // calculating the average of the rewards
        int averageReward = sumRewards / rewards.size();

        // printing out the final result
        System.out.println("Average Reward: " + averageReward);
        
    }

    /**
     * the epoch method for betting vs tossing
     * @return the total reward
     */
    public static int epoch() {

        // the total reward 
        int total_reward = 0;

        // a hundred loops
        for(int i = 0; i < 100; i++) {

            // making a random bet
            int randomBet = StateSpace.get(random.nextInt(ActionSpace.size()));

            // making a coin toss
            int coinToss = ActionSpace.get(random.nextInt(ActionSpace.size()));

            // if the bet matches the toss, then we increment by 1
            if(randomBet == coinToss) {
                // incrementing the total reward
                total_reward++;
            }

        }

        // returning the total reward
        return total_reward;
    }

}