> In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!

Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:

- dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
- percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
Assume that the user will input values in the expected formats.


<details>
<summmary>Hint</summary>
- Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
- Recall that float can convert a str to a float, per docs.python.org/3/library/functions.html#float.
- Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.


</detauks>
