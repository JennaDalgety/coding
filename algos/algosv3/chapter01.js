//Set myNumber to 42 . Set myName to your name. Now swap myNumber into myName & vice versa.//

// let myNumber = 42;
// let myName = "Jenna";

// [myNumber, myName] = [myName, myNumber];



//Print integers from -52 to 1066 using a FOR loop.//

// for (let i = -52; i <= 1066; i++) {
//     console.log(i);
// }



//Create beCheerful() . Within it, console.log string "good morning!" Call it 98 times.//

// const beCheerful = () => {
//     let i = 1
//     while (i <= 98) {
//         console.log("good morning!");
//         i++;
//     };
// }

// return beCheerful();



//Using FOR , print multiples of 3 from -300 to 0. Skip -3 and -6.//

// for (let i = 3; i >= -301; i--) {
//     if (i % 3 === 0) {
//         if (i === -3 || i === -6) {
//             continue;
//         } else {
//             console.log(i);
//         }
//     }
// }



//Print integers from 2000 to 5280, using a WHILE .//

// let i = 2000;

// while (i <= 5280) {
//     console.log(i);
//     i++;
// }



//If 2 given numbers represent your birth month and day in either order , log "How did you know?" , else log "Just another day...."//

// const birthday = (day, month) => {
//     if ((day === 1) && (month === "February")) {
//         console.log("How did you know?");
//     } else {
//         console.log("Just another day....")
//     }
// }

// return birthday(1, "February");



//Write a function that determines whether a given year is a leap year. If a year is divisible by four, it is a leap year, unless it is divisible by 100. However, if it is divisible by 400, then it is .//

// const isLeapYear = (inputYear) => {
//     if ((inputYear % 4 === 0) && (inputYear % 100 !== 0) || (inputYear % 400 === 0)) {
//         console.log(`${inputYear} is a leap year.`)
//     } else {
//         console.log(`${inputYear} is NOT a leap year.`)
//     }
// }

// return isLeapYear(2337);



//Print all integer multiples of 5, from 512 to 4096. Afterward, also log how many there were.//

// let count = 0;
// for (let i = 512; i <= 4097; i++) {
//     if (i % 5 === 0) {
//         console.log(i);
//         i++;
//         count++;
//     }
// }
// document.write(count);



//Print multiples of 6 up to 60,000, using a WHILE .//

// let i = 6;
// while (i <= 60000) {
//     if (i % 6 === 0) {
//         console.log(i);  
//     }
//     i++;
// }



//Print integers 1 to 100. If divisible by 5, print "Coding" instead . If by 10, also print " Dojo" .//

// for (i = 1; i <= 100; i++) {
//     if (i % 10 === 0) {
//         console.log("Coding Dojo");
//     } else if (i % 5 === 0) {
//         console.log("Coding");
//     } else {
//         console.log(i);
//     }
// }



//Your function will be given an input parameter incoming . Please console.log this value.//
// const ahoy = (incoming) => {
//     console.log(incoming);
// }
// return ahoy("Hello!")



//Add odd integers from -300,000 to 300,000, and console.log the final sum. Is there a shortcut?//
// let sum = 0;
// for (let i = -300000; i <= 300000; i+=2) {
//     sum += i;
// }
// console.log(sum);



//Log positive numbers starting at 2016, counting down by fours (exclude 0), without a FOR loop.//

// let posNum = 2016;
// while (posNum > 0) {
//     if (posNum % 4 === 0) {
//         console.log(posNum);
//     }
//     posNum--;
// }



//Based on earlier “Countdown by Fours”, given lowNum , highNum , mult , print multiples of mult from highNum down to lowNum , using a FOR . For (2,9,3) , print 963 (on successive lines).//

// const lowHighMult = (lowNum, highNum, mult) => {
//     for (i = highNum; i >= lowNum; i--) {
//         if (i % mult === 0) {
//             console.log(i);
//         }
//     }
// }
// return lowHighMult(2, 9, 3);



