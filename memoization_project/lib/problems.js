// Write a function, lucasNumberMemo(n), that takes in a number.
// The function should return the n-th number of the Lucas Sequence.
// The 0-th number of the Lucas Sequence is 2.
// The 1-st number of the Lucas Sequence is 1
// To generate the next number of the sequence, we add up the previous two numbers.
//
// For example, the sequence begins: 2, 1, 3, 4, 7, 11, ...
//
// Solve this recursively with memoization.
//
// Examples:
//
// lucasNumberMemo(0)   // => 2
// lucasNumberMemo(1)   // => 1
// lucasNumberMemo(40)  // => 228826127
// lucasNumberMemo(41)  // => 370248451
// lucasNumberMemo(42)  // => 599074578
function lucasNumberMemo(n, memo = {}) {
    if (n === 0) return 2;
    if (n === 1) return 1;
    if (memo[n]) return memo[n];

    
    return memo[n] = lucasNumberMemo(n - 1, memo) + lucasNumberMemo(n - 2, memo);
}


// Write a function, minChange(coins, amount), that accepts an array of coin values
// and a target amount as arguments. The method should the minimum number of coins needed
// to make the target amount. A coin value can be used multiple times.
//
// After you pass the first 3 examples, you'll likely need to memoize your code 
// in order to pass the 4th example in a decent runtime.
//
// Examples:
//  
// minChange([1, 2, 5], 11)         // => 3, because 5 + 5 + 1 = 11
// minChange([1, 4, 5], 8))         // => 2, because 4 + 4 = 8
// minChange([1, 5, 10, 25], 15)    // => 2, because 10 + 5 = 15
// minChange([1, 5, 10, 25], 100)   // => 4, because 25 + 25 + 25 + 25 = 100
function minChange(coins, amount, memo = {}) {
    if (memo[amount]) return memo[amount];
    if (amount === 0) return 0;

    let numCoins = [];

    // for (let coin in coins) {
    //     if (coins[coin] <= amount) {
    //         numCoins.push(minChange(coins, amount - coins[coin]) + 1);
    //     };
    // };

    coins.forEach(coin => {
        if (coin <= amount) {
            numCoins.push(minChange(coins, amount - coin, memo) + 1);
        };
    });

    memo[amount] = Math.min(...numCoins);
    return memo[amount];
}

//why does return numCoins show that the 1's are being added as strings?
//memoization with multi args use one that doesn't change as key

module.exports = {
    lucasNumberMemo,
    minChange
};


// You are given coins of different denominations and a total amount of money.
// Write a function to compute the number of combinations that make up that amount.
// You may assume that you have infinite number of each kind of coin.

var change = function (amount, coins, memo = {}) {
    let key = amount + '-' + coins
    if (memo[key]) return memo[key];
    if (amount === 0) return 1;

    let currentCoin = coins[coins.length - 1];
    let total = 0;

    for (let qty = 0; qty * currentCoin <= amount; ++qty) {
        total += change(amount - qty * currentCoin, coins.slice(0, -1), memo);
    };

    memo[key] = total;
    return memo[key];
}