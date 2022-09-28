// Create a function that takes two numbers as arguments and returns their sum.
function addition(a, b) {
	return(a + b)
}


// Create a function that takes voltage and current and returns the calculated power.
function circuitPower(voltage, current) {
	return(voltage * current)
}


// Create a function that takes a number as an argument, increments the number by +1 and returns the result.
function addition(num) {
	return(num + 1)
}


// Create a function that takes an array containing only numbers and return the first element.
function getFirstValue(arr) {
	return(arr[0])
}


// Create a function that takes the age in years and returns the age in days.
function calcAge(age) {
	return(age * 365)
}


// Write a function that takes the base and height of a triangle and return its area.
function triArea(base, height) {
	return((base * height) / 2)
}


// Given an n-sided regular polygon n, return the total sum of internal angles (in degrees).
function sumPolygon(n) {
	return((n-2) * 180)
}


// Create a function that takes a number as its only argument and returns true if it's less than or equal to zero, otherwise return false.
function lessThanOrEqualToZero(num) {
	if(num <= 0) {
		return true
	}else{
		return false
	}
}


// Fix the code in the code tab to pass this challenge (only syntax errors). Look at the examples below to get an idea of what the function should do.
function squared(b) {
	return (b * b)
}


// Write a function that returns the string "something" joined with a space " " and the given argument a.
function giveMeSomething(a) {
	return("something "+a)
}


// Given two numbers, return true if the sum of both numbers is less than 100. Otherwise return false.
function lessThan100(a, b) {
	if(a+b < 100){
		return true
	}else{
		return false
	}
}


// Create a function that takes length and width and finds the perimeter of a rectangle.
function findPerimeter(length, width) {
	return((length + width) * 2)
}


// Mubashir wants to swap two given numbers! It is not returning the right values. Can you help him fix it?
function swap(a, b) {
	temp = b
	b = a
	a = temp
	return [a, b]
}


// Mubashir created an infinite loop! Help him by fixing the code in the code tab to pass this challenge. Look at the examples below to get an idea of what the function should do.
function printArray(number) {
    var newArray = [];
    for(var i = 1; i <= number; i++) {
        newArray.push(i);
    }
    return newArray;
}


// A student learning JavaScript was trying to make a function. His code should concatenate a passed string name with string "Edabit" and store it in a variable called result. He needs your help to fix this code.
function nameString(name){
	var b = "Edabit"
	var result = name + b
    return result
}


// Write a function that converts hours into seconds.
function howManySeconds(hours) {
	return(hours * 60 * 60)
}


// Make a function using the && operator.
function and(a, b) {
	return(a && b)
}


// Create a function that returns true when num1 is equal to num2; otherwise return false.
function isSameNum(num1, num2) {
	return num1 === num2
}


// You are counting points for a basketball game, given the amount of 2-pointers scored and 3-pointers scored, find the final points for the team and return that value.
function points(twoPointers, threePointers) {
	return((twoPointers * 2) + (threePointers * 3))
}


// There is a single operator in JavaScript, capable of providing the remainder of a division operation. Two numbers are passed as parameters. The first parameter divided by the second parameter will have a remainder, possibly zero. Return that value.
function remainder(x, y) {
	return(x % y)
}


// Create a function that takes a boolean variable flag and returns it as a string.
function boolToString(flag) {
	return(String(flag))
}


// Fix the code in the code tab to pass this challenge (only syntax errors). Look at the examples below to get an idea of what the function should do.
function cubes(a) {
	return a * a * a
}


// The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.
function animals(chickens, cows, pigs) {
	return((chickens * 2) + (cows * 4) + (pigs * 4))
}


// Create a function that will handle simple math expressions. The input is an expression in the form of a string.
function calculator(str) {
	return(eval(str))
}


// Create a function that returns the number of frames shown in a given number of minutes for a certain FPS.
function frames(minutes, fps) {
	return(minutes*(60*fps))
}


// Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.
function footballPoints(wins, draws, losses) {
	return((wins*3) + (draws))
}


// Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.
function convert(hours, minutes) {
	return((hours*3600) + (minutes*60))
}


// Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.
function nextEdge(side1, side2) {
	return(side1+side2-1)
}


// Create a function that returns the given argument, but by using an arrow function.
let arrowFunc = x => x;


