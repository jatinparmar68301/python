# write a program to findout countries whose area is greater given area. use chatgpt to create dictionaries which country name as key and its' area as value.
country_area = {
    "Russia": 17098242,
    "Canada": 9984670,
    "China": 9596961,
    "United States": 9372610,
    "Brazil": 8515767,
    "Australia": 7692024,
    "India": 3287263,
    "Argentina": 2780400,
    "Kazakhstan": 2724900,
    "Algeria": 2381741
}
given_area = int(input("Enter the area in square kilometers: "))
print(f"Countries with area greater than {given_area} sq km:")
for country in country_area:
    if country_area[country] > given_area:
        print(f"{country}: {country_area[country]} sq km")

