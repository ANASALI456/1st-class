# customer
customer={
    "name":"anas ali",
    "age":"20",
    "college":"ARGC",
    "CLASS":"SECOUNDAIRE"
}
print(customer)
customer_list={
    "name":["uzair","fahad","ali"],
    "age":[25,36,55,89,41]
}
print(customer_list),
for x in range(len(customer_list["name"])):
    print(f"{customer_list["name"][x]}{customer_list["age"][x]}")
    