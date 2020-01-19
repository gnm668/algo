//tabulation notes

function tabFib(n) {
    let table = new Array(n);

    table[0] = 0;
    table[1] = 1;

    for (let i = 2; i <= n; ++i) {
        table[i] = table[i - 1] + table[i -2];
    }

    return table[n];
}

function tabFib2(n) {
    let secondLast = 0;
    let last = 1;

    if (n === 0) return secondLast;
    if (n === 1) return last;

    for (let i = 2; i <= n; ++i) {
            let temp = last;
            last = last + secondLast;
            secondLast = temp;
    }

    return last;
}

//bubble sort notes

function swap(arr, idx1, idx2) {
    let temp = arr[idx1];
    arr[idx1] = arr[idx2];
    arr[idx2] = temp;
}

function bubbleSort(arr) {
    let sorted = false;

    while (!sorted) {
        sorted = true;

        for (let i = 0; i < arr.length; ++i) {
            if (arr[i] > arr[i + 1]) {
                swap(arr, i, i + 1);
                sorted = false;
            }
        }
    }

    return arr;

}

//selection sort 

function minumumValueIndex(arr) {
    let minIndex = 0;

    for (let j = 0; j < arr.length; j++) {
        if (arr[minIndex] > arr[j]) {
            minIndex = j;
        }
    }

    return minIndex;
}

// function selectionSort(arr) {
//     for (let i = 0; i < arr.length; ++i) {
//         let minIndex = i;

//         for( let j = i + 1; i < arr.length; ++j) {
//             if (arr[minIndex] > arr[j]) {
//                 minIndex = j;
//             }
//         }

//         swap(arr, i, minIndex);
//     }

//     return arr;
// }
// why wasn't this working?

function selectionSort(arr) {
    for (let i = 0; i < arr.length; ++i) {
        let minIndex = i;

        for (let j = i + 1; j < arr.length; ++j) {
            if (arr[minIndex] > arr[j]) {
                minIndex = j;
            }
        }

        swap(arr, i, minIndex);
    }
    return arr;
}

function insertionSort(arr) {
    for (let i = 1; i < arr.length; ++i) {
        let currElement = arr[i];
        for (var j = i - 1; j >= 0 && currElement < arr[j]; --j) {
            arr[j + 1] = arr[j];
        }
        arr[j + 1] = currElement;
    }
    return arr;
}


//does the --j still decrement j at the end of inner loop before line 110?
//YES

function transpose(arr) {
    let rows = arr.length;
    let cols = arr[0].length;
    let grid = [];

    for (let i = 0; i < cols; ++i) {
        grid[i] = new Array(rows);
    };

    for (let i = 0; i < rows; ++i) {
        for (let j = 0; j < cols; ++j) {
            grid[j][i] = arr[i][j];
        };
    };

    return grid;
};

function revStr(str) {
    let i = 0, j = str.length - 1;

    for(let n = 0; n < str.length/2; ++n) {
        let temp = str[j];
        str[j] = str[i];
        str[i] = temp;
        ++ i;
        -- j;
    };

    return str;
};

let revStr = str => {

    for (let i = 0, j = str.length - 1; i < j; ++i, --j) {
        let temp = str[j];
        str[j] = str[i];
        str[i] = temp;
    };
};

function twoNumberSum(array, targetSum) {
    let diff = {};

    for (let i = 0; i < array.length; ++i) {
        if (targetSum - array[i] in diff) return [targetSum - array[i], diff[targetSum - array[i]]];
        diff[array[i]] = targetSum - array[i];
    };
    // Write your code here.
    return [];
};