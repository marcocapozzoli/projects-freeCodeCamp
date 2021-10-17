from budget import Category

food = Category('Food')
clothing = Category('Clothing')
entertainment = Category('Entertainment')
school = Category('School')

food.deposit(5000)
food.withdraw(20)

entertainment.deposit(5000)
entertainment.withdraw(1000)

clothing.deposit(5000)
clothing.withdraw(100)

school.deposit(5000)
school.withdraw(300)


# Print status
def create_spend_chart(*args):
    
    areas = args

    # Cálculo de gastos por categoria
    expenses_by_category = []
    for category in range(len(areas)):
        summation = 0
        for item in areas[category].ledger:
            if item['amount'] < 0:
                    summation += item['amount']
        expenses_by_category.append(summation)

    expenses_total = sum(expenses_by_category)

    # Gastos em porcentagem
    expenses_by_category_percent = []
    for expense in expenses_by_category:
        expenses_by_category_percent.append(round(expense/expenses_total*10)*10)
    
    # Gera o gráfico
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
    graph += "    " + ("-" * 3 * len(areas)) + "\n" + " "*5

    # Maior nome das categorias
    letter_count = []
    for area in areas:
        letter_count.append(len(area.category))
    max_letter = max(letter_count)
    
    # Nome das categorias no gráfico
    for i in range(max_letter):
        for area in areas:
            try:
                graph += area.category[i] + "  "
            except IndexError:
                graph += "   "
        graph += "\n" + " "*5         

    return(graph)    
        
            
            
create_spend_chart(clothing, entertainment, school, food)



