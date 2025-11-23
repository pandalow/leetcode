背包问题
```c++
#include <iostream>
#include <vector>

using namespace std;

int main(){
    int m , n;
    cin >> m >> n;
    vector<vector<int>> mater(m, vector<int>(2));

    // 所占空间
    for(int i = 0; i < m; i++){
        cin >> mater[i][0];
    }
    // 材料价值
    for(int i = 0; i< m ; i++){
        cin >> mater[i][1];
    }


    //明确dp数组定义, 
    // dp[i][j] 表示从下标为[0-i]的物品里任意取，放进容量为j的背包，价值总和最大是多少。;
    // 这里j的背包是一个假设从0到n上限, 
    // 举例说明: dp[1][4]任取 物品0，物品1 放进容量为4的背包里，最大价值是 dp[1][4];
    vector<vector<int>> dp(m, vector<int>(n+1,0));
    
    // 初始化, 初始化首行/首列, 从而就可以获得想要推出的元素了;
    // 首列必为0,因为背包空间为0; 
    // 首行为index0物品的价值, 但是重量要符合
    for(int j = mater[0][0]; j <= n ; j++){
        dp[0][j] = mater[0][1];
    }

    //明确递推公式
    // 求取 dp[1][4] 有两种情况：
    //      放物品1
    //      还是不放物品1
    //          - 如果不放物品1， 那么背包的价值应该是 dp[0][4] 即 容量为4的背包，只放物品0的情况。
    //          - 如果放物品1， 那么背包要先留出物品1的容量，目前容量是4，物品1 的容量（就是物品1的重量）为3，此时背包剩下容量为1。 容量为1，只考虑放物品0 的最大价值是 dp[0][1]，这个值我们之前就计算过。
    for(int i = 1; i < m; i++ ){
        for(int j = 0; j <=n; j++){
            if(j < mater[i][0]){
                dp[i][j] = dp[i-1][j];
            }else{            
                dp[i][j] = std::max(dp[i-1][j],dp[i-1][j-mater[i][0]]+mater[i][1]);
                }

        }

    }

    cout << dp[m-1][n] << endl;
    return 0;
}
```