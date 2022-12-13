// 1512. Number of Good Pairs
var numIdenticalPairs = function(nums) {
    let counter = 0
    for(i=0;i<nums.length;i++){
        for(j=i+1;j<nums.length;j++){
            if(nums[i] == nums[j]){
                counter += 1
            }
        }
    }
    return counter
};