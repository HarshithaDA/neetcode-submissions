class Solution {
    public int getSum(int a, int b) {
        // xor 
        //same digits -> 0
        //different digits -> 1

        //if 1 & 1 -> with xor we get 0 but we also need a carry for 1+1=2 10
        //only case we have a carry - 2 ones 
        //one carry has to be added in the left next position - so take the result and shift to left by 1 << 1

         // xor the carry (a&b) shifted to left by 1 (a&b << 1) to the result (a ^ b)
         // then & them then shift to left by 1
         //then and

        // while carry is present
         while (b != 0){
            int temp = (a&b) << 1;
            a = a^b;
            b = temp;
         }
         return a;
    }
}