//This is based on “Flexible Countdown”. The parameter names are not as helpful, but the problem is essentially identical; don’t be thrown off! Given 4 parameters (param1,param2,param3,param4) , print the multiples of param1 , starting at param2 and extending to param3 . One exception: if a multiple is equal to param4 , then skip (don’t print) it. Do this using a WHILE . Given (3,5,17,9) , print 6,12,15 (which are all of the multiples of 3 between 5 and 17 , and excluding the value 9 ).//

//param1 = mult
//param2 = low
//param3 = high
//param4 = skip

// const finalCount = (param1, param2, param3, param4) => {
//     let i = param2;
//     while (i <= param3) {
//         if ((i % param1 === 0) && (i != param4)) {
//             console.log(i);
//         }
//         i++;
//     }
// }
// return finalCount(3, 5, 17, 9);



//Create a function that accepts a number as an input. Return a new array that counts down by one, from the number (as array’s ‘zeroth’ element) down to 0 (as the last element). How long is this array?//

// const countdown = (numby) => {
//     arr = [];
//     for (i = numby; i >= 0; i--) {
//         arr.push(i);
//     }
//     console.log(arr);
//     console.log(arr.length);
// }
// return countdown(5);



//Your function will receive an array with two numbers. Print the first value, and return the second.//

// const printReturn = (arr) => {
//     console.log(arr[0]);
//     return arr[1];
// }
// return printReturn([2,3]);



//Given an array, return the sum of the first value in the array, plus the array’s length. What happens if the array’s first value is not a number, but a string (like "what?") or a boolean (like false ).//

// const returny = (arr) => {
//     return(arr[0] + arr.length);
// }
// returny([2,3]);



//For [1,3,5,7,9,13] , print values that are greater than its 2 nd value. Return how many values this is.//

// const arr = [, 3, 5, 7, 9, 13];
// let count = 0;

// for (let i = 0; i <= arr.length; i++) {
//     if (arr[i] > arr[1]) {
//         console.log(arr[i]);
//         count ++;
//     }
// }
// return(count);



//Write a function that accepts any array, and returns a new array with the array values that are greater than its 2 nd value. Print how many values this is. What will you do if the array is only one element long?//

// const general2 = (arr) => {
//     let count = 0;
//     let newArr = [];
//     if (arr.length <= 1) {
//         console.log("This array is only one character long");
//     } else {
//         for (let i = 0; i <= arr.length; i++) {
//             if (arr[i] > arr[1]) {
//                 newArr.push(arr[i]);
//                 count++;
//             }
//         } 
//         console.log(newArr);
//         console.log(count);     
//     } 
// }
// general2([2, 4, 6, 8, 10]);



//Given two numbers, return array of length num1 with each value num2 . Print "Jinx!" if they are same.//

// const jinxy = (num1, num2) => {
//     let arr = [];
//     if (num1 === num2) {
//         console.log("Jinx!");
//         return; 
//     } else {
//         while (arr.length <= num2) {
//             arr.push(num1);
//         }
//     }
//     console.log(arr);
// }
// jinxy(5, 5);



//Your function should accept an array. If value at [0] is greater than array’s length, print "Too big!" ; if value at [0] is less than array’s length, print "Too small!" ; otherwise print "Just right!" .//

// const threeBears = (arr) => {
//     if (arr[0] > arr.length) {
//         console.log("Too big!");
//     } else if (arr[0] < arr.length) {
//         console.log("Too small!");
//     } else {
//         console.log("Just right!");
//     }
// }
// threeBears([5, 2, 3]);



//Kelvin wants to convert between temperature scales. Create fahrenheitToCelsius(fDegrees) that accepts a number of degrees in Fahrenheit, and returns the equivalent temperature as expressed in Celsius degrees. For review, Fahrenheit = (9/5 * Celsius) + 32 .//

