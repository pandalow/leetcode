[7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)

```
class Solution {
public:
    int reverse(int x) {

        int results = 0;

        while(x!=0){
            // 取最后一位数字
            int digit = x % 10;
            // 减少当前位数
            x /= 10;
            // 对overflow 进行判断, 正数部分, 这里要特殊处理
            // 如果当前结果位数比32位数字/10大, 就证明下一次乘法位数必然超限了
            if(results > INT_MAX / 10 ){
                return 0;
                //如果正好是相同位数, 就需要判断整个乘法会不会超过后面的数字
            }else if(results == INT_MAX /10 && digit > 7){
                return 0;
            }
            //对overflow进行判断, 负数部分
            //
            if(results < INT_MIN /10){
                return 0;
            }else if(results == INT_MIN/10 && digit < -8){
                return 0;
            }
            results = results * 10 + digit;
        }
        return results;

    }
};
```
