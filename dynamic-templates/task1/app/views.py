from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    list_inflation = []
    list_context_year_and_summa = []
    with open('inflation_russia.csv', encoding='utf-8', newline='\n') as csvfile:
        csvfile.readline()
        inflation = csv.reader(csvfile, delimiter=';')
        for row in inflation:
            list_month = []
            list_month.append(row[0])
            for elem_row in row[1:-1]:
                if elem_row != '':
                    str_to_float = float(elem_row)
                    list_month.append(str_to_float)
                else:
                    list_month.append('-')
            list_month.append(row[-1])
            list_inflation.append(list_month)
    return render(request, template_name,
                  context ={'table_inflation':list_inflation})