import mh_z19, schedule, time
def print_co2():
    print(mh_z19.read())

schedule.every().minute.do(print_co2)

while True:
    schedule.run_pending()
    time.sleep(1)
