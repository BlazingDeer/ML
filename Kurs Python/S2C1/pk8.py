projects=["Brexit","Nord Stream","US Mexico Border"]
leaders= [ "Theresa May","Wladimir Putin", "Donald Trump and Bill Clinton"]

for project,leader in zip(projects,leaders):
    print(project,leader,sep=" - ")

dates=['2016-06-23', '2016-08-29', '1994-01-01']

for i,(project,data_projektu,leader) in enumerate(zip(projects,dates,leaders)):
    print(i,"- The leader of",project,"started",data_projektu,"is",leader)