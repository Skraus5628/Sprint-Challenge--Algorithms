#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    This RTComplexity is O(n): With each iteration of the while loop, 'a' increases by 'n * n', so after 'n' iterations 'a' will be equal to 'n * (n * n)' which matches the while loop's conditional check of 'a < n * n * n'!

b)
    The RTComplexity is O(n*log(n)) -> because there are nested loops: the outer 'for' loop will run 'n' times, and the inner 'while' loop will run log(n) times. The inner loop has a log(n) time complexity because the value of 'j' doubles with each iteration, so 'j' will increase quadradically and only take log(n) iterations to reach the value of 'n'.

c)
    This RTComplexity is O(n). This is because the function is recursive and will call itself 'n' times. When it hits its base case, the function will backtrack through all 'n' function calls, adding '2' to the return value each time. Since adding '2' to another value is a constant time operation, and it is done 'n' times, the final runtime complexity is O(n).


## Exercise II

    The building can be seen like an array of floors. Because the floors of any building are sorted by height, then in our analogy we can say the array is sorted in ascending order (i.e. lowest floor is at the bottom and highest floor on top!). Given a sorted array, we can use a binary search approach to find efficiently find a specific floor. This would mean first going to the middle floor and dropping an egg.
    --> If the egg breaks, you can ignore the top half of floors and go down to the middle of the bottom half of floors
    --> If the egg didn't break when dropped it from the middle floor, then you would go up to the middle of top half of floors.

    -- You won't know which floor is the highest (non-breaking) floor (i.e. floor 'f') unless you test two consecutive floors resulting in one intact egg and one broken egg so you will need to continue this binary search pattern all the way to the end (or log(n) times) 
    --> so that your last floor change will either be going down one floor (if your second-to-last drop resulted in a broken egg) 
    --> or up one floor (if your second-to-last drop resulted in an intact egg). 
     -- In either of the two previous scenarious, your last drop will guarantee that you have dropped an egg from floor 'f-1' AND from floor 'f'.


    Using a binary search approach, it will always take log(n) egg drops in order to find floor 'f'.