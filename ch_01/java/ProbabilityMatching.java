import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

/**
 * class for probability matching
 */
public class ProbabilityMatching {

    // initializing a random object
    public static Random random = new Random();

    // the state space is discrete and describes the possible outcomes
    public static List<Integer> StateSpace = Arrays.asList(1, 1, 1, 1, 0);

    /**
     * the main method
     * @param args arguments
     */
    public static void main(String[] args) {

        // initializing an array of the results of 100 coin tosses vs betting
        List<Integer> rewards = new ArrayList<>();

        // a for loop of 250 iterations
        for(int i = 0; i < 250; i++) {
            rewards.add(epoch(100));
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
    public static int epoch(int n) { 

        // the total reward 
        int total_reward = 0;

        // defining the action space
        List<Integer> ActionSpace = new ArrayList<>(Arrays.asList(0, 1));

        // iterations of coin flipping
        for(int i = 0; i < n; i++) {

            // number of 1's
            int oneCount = 0;
            for(int j = 0; j < ActionSpace.size(); j++) {
                if(ActionSpace.get(j) == 1) {
                    oneCount++;
                }
            }

            // number of 0's
            int zeroCount = 1;
            for(int k = 0; k < ActionSpace.size(); k++) {
                if(ActionSpace.get(k) == 0) {
                    zeroCount++;
                }
            }

            // the chosen action using probability matching
            int actionChosen;
            if(oneCount > zeroCount) {
                actionChosen = 1;
            } else {
                actionChosen = 0;
            }

            // making a coin toss
            int coinToss = StateSpace.get(random.nextInt(StateSpace.size()));

            if(actionChosen == coinToss) {
                total_reward++;
            }

            ActionSpace.add(coinToss);
            
            
        }

        return total_reward;

    }

    
}
