# What is the time complexity, and more importantly why?
Graham O(n log n) timsort is used and that is what longest time

# Why should the α and β comparisons with γ be done in a specific order (depending on which of the four cases you have)?

# What happens if an α or β is infinity? Is that a valid numerical value in the language you use?

# How is % computed in the language you use? Is it guaranteed to be non-negative? That is not the case for ISO C, at least (but the sign is specified identically for C and C++). The reason we have this question is that most programmers sooner or later will experience an unpleasant surprise if they have not thought about this. Note that the pseudo code should work for any language.
In python the resulting sign will always be the same as the denominator. Algorithm D from Knuth's 'The Art of Computer Programming

# Would it be easier to parallellize Graham scan or Preparata-Hong?
preparata-hong, since the task is divided, into multiple problems. But that is just a premonition