// Create a function that takes two strings as arguments and return either true or false depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
function comp(str1, str2) {
	return(str1.length == str2.length)
}


// Fix the code in the code tab to pass this challenge (only syntax errors). Look at the examples below to get an idea of what the function should do.
function maxNum(n1,n2) {
	if (n1<n2){
		return n2
	}else{
		return n1
	}
}


// Given two arguments, return an array which contains these two arguments.
function makePair(num1, num2) {
	return([num1, num2])
}


// Implement a function that returns true if the parameters are equal, and false if they are not.
function checkEquality(a, b) {
	return(a === b)
}


// Write a function that returns the length of a string. Make your function recursive.
function length(str) {
	return(str.length)
}


// Create a function that returns true if an integer is evenly divisible by 5, and false otherwise.
function divisibleByFive(n) {
	return(n%5 == 0)
}


// Create a function that takes an integer and returns true if it's divisible by 100, otherwise return false.
function divisible(num) {
	return(num%100 == 0)
}


// Create a function that calculates the area of a rectangle. If the arguments are invalid, your function must return -1.
function area(h, w) {
	if(h <=0 || w <=0 ){
		return( -1)
	}else{
		return(h*w)
	}
}

// A vehicle needs 10 times the amount of fuel than the distance it travels. However, it must always carry a minimum of 100 fuel before setting off. Create a function which calculates the amount of fuel it needs, given the distance.
function calculateFuel(n) {
	if(n <= 10){
		return 100
	}else{
		return(n * 10)
	}
}


// Write a function that takes an integer minutes and converts it to seconds.
function convert(minutes) {
	return(minutes*60)	
}


// Create a function that takes three arguments prob, prize, pay and returns true if prob * prize > pay; otherwise return false.
function profitableGamble(prob, prize, pay) {
	return(prob*prize > pay)
}


// Given two strings, firstName and lastName, return a single string in the format "last, first".
function concatName(firstName, lastName) {
	return(lastName + ", " + firstName)
}


// Create a function that returns true if a string is empty and false otherwise.
function isEmpty(s) {
	if(s.length > 0){
		return false
	}else{
		return true
	}
}


// Create a function that evaluates an equation.
function eq(evaluate) {
	return eval(evaluate)
}


// The challenge is to try and fix this buggy code, given the inputs true and false. See the examples below for the expected output.
function has_bugs(buggy_code) {
	if (buggy_code) {
		return ('sad days')
	} else {
		return ("it's a good day")
	}
}


// Create a function that takes a number as an argument and returns negative of that number. Return negative numbers without any change.
function returnNegative(n) {
	if (n > 0){
		return(n-n-n)
	}else{
		return n
	}
}


// Write a function to reverse an array.
function reverse(arr) {
	var temp = []
	for(i=arr.length-1; i>=0; i--){
		temp.push(arr[i])
	}return temp
}


// Write a template string according to the following example:
function format(a, b, c) {
	const template = `Their names were: ${a}, ${b} and ${c}.`
	return template;
}


// According to the lodash documentation, _.drop creates a slice of an array with n elements dropped from the beginning.
function drop(arr, val = 1) {
	return(arr.slice(val))
}


// Help fix all the bugs in the function incrementItems! It is intended to add 1 to every element in the array!
function incrementItems(arr) {
	for (let i = 0; i < arr.length; i++)
		arr[i] = arr[i] + 1
	return arr
}


// Create a function that takes an equation (e.g. "1+1"), and returns the answer.
function equation(s) {
	return eval(s)
}


// Given two integers, a and b, return true if a can be divided evenly by b. Return false otherwise.
function dividesEvenly(a, b) {
	return(a % b == 0)
}


// Write a function that returns the boolean true if the given number is zero, the string "positive" if the number is greater than zero or the string "negative" if it's smaller than zero.
function equilibrium (x) {
	if (x > 0) return "positive"
	if (x < 0) return "negative"
	return true
}


// Write a function that returns true if the given integer is even, and false if it's odd.
function isEven(n) {
	return n % 2 == 0
}


// Given an object containing counts of both upvotes and downvotes, return what vote count should be displayed. This is calculated by subtracting the number of downvotes from upvotes.
function getVoteCount(votes) {
	return votes.upvotes - votes.downvotes
}


