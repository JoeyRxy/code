package m.learn;

@SuppressWarnings("unused")
public class Knapsack {
    /**
     * 
     * @param cost  是物品占用背包的（空间）代价
     * @param value 是物品的价值
     */
    public Knapsack(int[] cost, int[] value) {

    }

    public static void main(String[] args) throws Exception {
        int N = 20;
        int[] cost = new int[N];
        int[] value = new int[N];
        // 检查是否都是正整数
        for (int i = 0; i < N; i++) {
            if (cost[i] <= 0 || value[i] <= 0)
                throw new Exception("必须是正整数");
        }
        Knapsack solution = new Knapsack(cost, value);
    }
}