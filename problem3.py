"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []
    while True:
        # TODO: Get input from user
        # TODO: Check if user typed 'done'
        # TODO: Try to convert to float and add to list
        # TODO: Handle invalid input gracefully
        raw = input("Give some integers (when you are finished, type 'done'): ")
        s = raw.strip()
        s_norm = s.strip("'\'").lower()

        if s_norm == "done": 
            break

        try : 
            numbers.append(int(s))
        except ValueError : 
            print("Not an integer. Enter an integer, or 'done'")
        pass

    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    analysis = {}

    # TODO: Calculate count
    # TODO: Calculate sum
    # TODO: Calculate average
    # TODO: Find minimum
    # TODO: Find maximum
    # TODO: Count even numbers (hint: use modulo operator)
    # TODO: Count odd numbers
    count = numbers.len()
    sum = numbers.sum()
    average = numbers.average()
    minimum = numbers.minimum()
    maximum = numbers.maximum()
    even = 0
    odd = 0
    for num in numbers: 
        if num % 2 == 0 :
            even += 1
        else : 
            odd += 1
    analysis['count'] = count
    analysis['sum'] = sum
    analysis['average'] = average
    analysis['minimum'] = minimum
    analysis['maximum'] = maximum
    analysis['even'] = even
    analysis['odd'] = odd
    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)

    # TODO: Display all analysis results in a nice format
    # Example:
    # Count: 5
    # Sum: 25
    # Average: 5.00
    # etc.

    for k, v in analysis.items():
        print(k, " : ", v)
    pass


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()