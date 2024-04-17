# create variables that represent running, swimming and cycling times (in minutes)
run_t = float(input("Running time (in minutes): "))
swim_t = float(input("Swimming time (in minutes): "))
cycle_t = float(input("Cycling time (in minutes): "))

# create and display variable representing the total time 
total_t = run_t + swim_t + cycle_t
print("Your total time is: " + str(total_t) + " minutes")

# create elif statement distributing awards based on total time 
if total_t  <= 100.0:
        print ("Congratulations! You have an received a Provincial Colours Award.")
elif (total_t <= 105.0) and (total_t > 100.0) :
        print ("Congratulations! You have an received a Provincial Half Colours Award.")
elif (total_t <= 110.0) and (total_t > 105.0) :
        print ("Congratulations! You have an received a Provincial Scroll.")
else: 
        print("Unfortunately your total time has exceeded the qualifying time by more than 10 minutes, no award will be given on this occasion.")

