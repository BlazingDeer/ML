def calculate_paint(efficency_ltr_per_m2,*surfaces):
    powierzchnia=sum(surfaces)
    return powierzchnia*efficency_ltr_per_m2

print(calculate_paint(0.5,10,15,5,20))

powierzchnie=[1,2,3,4,5,10,15]
print(calculate_paint(0.5,*powierzchnie))

def log_it(*args):
    with open("log_it.txt","a") as f:
        for arg in args:
            f.write(arg+" ")
        f.write("\n")

log_it("starting processing forecasting")
log_it("Error","Not enouhg data","invoices","2020")