// Create a function that takes a string and returns it as an integer.
function stringInt(str) {
	return parseInt(str)
}


// Create a function that takes two arguments. Both arguments are integers, a and b. Return true if one of them is 10 or if their sum is 10.
function makesTen(a, b) {
	return(a == 10 || b == 10 || a + b == 10)
}


// Write a function that checks whether a person can watch an MA15+ rated movie. One of the following two conditions is required for admittance:
function acceptIntoMovie(age, isSupervised) {
	return(age >= 15 || isSupervised)
}


// Create a function that takes a string and returns it as an integer.
function stringInt(str) {
	return parseInt(str)
}


// Create a function that takes a base number and an exponent number and returns the calculation.
function calculateExponent(num, exp) {
	return(num ** exp)
}


// Given a person's age and the number of times they've moved house as moves, return the average number of years that they've spent living in the same house.
function yearsInOneHouse(age, moves) {
	return Math.round(age / (moves+1))
}


// Create a function that accepts a measurement value in inches and returns the equivalent of the measurement value in feet.
function inchesToFeet(inches) {
	return Math.floor(inches/12)
}


// In the Code tab you will find code that is missing a single character in order to pass the tests. However, your goal is to submit a function as minimalist as possible. Use the tips in the tips section below.
add2 = (x) => x + 2
add3 = (x) => x + 3
add5 = (x) => x + 5
add7 = (x) => x + 7
add11 = (x) => x + 11


// I have a bucket containing an amount of navy blue paint and I'd like to paint as many walls as possible. Create a function that returns the number of complete walls that I can paint, before I need to head to the shops to buy more.
function howManyWalls(n, w, h) {
	return Math.floor(n/(w*h))
}


// Write a function that uses the ternary operator to return "yeah" if bool is true, and "nope" otherwise.
function yeah_nope(bool) {
	return bool ? "yeah" : "nope"
}


// Given the person's age, and whether break time is in session, create a function which returns whether he should serve drinks.
function shouldServeDrinks(age, onBreak) {
	return(age >=18 && onBreak == false)
}


// Given a string, return true if its length is even or false if the length is odd.
function oddOrEven(s) {
    return(s.length % 2 == 0)
}


// Create a function that takes a word and returns the new word without including the first character.
function newWord(str) {
	return str.slice(1)
}


// Write a function that determines if the year is a leap year or not.
function leapYear(year) {
	return(year % 4 == 0 || year % 100 == 0 && year % 400 == 0)
}


// Create a function that calculates the chance of being an imposter. The formula for the chances of being an imposter is 100 × (i / p) where i is the imposter count and p is the player count.
function imposterFormula(i, p) {
	return Math.round((i/p)*100) + "%"
}


// Create a function that returns the opposite of the given boolean, as a number.
function flipBool(b) {
	if(b==true){
		return 0
	}else if (b==false){
		return 1
	}
}


// Create a function that returns how many possible arrangements can come from a certain number of switches (on / off)
function posCom(num) {
	return(2 ** num)
}


// Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers.
function isEvenOrOdd(num) {
	return num % 2 == 0 ? "even" : "odd"
}


// Write a function that accepts base (decimal), height (decimal) and shape ("triangle", "parallelogram") as input and calculates the area of that shape.
function areaShape(base, height, shape) {
	return shape == "parallelogram" ? (base * height) : (base * height * 0.5)
}


// Create a function to concatenate two integer arrays.
function concat(arr1, arr2) {
	return arr1.concat(arr2)
}


// Someone has written the function isOdd() to check if a given number is odd or not. Unfortunately, the function does not return the correct result for all the inputs. Help her fix the error.
function isOdd(num) {
	return (num % 2 == 1 || num % 2 == -1)
}


// You need to create two functions to substitute toString() and parseInt(); A function called intToString() that converts integers into strings and a function called stringToInt() that converts strings into integers.
function intToString(num) {
	return(num + "")
}

function stringToInt(num) {
	return(parseInt(num))
}


// You must calculate the number of people there will be in three decades from now. You must calculate the number of people there will be in three decades from now.
function futurePeople(population, n) {
	return(population + (n*360))
}


// Create a function that takes an array of numbers or letters and returns a string.
function arrayToString(arr) {
	return(arr.join(""))
}


