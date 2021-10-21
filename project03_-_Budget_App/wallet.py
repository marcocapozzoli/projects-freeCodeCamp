from budget import Category

food = Category('Food')
entertainment = Category('Entertainment')
business = Category('Business')

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")

food.withdraw(100)
food.withdraw(200)
entertainment.withdraw(33.40)
business.withdraw(10.99)


# Print status
def create_spend_chart(args):
    
    areas = args
    
    # Calculation of expenses by category
    expenses_by_category = []
    for category in range(len(areas)):
        summation = 0
        for item in areas[category].ledger:
            if item['amount'] < 0:
                summation += item['amount']
        expenses_by_category.append(summation)

    expenses_total = sum(expenses_by_category)


    # Percentage expenses
    expenses_by_category_percent = []
    for expense in expenses_by_category:
        expenses_by_category_percent.append(round(expense / expenses_total * 10) * 10)

    # Generate the graph
    graph = ""
    graph += "Percentage spent by category\n"
    for value in reversed(range(0, 101, 10)):
        graph += str(value).rjust(3) + '|'
        for expense in expenses_by_category_percent:
            if value <= expense:
                graph += ' o '
            else:
                graph += '   '       
        graph += ' \n'
    graph += "    " + (("-" * 3 * len(areas)) + "-")  + "\n" + " " * 5

    # Biggest category name
    letter_count = []
    for area in areas:
        letter_count.append(len(area.category))
    max_letter = max(letter_count)
    
    # Name of categories on chart
    for i in range(max_letter):
        for area in areas:
            try:
                graph += area.category[i] + "  "
            except IndexError:
                graph += "   "
        graph += "\n" + " " * 5         

    return graph
        
            
if __name__ == "__main__":
    create_spend_chart([business, food, entertainment])