// const fahrenheitToCelsius = (fDegrees) => {
//     let celsius = (fDegrees - 32) * 5/9;
//     return(celsius);
// }
// fahrenheitToCelsius(50);



//Create celsiusToFahrenheit(cDegrees) that accepts number of degrees Celsius, and returns the equivalent temperature expressed in Fahrenheit degrees.//

// const celsiusToFahrenheit = (cDegrees) => {
//     let farenheit = (9/5 * cDegrees) + 32;
//     return(farenheit);
// }
// celsiusToFahrenheit(10);



//Given an array, write a function that changes all positive numbers in the array to “big”. Example: makeItBig([-1,3,5,-5]) returns that same array, changed to [-1,"big","big",-5] .

// const makeItBig = (arr) => {
//     for (let i = 0; i < arr.length; i++) {
//         if (arr[i] > 0) {
//             arr[i] = "big";
//         }
//     }
//     return(arr);
// };
// makeItBig([-1, 3, 5, -5]);



//Create a function that takes array of numbers. The function should print the lowest value in the array, and return the highest value in the array.

// const lowHigh = (arr) => {
//     console.log(Math.min.apply(null, arr));
//     return Math.max.apply(null, arr);
    
// };
// lowHigh([1,3,5,7]);



//Build a function that takes array of numbers. The function should print second-to-last value in the array, and return first odd value in the array.

// const printReturn = (arr) => {
//     console.log(arr[arr.length - 2]);
//     for (let i = 0; i < arr.length; i++) {
//         if (arr[i] % 2 != 0) {
//             return(arr[i]);
//         }
//     }
// }
// printReturn([1, 3, 5, 7, 9]);



//Given array, create a function to return a new array where each value in the original has been doubled. Calling double([1,2,3]) should return [2,4,6] without changing original.

// const double = (arr) => {
//     let newArr = [];
//     for (let i = 0; i < arr.length; i++) {
//         newArr.push(arr[i] * 2);
//     }
//     return(newArr);
// }
// double([1, 2, 3]);



//Given array of numbers, create function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.

// const countPositives = (arr) => {
//     let positiveCount = 0;
//     for (let i = 0; i < arr.length; i++) {
//         if (arr[i] > 0) {
//             positiveCount += 1;
//         }
//     }
//     arr.pop();
//     arr.push(positiveCount);
//     return(arr);
// }
// countPositives([-1, -1, 1, 1]);



//Create a function that accepts an array. Every time that array has three odd values in a row, print "That’s odd!" Every time the array has three evens in a row, print "Even more so!"

// const evensOdds = (arr) => {
//     for (let i = 0; i < arr.length - 2; i++) {
//         if ((arr[i] % 2 != 0) && (arr[i + 1] % 2 != 0) && (arr[i + 2] % 2 != 0)) {
//             console.log("That's odd!");
//         } else if ((arr[i] % 2 === 0) && (arr[i + 1] % 2 === 0) && (arr[i + 2] % 2 === 0)) {
//             console.log("Even more so!");
//         }
//     }
// }
// evensOdds([1, 2, 2, 4, 5, 7, 7, 8, 9]);



//Given arr , add 1 to odd elements ( [1] , [3] , etc.), console.log all values and return arr .

// const incrementSecond = (arr) => {
//     for (let i = 0; i < arr.length; i++) {
//         if (arr[i] % 2 != 0) {
//             arr[i] = arr[i] + 1;
//         }
//     }
//     console.log(arr);
// }
// incrementSecond([1, 2, 3, 4, 5]);



You are passed an array containing strings. Working within that same array, replace each string with a number – the length of the string at previous array index – and return the array.

const previousLength = (arr) => {
    for (let i = 0; i < arr.length; i++) {
        if (i === 0) {
            arr[i] = arr[i].length;
        } 
        else if (i > 0) {
            arr[i] = arr[i-1].length;
        }
    }
    console.log(arr);
}
previousLength(["cat", "Mary", "doctor", "bike"]);