// Create a function that accepts an array and returns the last item in the array.
function getLastItem(arr) {
	return(arr[arr.length-1])
}


// Fix the code in the code tab to pass this challenge (only syntax errors). Look at the examples below to get an idea of what the function should do.
function sumArray(arr) {
	var sum = 0
    for (i=0; i<arr.length; i++) {
		sum+=arr[i]
	}
	return sum
}


// Create a function that returns a number, based on the string provided. Here is a list of all digits:
function word(s) {
	var x = (["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])
	return x.indexOf(s)
}


// Create a function that takes a name and returns a greeting in the form of a string. Don't use a normal function, use an arrow function.
const helloName = name => "Hello " + name + "!"


// Write a function to check if an array contains a particular number.
function check(arr, el) {
	return arr.includes(el)
}


// Write a function that returns the string "even" if the given integer is even, and the string "odd" if it's odd.
function parity(n) {
	return n % 2 == 0 ? "even":"odd"
}


// A typical car can hold four passengers and one driver, allowing five people to travel around. Given n number of people, return how many cars are needed to seat everyone comfortably.
function carsNeeded(n) {
	return Math.ceil(n/5)
}


// Given a Rubik's Cube with a side length of n, return the number of individual stickers that are needed to cover the whole cube.
function howManyStickers(n) {
	return(n*n*6)
}


// Some basic arithmetic operators are +, -, *, /, and %. In this challenge you will be given three parameters, num1, num2, and an operator. Use the operator on number 1 and 2.
function operate(num1, num2, operator) {
	return(eval(num1 + operator + num2))
}


// Given an index and an array, return the value of the array with the given index.
function valueAt(arr, i) {
	return(arr[Math.floor(i)])
}


// Return the Kinetic Energy in Joules, given the mass and velocity. For the purposes of this challenge, round answers to the nearest integer.
function kineticEnergy(m, v) {
	return Math.round(0.5 * m * v ** 2)
}


// Given the after-tax income as ati, what you are supposed to do is to make a function that will return an object that shows how much a person needs to spend on needs, wants, and savings.
function fiftyThirtyTwenty(ati) {
	return {
		"Needs" : ati * 0.5,
		"Wants" : ati * 0.3,
		"Savings" : ati * 0.2
	}
}


// Given the radius of a circle and the area of a square, return true if the circumference of the circle is greater than the square's perimeter and false if the square's perimeter is greater than the circumference of the circle.
function circle_or_square(rad, area){
	var rad = rad * 3.14 * 2
	var area = Math.sqrt(area) * 4
	return(rad > area)
}


// Given two arrays, which represent two sandwiches, return whether both sandwiches use the same type of bread. The bread will always be found at the start and end of the array.
function hasSameBread(arr1, arr2) {
	return(arr1[0] == arr2[0] && arr1[2] == arr2[2])
}


// Create a function that returns true if a string contains any spaces.
function hasSpaces(str) {
	return(str.includes(" "))
}


// Create a function that takes a string (a random name). If the last character of the name is an "n", return true, otherwise return false.
function isLastCharacterN(word) {
	return(word.endsWith("n"))
}


// Return what bag is needed for the product
function getContainer(product) {
	switch (product) {
		case "Bread": return "bag";
		case "Beer":
		case "Milk": return "bottle";
		case "Cerials": return "box";
		case "Eggs": return "carton";
		case "Candy": return "plastic";
		default: return null;
	}
}


// Create a function that takes an array and returns the types of values (data types) in a new array.
function arrayValuesTypes(arr) {
	var list = []
	for(let i=0;i<arr.length;i++){
		list.push(typeof(arr[i]))
	}
	return list
}


// This challenge is a bit different as the function you are given already contains some code that you should not change or remove. Also, don't do a return statement, it is already included. Your task is, given an object, prevent changes to that object.
function preventChanges(obj) {
	Object.freeze(obj)
// DON'T CHANGE OR REMOVE THE LINES BELOW
	obj.noChanges = false;
	obj.signature = "whatever";
	return obj;
}


// Create a function that takes two numbers num1, num2, and an array arr and returns an array containing all the numbers in arr greater than num1 and less than num2.
function arrBetween(num1, num2, arr) {
	list = []
	for (i=0;i<arr.length;i++){
		if(arr[i] > num1 && arr[i] < num2){
			list.push(arr[i])
		}
	}
	return list
}


// Create a function that takes a positive integer n and returns the nth "star number".
function starNumber(n) {
	return (6 * n * (n-1) + 1)
}


// Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.
function relationToLuke(name) {
	const data = {
		"Darth Vader":"father",
		"Leia":"sister",
		"Han":"brother in law",
		"R2D2":"droid"
	}
	return `Luke, I am your ${data[name]}.`
}


// Write a function that returns the strings: "both" if both given booleans a and b are true. "first" if only a is true. "second" if only b is true ."neither" if both a and b are false.
function areTrue(a, b) {
	if (a == true && b == true) {
		return "both";
	} else if (a == true) {
		return "first";
	} else if (b == true) {
		return "second";
	} else {
		return "neither";
	}
}


// Create a function that takes as a parameter an array of "stringified" numbers and returns an array of numbers.
function toNumberArray(arr) {
	const num = arr.map((i) => Number(i));
	return(num);
}


// Create a function that takes a string and returns the concatenated first and last character.
function firstLast(name) {
	return name.charAt(0) + name.charAt(name.length-1)
}


// Create a function that takes in a word and determines whether or not it is plural. A plural word is one that ends in "s".
function isPlural(word) {
	return(word.endsWith("s"))
}


// Create a function that takes an array of integers and strings. Convert integers to strings and return the new array.
function parseArray(arr) {
	return arr.map(String);
}


// Create a function that takes a string; we'll say that the front is the first three characters of the string. If the string length is less than three characters, the front is whatever is there. Return a new string, which is three copies of the front.
function frontThree(str) {
	var x = (str.slice(0,3))
	return x.repeat(3)
}


// Create a function that takes a number n and returns the nth even number beginning with 0 as the first.
function nthEven(n) {
	return ((n*2)-2)
}


// A taxi journey costs $3 for the first kilometer travelled. However, all kilometers travelled after that will cost $2 each. Create a function which returns the distance that the taxi must've travelled, given the cost as a parameter.
function journeyDistance(num) {
	return Math.floor(num/2)
}


// Your task: Create variables first, second, third and other from the given array using Destructuring Assignment
let [first,second,third,...other] = [1, 2, 3, 4, 5, 6, 7, 8];


// Create a function that takes an object as an argument and returns a string with facts about the city. The city facts will need to be extracted from the object's three properties:
function cityFacts(city) {
	return `${city.name} has a population of ${city.population} and is situated in ${city.continent}`
}


//Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.
function stutter(word) {
	x = word.slice(0,2) + "... "
	return x.repeat(2) + word + "?"
}


// Create a function which validates whether a given number exists, and could represent a real life quantity. Inputs will be given as a string.
function validStrNumber(n) {
	return !isNaN(n)
}


// Create a function that takes a string txt and a number n and returns the repeated string n number of times. If given argument txt is not a string, return Not A String !!
function repeatString(txt, n) {
	if ((typeof txt) === 'string'){
		return txt.repeat(n)
	}
	return "Not A String !!"
}


// Create a function that inverts the rgb values of a given tuple.
function colorInvert(rgb) {
	for(i=0;i<rgb.length;i++){
		rgb[i] = 255-rgb[i]
	}
	return rgb
}


// Create a function that takes in a current mood and return a sentence in the following format: "Today, I am feeling {mood}". However, if no argument is passed, return "Today, I am feeling neutral".
function moodToday(mood) {
	return `Today, I am feeling ${mood||"neutral"}`
}


// Given a fraction as a string, return whether or not it is greater than 1 when evaluated.
function greaterThanOne(frac) {
	return (eval(frac) > 1)
}


// Create a function that returns the number of arguments it was called with.
function numArgs() {
	return arguments.length
}


// Create a function that returns the number of syllables in a simple string. The string is made up of short repeated words like "Lalalalalalala" (which would have 7 syllables).
function countSyllables(str) {
	return (str.length/2)
}


// Create a function that returns the ASCII value of the passed in character.
function ctoa(c) {
	return c.codePointAt(0);
}


// Create a function that takes the number of daily average recovered cases recovers, daily average newCases, current activeCases, and returns the number of days it will take to reach zero cases.
function endCorona(recovers, newCases, activeCases) {
	return Math.ceil(activeCases / (recovers-newCases))
}


// Write a function that validates whether two strings are identical. Make it case insensitive.
function match(s1, s2) {
	return (s1.toLowerCase() == s2.toLowerCase())
}


// Create a function that determines whether or not it's possible to split a pie fairly given these three parameters: Total number of slices. Number of recipients. How many slices each person gets.
function equalSlices(total, people, each) {
	return((total / (people*each)) >= 1)
}


// There is an easy way to assign to array values to the nth index by using rest parameter syntax.
	const str = '[head, ...tail] = [1, 2, 3, 4]'


// You will need to write three unfinished logic gates. Continue to write the three logic gates: AND, OR, and NOT.
function NOT(n) {
	return +!n
}
function AND(a, b) {
	return(a && b)
}
function OR(a, b) {
	return(a||b)
}


// Spot and fix the error(s) in the code to make the function work.
function sortWord(word){
	return word.split('').sort().join('');
}


// Write a function that returns true if k^k == n for input (n, k) and return false otherwise.
function kToK(n, k) {
	return(k**k == n)
}


// Create a function that takes a number and return an array of three numbers: half of the number, quarter of the number and an eighth of the number.
function halfQuarterEighth(n) {
	return[(n*0.5),(n*0.25),(n*0.125)]
}


// Create a function that takes an array of two numbers and checks if the square root of the first number is equal to the cube root of the second number.
function checkSquareAndCube(arr) {
	return Math.sqrt(arr[0]) == Math.cbrt(arr[1])
}


// Create a function that takes an angle in radians and returns the corresponding angle in degrees.
function radiansToDegrees(rad) {
	return (rad * (180/Math.PI))
}


// Create a function that takes an angle in radians and returns the corresponding angle in degrees.
function addBinary(a,b) {
	return (a+b).toString(2)
}


// Create a function that takes an array of words and transforms it into an array of each word's length.
function wordLengths(arr) {
	for(i=0;i<arr.length;i++){
		arr[i] = arr[i].length
	}
	return arr
}


// You can assign variables from arrays with destructuring like this. But you can also skip over items in the array being destructured.
const arr = ["eyes", "nose", "lips", "ears"]
var [eyes, nose, lips, ears] = arr


// Create a function that checks if the argument is an integer or a string. Return "int" if it's an integer and "str" if it's a string.
function intOrString(param) {
	if(typeof(param) == "number"){
		return "int"
	}return "str"
}


// Write a function that returns the first truthy argument passed to the function. If all arguments are falsy, return the string "not found". The function will be called with a minimum of one and a maximum of four arguments: a, b, c, d.
function firstOne(a, b = 0, c = 0, d = 0) {
	return(a || b || c || d || "not found")
}


// Create a function that takes a string and changes the word amazing to not amazing. Return the string without any change if the word edabit is part of the string.
function amazingEdabit(str) {
	if (str.includes("edabit")){
		return str
	}else{
		return str.replace("amazing", "not amazing")
	}
}


// Create a function that returns the total number of parameters passed in.
function numberArgs(...a) {
	return arguments.length
}


// Create a function that takes a whole number as input and returns the shape with that number's amount of sides. Here are the expected outputs to get from these inputs.
function nSidedShape(n) {
	var data = {
		1	:"circle",
		2	:"semi-circle",
		3	:"triangle",
		4	:"square",
		5	:"pentagon",
		6	:"hexagon",
		7	:"heptagon",
		8	:"octagon",
		9	:"nonagon",
		10 :"decagon"
	}
	return data[n]
}


// Create a function that has some arguments and returns the type of the fifth argument. In case the arguments were less than 5, return "Not enough arguments".
function fifth() {
	if (arguments.length<5){
		return "Not enough arguments"
	}return typeof(arguments[4])
}


// Create a function that takes an array with numbers and return an array with the elements multiplied by two.
function getMultipliedArr(arr) {
	for(i=0;i<arr.length;i++){
		arr[i] = arr[i] * 2 
	}return arr
}


// Create a function that returns the name of the man who can bring home the most items. The parameters are given as follows:
function whoWinsTonight(coins, space, price, size) {
	x = Math.floor(coins/price)
	y = Math.floor(space/size)
	if (x > y){
		return "Bill"
	}else if (x < y){
		return "Will"
	}return "Tie"
}


// Given an array, rotate the values clockwise by one (the last value is sent to the first position).
function rotateByOne(arr) {
	x = arr.length-1
	y = [arr[x]]
	for(i=0;i<arr.length-1;i++){
		y.push(arr[i])
	}return(y)
}	


// Implement a function that returns the volume of the pizza as a whole number, rounding it to the nearest integer (and rounding up for numbers with .5 as decimal part).
function volPizza(radius, height) {
	return Math.round((radius**2)*height*Math.PI)
}


// Create a function which returns the length of a string, WITHOUT using String.length property.
function length(s) {
	var x = 0
	for(i=0;i<s.length;i++){
		x += 1
	}return x
}


// Create a function that returns the string "Burp" with the amount of "r's" determined by the input parameters of the function.
function longBurp(num) {
	x = ""
	for(i=0;i<num;i++){
		x = x + "r"
	} return("Bu" + x + "p")
}

// Create a function that counts how many D's are in a sentence.
function countDs(sentence) {
	var x = 0
	for(i=0;i<sentence.length;i++){
		if(sentence[i] == "D" || sentence[i] == "d"){
			x += 1
		}
	}return x
}


// If the number is a multiple of 3, return "Hello". If the number is a multiple of 5, return "World". If the number is a multiple of both 3 and 5, return "Hello World".
function helloWorld(num) {
	if(num % 3 == 0 && num % 5 == 0){
		return "Hello World"
	}else if(num % 3 == 0){
		return "Hello"
	}return "World"
}


// ES6: Destructuring Arrays II
let [ trans1, trans2, [trans3, [trans4 ]]] = arr


// Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time.
function damage(damage, speed, time) {
	const x = damage * speed
	if(damage > 0 && speed > 0){
		if(time == "second"){
			return x
		}else if (time == "minute"){
			return (x * 60)
		}else if (time == "hour"){
			return (x * 3600)
		}
	}return "invalid"
}


// Sometimes an object will be missing properties we are expecting. We can avoid undefined errors by using default values. Use ES6 object destructuring to add a default value of 1 to the one variable. Ignore the .toString() function (used for validation).
const str = `({ one = 1, two } = { two : 2}).toString()`


//  create three functions for the class that returns the following strings: getAge() returns "name is age age" getHeight() returns "name is heightcm" getWeight() returns "name weighs weightkg"
class Player {
	constructor(name, age, height, weight) {
		this.name = name
		this.age = age
		this.height = height
		this.weight = weight
	}
	
	getAge() {
		return this.name + " is age " + this.age
	}

	getHeight() {
		return this.name + " is " + this.height + "cm"
	}
		
	getWeight() {
		return this.name + " weighs " + this.weight + "kg"
	}
}


// For each of the 6 coffee cups I buy, I get a 7th cup free. In total, I get 7 cups. Create a function that takes n cups bought and return as an integer the total number of cups I would get.
function totalCups(n) {
	let x = Math.floor(n / 6)
	return x + n
}


// Create a function that takes a string and returns a string with spaces in between all of the characters.
function spaceMeOut(str) {
	let results = ""
	for(i = 0;i < str.length;i++){
		results = results + str[i] + " "
	}
	return results.trimEnd()
}


// Write a function that takes two numbers and returns if they should be added, subtracted, multiplied or divided to get 24. If none of the operations can give 24, return null.
function operation(num1, num2) {
	if(num1 + num2 == 24){
		return("added")
	}else if(num1 - num2 == 24){
		return("subtracted")
	}else if(num1 * num2 == 24){
		return("multiplied")
	}else if(num1 / num2 == 24){
		return("divided")
	}else{
		return(null)
	}
}


// Create a function that takes an array and returns the sum of all numbers in the array.
function getSumOfItems(arr) {
	let sum = 0
	for(i=0;i<arr.length;i++){
		sum += arr[i]
	}
	return sum
}


// calculates its radius and its height. Now, he wants to know from you the total volume of pizza
function volPizza(radius, height) {
	return Math.round(radius**2 * height * Math.PI)
}