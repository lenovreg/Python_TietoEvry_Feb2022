# 3. City Population
# The city has a known population p0
# A percentage of population perc is added each year
# Every year a certain number of delta also arrive (or leave)
# We need to know when (if at all) the city will reach a population of p
# Write a function get_city_year (p0, perc, delta, p) that returns the years (full) when p is reached.
# If p cannot be reached, then we return -1
# Example:
# get_city_year (1000,2,50,1200) -> 3
# 1000 + 1000 * 0.02 + 50 => 1070 after the 1st year
# 1070 + 1070 * 0.02 + 50 => 1141 after the 2nd year
# 1141 + 1141 * 0.02 + 50 => 1213 after the 3rd year
# so the function here returns 3 and is done
# PS. Note that we give perc as a percentage to be converted to a decimal number.
# More test examples:
# get_city_year (1000, 2, -50, 5000) -> -1
# get_city_year (1500, 5, 100, 5000) -> 15
# get_city_year (1500000, 2.5, 10000, 2,000,000) -> 10


#p0
#percentage per year
#delta
#population to reach == p
def get_city_year(p0, perc, delta, p):
    # get_city_year (1000,2,50,1200) -> 3
    years_count=0
    reaching_p = 0
    p0 = round(p0)
    while True:
        reaching_p+= p0 + (p0*perc*0.01) + delta
        years_count+=1
        #print('reaching_p ', reaching_p)
        if reaching_p < p0 or reaching_p < 0:
            years_count = - 1
            break
        elif reaching_p >= p:
            break
        else:
            continue
    return round(reaching_p),years_count # should never get here


p0 = float(input('Input population: '))
perc = float(input('Input percentage per year: '))
delta=float(input('Input delta: '))
p=float(input('Input population to reach: '))
years=0
population=0
print(f'Population now: {p0}, percentage per year: {perc}, delta: {delta}, population to reach for: {p}')
population,years=get_city_year(p0,perc,delta,p)
print(f'{round(p0)}+{round(p0)}*{perc}*0.01+{round(delta)} = {population} will be reached after {years} years')