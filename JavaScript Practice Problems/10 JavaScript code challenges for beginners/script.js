// 1. Print all even numbers from 0 – 10
for(i=0; i<=10;i+=2) {
    console.log(i)
}

// 2. Print a table containing multiplication tables
function multiplicationTable(element) {
    for(i=1; i<=element; i++) {
        for(n=1; n<=element; n++) {
            console.log(i +" * "+ n +" = " +(i*n))
        }
    }
}

console.log(multiplicationTable(10))

// 3. Create a length converter function
function kilotomiles(element) {
    return (element * 0.62137119)
}
console.log(kilotomiles(10))

// 4. Calculate the sum of numbers within an array
var x = ([-5, 1, -3, 0, -2, 8, -8])
function sumArray(arr) {
    var count = 0
    for(i=0; i<x.length; i++) {
        count = count + x[i];
    }return count
}
console.log(sumArray(x))

// 5. Create a function that reverses an array
var x = ([-5, 1, -3, 0, -2, 8, -8])
var y = []
function reverse(arr) {
    for(i=x.length-1; i >= 0; i--) {
        y.push(x[i])
    }return y
}   

console.log(reverse(x))

// 6. Sort an array from lowest to highest
var x = ([-5, 1, -3, 0, -2, 8, -8])
function arrange(a, b) {
    return a-b;
}

console.log(x.sort(arrange))

// 7. Create a function that filters out negative numbers
var x = ([-5, 1, -3, 0, -2, 8, -8])
function filterNegative(arr) {
    var y = ([])
    for(i=0; i < x.length; i++) {
        if(x[i] >= 0) {
            y.push(x[i]);
        }
    }return y;
}
console.log(filterNegative(x))

// 8. Remove the spaces found in a string
var x = "Today was a good day"
function removeSpace(element) {
    return element.replace(/ /g, "")
}

console.log(removeSpace(x))

// 9. Return a Boolean if a number is divisible by 10
function div10(element) {
    if(element % 10 == 0){
        return true
    }else{
        return false
    }
}
console.log(div10(10))

// 10. Return the number of vowels in a string
var x = "Today was a good day";
function returnVowels(element) {
    count = element.match(/[aeiou]/gi).length;
    return count
}

console.log(returnVowels(x))