## Program Skills
* Practice using lists of iterables
* Practice using dictionaries
* Practice using the random module

## Summary

For the past few years, the ideas of diversity and inclusion have been marketed to companies as a tool to enhance team performance. The benefits of establishing and encouraging a diverse workplace help both the individuals as well as the company. 

Unfortunately, unconscious and unintentional biases can lead some people to be hired and/or promoted more frequently than others. Though these very small biases seem insignificant, the cumulative effects within a larger system can be harmful.

In this program, I will be modeling the impacts of implicit biases within a company. Most employees would not consider themselves to be discriminatory, yet companies today still lack diverse work environments (check out Google’s diversity statistics). This is due to the fact that people have unintentional biases that can affect their treatment of others, whether they realize it or not.

## Program Structured

1. **create_employee()** - returns a dictionary representing one new randomly generated employee.
2. **create_company(sizes)** - takes in a list of the number of employees at each level and returns a list of those levels, each of which is a list of randomly generated employee dictionaries.
3. **get_pct_favored(company, level)** - takes in a company list and a level to examine, and returns the percent of "favored" employees at that level.
4. **turnover(company, sizes, pct)** - takes in a company list, the sizes list (as in function 2), and a float representing the percent of employees leaving the company, and modifies the company list in place to simulate hiring and promotions.
5. **main(num_simulations, sizes, pct)** - takes in the number of simulations to run, a list of company sizes (for function 2), and a percent of turnover (for function 4), and prints the average percent of "favored" employees at each level over all simulations.
