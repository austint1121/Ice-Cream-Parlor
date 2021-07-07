
# Ice Cream Parlor

Practice Project source: https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream. On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.

Given the value of  and the  of each flavor for  trips to the Ice Cream Parlor, help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of money during each visit. ID numbers are the 1- based index number associated with a . For each trip to the parlor, print the ID numbers for the two types of ice cream that Sunny and Johnny purchase as two space-separated integers on a new line. You must print the smaller ID first and the larger ID second.

# Note:

Two ice creams having unique IDs  and  may have the same cost (i.e., ).
There will always be a unique solution.


# Function Description

whatFlavors has the following parameter(s):

int cost[n] the prices for each flavor
int money: the amount of money they have to spend
Prints

int int: the indices of the two flavors they will purchase as two space-separated integers on a line
Input Format

The first line contains an integer, "t" , the number of trips to the ice cream parlor.

Each of the next 3 sets of "t" lines is as follows:

The first line contains "money" 
The second line contains an integer,"n", the size of the array cost .
The third line contains "n" space-separated integers denoting the "cost[i]".
Constraints

