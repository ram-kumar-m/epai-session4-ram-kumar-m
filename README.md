# Qualeans 

Qualeans are proprietary representations of the state of a quark. which exist in states [1, 0, -1] or as we like to call them [exist, doesn't exist, maybe_exists]

> [1, 0, -1] ->  [exist, doesn't exist, maybe_exists]

The internal representations of these quirky particleas are as follows.

1. User inputs a state from the available list of states [0, 1, -1] 
2. User input is multiplied with a uniform distibution with central limit of 0 rounded off to 10 digits of precision using Bankers's Roudind off.
   ``` python
   random.uniform(-1,1)
   ```
The initilization of the qualiean can be done in 2 ways:

1. ``` python
   Qualean(0), Qualean(1) or Qualean(-1) 
   ```
2. ``` python 
   Qualean(qual= Decimal(number))
   ```

>Note: During this second method, The representation of the Qualean datatype will show it as 'Derieved'.

The first method initialieses with user input.
While the second method gives the user the ability to initialise a qualean with a pre-calculated internal value.

> The Qualean class uses the Decimal data type to store numbers internally.
``` python
from decimal import Decimal
```

## Inbuilt methods

The Qualiean data type has some very useful inbuilt methods, Some of which are described below.
> These methods can be invoked as follows:
 ``` python
 q = Qualean(0)
 q.___bool__()

 False
 ```

1. ### __repr__
   This function will return represenational info pertaining to the Qualean.
   ```python 
   q = Qualean(1)
   Qualean((1, 0.0587677418068242030102510398137383162975311279296875) -> 0.0587677418)
   ```
   where the three values are respectively the user_input, the value from the uniform distribution and the final internal value stored.

2. ### __str__
    Gives an more user friendly output for the print function.
    ``` python
    This is an object of type Qualean with internal val 0.0587677418
    ```
3. ### __eq__
   Checks if two qualeans are equal by checking their internal values by using '=' in python.  

4. ### __add__
   Allows the use of the internal '+' operator to add two qualeans.

5. ### __mul__
   Allows the use of the internal '*' operator for the multiplication between qualeans and scalar with a qualean.
   > This follows the rule q + q + q = q * 3.

   > The internal mutiplication returns a Qualean with a value equal to the dot product of the values of the other qualeans.

6. ### __sqrt__
   This function implements the Decimal.sqrt() if the root is real and cmath.sqrt() if the root is imaginary and gives the reult in the 'Decimal' and 'Complex' datatypes respectively.

7. ### Comparison operators: >, >=, < and <= 
   This implements the internal `__gt__`, `__ge__` and `__lt__`, `__le__`. Which allows simple > , >= , < and <= operations of qualeans using their internal stored values respectively.

8. ### __bool__
   This operation retruns `False` if the internal value of the is `0 or None` else it returns `True`.
   > This allows qualeans to be used more pythonically with if statements, like 
   ``` python
   if q:
       do_something()
    ```
9. ### __invertsign__
   The Function `q.__invertsign__()` will return a new qualean whole internal value inverted.

10. ### __float__ 
    This function returns the internal value of the qualean as `float`.

11. ### __and__, __or__
    The deafult pythonic `and, or` operations are implemented such that
    * q1 and q2 returns False when q2 is not defined as well and q1 is False
    * q1 or q2 returns True when q2 is not defined as well and q1 is not false
    > This allows logical operations `and, or `directly in python like 
    ```python
    p or q 
    p and q   
    ```

## Test Cases (using __Pytest__)
1. ### test_readme_exists
   Checks if there is a README.md file in the same folder.

2. ### test_readme_contents
   Checks if the README.md file has alteast 500 words.

3. ### test_readme_proper_description
   Checks if the required functions are present in the README.md file.

4. ### test_readme_file_for_formatting
   Checks if there are adequete headings present in the README.md file.

5. ### test_indentations
   Checks if proper indentations are present throughout the python file.
   using the rule of 4 spaces equals 1 Tab.

6. ### test_function_name_had_cap_letter
   Checks if any one the functions have capital letters used in their names, which breaks the PEP8 conventions.

7. ### test_repr
   Checks if the `__repr__` method exits for the class, and displays relevant information.

8. ### test_str
   Checks if the `__str__` methods exists so that the datatype can be printed properly,

10. ### test_add_two_qualeans
    Checks if we can safely and properly add two qualeans.

11. ### test_cant_add_num_with_qualeans
    Ensures qualeans can only be added with qualeans and nothing else.

12. ### test_qualean_class_exists_for_states
    Ensures that allowed inputs of [0, 1, -1] can have their own qualean objects.

13. ### test_for_invalid_inputs
    Checks if invalid inputs, values other than 0, -1, 1 raises a `ValueError`.

14. ### test_for_derieved_datatype
    Checks if the qualean obtained by doing a binary operation on two qualeans has a field with value 'Derieved', letting us know the qualean so formed was not formed with user input.

15. ### test_scalar_multiplication_by_100
    Checks for scalar multiplicaton of qualeans with numbers.
    In this case <br> `if q + q + q ... 100 times = 100 * q`.
   
16. ### test_for_eq
    Checks for the equality operation of qualeans. namely <br>
    `if q1 == q2`.
   
17. ### test_for_decimal_sqrt
    Checks if the inbulit `sqrt` method gives the same value as the `Decimal.sqrt` method.

18. ### test_central_limit_theorum
    Checks if sum of 1 million different qs is very close to zero (using the `isclose` method).

19. ### test_qualean_multiplication
    Checks if qualean mutiplication is executed as desired.

20. ### test_gt
    Checks the grater than operator (`>`)

20. ### test_ge
    Checks the grater than or equal to operator (`>=`)

20. ### test_lt
    Checks the less than operator (`<`)

20. ### test_le
    Checks the less than or equal to operator (`<=`)

23. ### test_bool
    Checks if bool method returns `True or False` as required.
   
24. ### test_invertsign
    Checks if the `__invertsign__` function yields a new qualean with internal value mutiplied by -1.

25. ### test_float_constructor
    Checks if the float constrctor yields a float value from the Qualean Class.

26. ### test_and
    Checks if `and` operator works, hence can be used for shortcirtuiting.

26. ### test_or
    Checks if `or` operator works, hence can be used for shortcirtuiting.