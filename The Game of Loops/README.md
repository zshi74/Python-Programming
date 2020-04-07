## Program Skills

* Creating and using while loops
* Practice with conditionals and functions

## Summary

In the Free city of Braavos lies the Iron Bank. Legend has it that it is a bank unlike any other. You can't run from them, you can't cheat them, you can't sway them with excuses. Queen Daenerys wants to open an account in the Iron Bank. The Lords of the Iron Bank ask her to set a password that cannot be broken. They have some strange criteria for the password, which must be met:

1. No letters should repeat.
2. The number of vowels should not be odd.
3. At least one special character from the set {@, #, *, $} must be present.
4. The only numbers allowed are those divisible by either 2 or 3.

The Iron Bank needs help in verifying if the password set by the queen is valid. Please help the Lords of the Iron Bank design a program that performs this check

## Program Structure

1. **has_unique_letters(pw_1)** - checks each letter to ensure that it is unique; returns True if all letters are unique and False if there are any repeats.
2. **has_even_vowels(pw_2)** - checks the number of vowels in the password; returns True if the number of vowels is 0 or even, False if the number of vowels is odd.
3. **has_special_character(pw_3)** - checks whether the password contains at least one character from the set {@, #, *, $}; returns True if there is one and False if there is not.
4. **has_divisible_numbers(pw_4)** - checks whether any numbers 0-9 in the password are divisible by 2 or 3; returns True if all numbers are and False if any number is not.

Note that all of these functions return either True or False. Do not call print at any time in any of these functions.

In addition to these functions, you must also include a **check_password(pw_5)** function as detailed below, which should begin running when we run your program (so: call it). You do NOT need to include any OTHER function calls in your submission, though we recommend testing your program thoroughly.
