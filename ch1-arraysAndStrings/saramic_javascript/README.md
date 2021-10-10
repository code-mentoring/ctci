# JS solution

```
make
```

_see at the end to what this will output_

OR

```
# install dependancies
npm install       # or make install

# run tests
npm test          # or make test

# run tests in watch mode whilst coding
npm run watch     # or make watch

# run code
npm run examples
# or
node index.js
```

## install node

assuming you have a modern node js environment installed 

```
node -v
v14.17.6
```

if you have [asdf](https://asdf-vm.com/) you can use `adsf install`

## output of make

if you run

```
make
```

it install node, run all the tests and run some examples with the output of

```
make
npm install

audited 327 packages in 1.841s

found 0 vulnerabilities

npm test

> jest

 PASS  ./eg_1_7_rotateMatrix.spec.js
 PASS  ./eg_1_6_stringCompression.spec.js
 PASS  ./eg_1_4_palindromePermutation.spec.js
 PASS  ./eg_1_1_isUnique.spec.js
 PASS  ./eg_1_8_zeroMatrix.spec.js
 PASS  ./eg_1_2_checkPermutation.spec.js

Test Suites: 6 passed, 6 total
Tests:       44 passed, 44 total
Snapshots:   0 total
Time:        0.372 s, estimated 1 s
Ran all test suites.
npm run examples

> node index.js

Session 1.1 - isUnique
input:  ""                   isUnique:  true
input:  "abc"                isUnique:  true
input:  "aabc"               isUnique:  false
input:  "\t\t"               isUnique:  false
input:  "😀😀"               isUnique:  false
input:  "😀🙁"               isUnique:  true

Session 1.2 - checkPermutation
input:  ["asdf","fdsa"]      checkPermutation:  true
input:  ["sarah","michael"]  checkPermutation:  false
input:  ["god","dog"]        checkPermutation:  true
input:  [1234,4321]          checkPermutation:  true
input:  [null,null]          checkPermutation:  true
input:  [null,null]          checkPermutation:  false

Session 1.4 - palindromePermutation
input:  "code"               palindromePermutation:  false
input:  "aab"                palindromePermutation:  true
input:  "carerac"            palindromePermutation:  true
input:  "Borrow or rob"      palindromePermutation:  true
input:  123454321            palindromePermutation:  true
input:  "!@#$%^&*()"         palindromePermutation:  false
input:  null                 palindromePermutation:  false

Session 1.6 - stringCompression
input:  "aabcccccaaa"        stringCompression:  "a2b1c5a3"
input:  "aabbcc"             stringCompression:  "aabbcc"
input:  "aaaaaaaaaaaaaaa"    stringCompression:  "a15"

Session 1.7 - rotateMatrix
input:  [
  1,2,3
  4,5,6
  7,8,9
]
output:  [
  7,4,1
  8,5,2
  9,6,3
]

input:  [
  1,2,3
  4,5,6
]
output:  [
  4,1
  5,2
  6,3
]

rotate matrix in place
[
  1,2,3
  4,5,6
  7,8,9
]
[
  7,4,1
  8,5,2
  9,6,3
]
[
  0,1,2,3,4
  1,2,3,4,5
  2,3,4,5,6
  3,4,5,6,7
  4,5,6,7,8
]
[
  4,3,2,1,0
  5,4,3,2,1
  6,5,4,3,2
  7,6,5,4,3
  8,7,6,5,4
]

Session 1.8 - zeroMatrix
[
  1,1,1,1,1
  1,0,1,1,1
  1,1,1,1,1
  1,0,1,0,1
  1,1,1,1,1
]
[
  1,0,1,0,1
  0,0,0,0,0
  1,0,1,0,1
  0,0,0,0,0
  1,0,1,0,1
]
```

