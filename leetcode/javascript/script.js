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

// 1929. Concatenation of Array
var getConcatenation = function(nums) {
    let answer = new Array(nums.length*2)
    for(i=0;i<nums.length;i++){
        answer[i] = nums[i]
        answer[i+nums.length] = nums[i]
    }
    return answer
};

// 1920. Build Array from Permutation
var buildArray = function(nums) {
    let answer = new Array(nums.length)
    for(i=0;i<nums.length;i++){
        answer[i] = nums[nums[i]]
    }
    return answer
};

// 2769. Find the Maximum Achievable Number
var theMaximumAchievableX = function(num, t) {
    return num + (t*2)
};
