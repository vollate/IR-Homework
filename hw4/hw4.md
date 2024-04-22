# Homework 4
![sample](https://cs.stanford.edu/people/karpathy/reinforcejs/gridworld_dp.html)

>12111224  
>贾禹帆

## Q1

### value iteration

>gamma = 1

- iteration 0:

|0|0|0|
|-|-|-|
|0|0|0|
|0|0|0|

- iteration 1:

|-1|-1|0|
|-|-|-|
|-1|-1|-1|
|-1|-1|-1|

- iteration 2:

|-2|-1|0|
|-|-|-|
|-2|-2|-1|
|-2|-2|-2|

### policy iteration

>gamma = 1

- iteration 0:

|0|0|0|
|-|-|-|
|0|0|0|
|0|0|0|

- iteration 1:

|-1|-1|0|
|-|-|-|
|-1|-1|-1|
|-1|-1|-1|

- iteration 2:

|-2|-1.75|0|
|-|-|-|
|-2|-2|-1.75|
|-2|-2|-2|

## Q2

### value iteration

>gamma = 1

- iteration 0:

|0|0|0|
|-|-|-|
|0|0|0|
|0|0|0|

- iteration 1:

|-0.1|-0.1|0|
|-|-|-|
|-0.1|-1|-0.1|
|-0.1|-0.1|-0.1|

- iteration 2:

|-0.2|-0.1|0|
|-|-|-|
|-0.2|-1.1|-0.1|
|-0.2|-0.2|-0.2|

### policy iteration

>gamma = 1

- iteration 0:

|0|0|0|
|-|-|-|
|0|0|0|
|0|0|0|

- iteration 1:

|-0.1|-0.1|0|
|-|-|-|
|-0.1|-1|-0.1|
|-0.1|-0.1|-0.1|

- iteration 2:

|-0.2|-0.4|0|
|-|-|-|
|-0.425|-1.1|-0.4|
|-0.2|-0.425|-0.2|
