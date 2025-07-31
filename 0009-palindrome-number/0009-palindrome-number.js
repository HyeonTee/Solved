/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0) return false
    const numList = []
    while (x !== 0) {
        numList.push(x % 10)
        x = Math.floor(x / 10)
    }

    for (let i = 0; i < numList.length; i++) {
        if (numList[i] !== numList[numList.length - i - 1]) {
            return false
        }
    }

    return true
};