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

// 2894. Divisible and Non-divisible Sums Difference
var differenceOfSums = function(n, m) {
    let answer = 0
    for(i=1;i<n+1;i++){
        if(i % m == 0){
            answer = answer - i
        }else{
            answer = answer + i
        }
    }
    return answer
};
