country_file_name = "country_data.txt"
countries = {}
with open(country_file_name) as country_file:
     for row in country_file:
         field = row.rstrip().split(";")
         country_code, country_name, capital, total_area, \ 
             population, currency_code, currency_name, lang_name = fields
        #  print(country_code, country_name, capital, total_area,
        # population, currency_code, currency_name, lang_name, sep="\n\t")
    countries[country_code] ={
        "code": country_code,
        "capital": capital,
        "area": total_area,
        "population": population,
        "currency": currency_name,
        "currency_code": currency_code,
        "language": lang_name
    } 
  
    print(countries)
