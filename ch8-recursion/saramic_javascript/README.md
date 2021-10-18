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

following install, test and demo output will be printed

```
make
npm install

audited 327 packages in 1.846s

npm test

> jest

 PASS  ./ch8Recursion.spec.js
  magicIndex
    ✓ returns undefined if there is no magic index (1 ms)
    ✓ returns the magic index
    ✓ returns one of the magic indices
    a large enough input array
      ✓ find the magic index in FAST O(log(n)) time (21 ticks) (73 ms)
      ✓ find the magic index in SLOW O(n) time (10,0001 ticks) (1 ms)

Test Suites: 1 passed, 1 total
Tests:       5 passed, 5 total
Snapshots:   0 total
Time:        0.735 s, estimated 1 s
Ran all test suites.
npm run examples

> node index.js

8.1: Triple Step
TODO ...

8.2: Robot in a Grid
TODO ...

8.3: Magic Index
input:  [-1,0,2,35]                    magicIndex:  2
input:  [1,2,3,4,5]                    magicIndex:  1
input:  [-1,0,1,2,3,4,5,6,7,9,11]      magicIndex:  9
                   BASIC Performed in: 10  iterations
               RECURSIVE Performed in:  1  iterations

8.4: Power Set
TODO ...
```

