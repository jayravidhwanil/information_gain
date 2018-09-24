import csv
import math
training_data = 'Car_test.csv'
import pandas
Dataread = pandas.read_csv(training_data)
accepted = ['acc', 'vgood']
rejected = ['unacc', 'good']
Training_frame = pandas.DataFrame(Dataread)
Training_frame.head()
#totalentities=Training_frame.loc[(Training_frame['class_label'].isin(accepted))or Training_frame['class_label'].isin(rejected)]
total_count= len(Training_frame.index)
positives=Training_frame.loc[Training_frame['class_label'].isin(accepted)]
positives_count= len(positives.index)
negatives=Training_frame.loc[Training_frame['class_label'].isin(rejected)]
negatives_count= len(negatives.index)
#print(Dataread.info())
#Dataread=csv.reader(training_data, delimiter=',',skipinitialspace=True)
def entropy(Y,N):
    entropy_value=0
    total=0
    total=Y+N
    if Y!= 0 and N!=0:
        entropy_value=-(Y/total*math.log(Y/total,2))-(N/total*math.log(N/total,2))
    elif Y!=0 and N==0:
        entropy_value = -(Y / total * math.log(Y / total, 2))
    elif N!=0 and Y==0:
        entropy_value = -(N/total*math.log(N/total,2))
    else:
        entropy_value = 0
    return entropy_value
total_info=entropy(positives_count,negatives_count)
def information_gain():
    buying_possible_list = ["vhigh", "high", "med", "low"]
    maint_possible_list = ["vhigh", "high", "med", "low"]
    doors_possible_list = ["2", "3", "4", "5more"]
    persons_possible_list = ["2", "4", "more"]
    lug_boot_possible_list = ["small", "med", "big"]
    safety_possible_list = ["low", "med", "high"]
    # buying_training_list = Dataread['buying'].unique().tolist()
    # buying_training_list_value = len(buying_training_list)
    # buying_possible_value = len(buying_possible_list)
    # print("buying_possible_list",buying_possible_list)
    # print("buying_possible_value",buying_possible_value)
    # print("buying_training_list",buying_training_list)
    # print("buying_taiining_list_value",buying_training_list_value)
    # maint_training_list = Dataread['maint'].unique().tolist()
    # maint_training_list_value = len(maint_training_list)
    # maint_possible_value = len(maint_possible_list)
    # print("maint_possible_list",maint_possible_list)
    # print("maint_possible_value",maint_possible_value)
    # print("maint_training_list",maint_training_list)
    # print("maint_training_list_value",maint_training_list_value)
    # doors_training_list = Dataread['doors'].unique().tolist()
    # doors_training_list_value = len(doors_training_list)
    # doors_possible_value = len(doors_possible_list)
    # print("doors_possible_list",doors_possible_list)
    # print("doors_possible_value",doors_possible_value)
    # print("doors_training_list",doors_training_list)
    # print("doors_training_list_value",doors_training_list_value)
    # persons_training_list = Dataread['persons'].unique().tolist()
    # persons_training_list_value = len(persons_training_list)
    # persons_possible_value = len(persons_possible_list)
    # print("persons_possible_list",persons_possible_list)
    # print("persons_possible_value",persons_possible_value)
    # print("persons_training_list",persons_training_list)
    # print("persons_training_list_value",persons_training_list_value)
    # lug_boot_training_list = Dataread['lug_boot'].unique().tolist()
    # lug_boot_training_list_value = len(lug_boot_training_list)
    # lug_boot_possible_value = len(lug_boot_possible_list)
    # print("lug_boot_possible_list",lug_boot_possible_list)
    # print("lug_boot_possible_value",lug_boot_possible_value)
    # print("lug_boot_training_list",lug_boot_training_list)
    # print("lug_boot_training_list_value",lug_boot_training_list_value)
    # safety_training_list = Dataread['safety'].unique().tolist()
    # safety_training_list_value = len(safety_training_list)
    # safety_possible_value = len(safety_possible_list)
    # print("safety_possible_list",safety_possible_list)
    # print("safety_possible_value",safety_possible_value)
    # print("safety_training_list",safety_training_list)
    # print("safety_training_list_value",safety_training_list_value)
    #attribute1 - 'buying' fractions calculation
    buying_fractions_accepted=[0,0,0,0]
    buying_fractions_rejected=[0,0,0,0]
    buying_present_list=[0,0,0,0]
    info_buying = 0
    for i in range(0,4):
        buying_fractions_accepted[i] = Training_frame.loc[(Training_frame['buying'] == buying_possible_list[i]) & Training_frame['class_label'].isin(accepted)]
        buying_fractions_rejected[i]= Training_frame.loc[(Training_frame['buying'] == buying_possible_list[i]) & Training_frame['class_label'].isin(rejected)]
        buying_present_list[i] = Training_frame.loc[(Training_frame['buying'] == buying_possible_list[i])]
        #print(len(buying_fractions_accepted[i].index))
        #print(len(buying_fractions_rejected[i].index))
        info_buying+=float(len(buying_present_list[i].index)/total_count*entropy(len(buying_fractions_accepted[i].index),len(buying_fractions_rejected[i].index)))
    info_gain_buying=total_info-info_buying
    print(info_gain_buying)
    #attribute2 - 'maint' fractions calculation
    maint_fractions_accepted=[0,0,0,0]
    maint_fractions_rejected=[0,0,0,0]
    maint_present_list=[0,0,0,0]
    info_maint = 0
    for i in range(0,4):
        maint_fractions_accepted[i] = Training_frame.loc[(Training_frame['maint'] == maint_possible_list[i]) & Training_frame['class_label'].isin(accepted)]
        maint_fractions_rejected[i] = Training_frame.loc[(Training_frame['maint'] == maint_possible_list[i]) & Training_frame['class_label'].isin(rejected)]
        maint_present_list[i]= Training_frame.loc[(Training_frame['maint'] == maint_possible_list[i])]
        #print(len(maint_fractions_accepted[i].index))
        #print(len(maint_fractions_rejected[i].index))
        info_maint+=float(len(maint_present_list[i].index)/total_count*entropy(len(maint_fractions_accepted[i].index), len(maint_fractions_rejected[i].index)))
    info_gain_maint= total_info-info_maint
    print(info_gain_maint)
    doors_fractions_accepted=[0,0,0,0]
    doors_fractions_rejected=[0,0,0,0]
    doors_present_list=[0,0,0,0]
    info_doors = 0
    for i in range(0,4):
        doors_fractions_accepted[i] = Training_frame.loc[(Training_frame['doors'] == doors_possible_list[i]) & Training_frame['class_label'].isin(accepted)]
        doors_fractions_rejected[i] = Training_frame.loc[(Training_frame['doors'] == doors_possible_list[i]) & Training_frame['class_label'].isin(rejected)]
        doors_present_list[i] = Training_frame.loc[(Training_frame['doors'] == doors_possible_list[i])]
        #print(len(doors_fractions_accepted[i].index))
        #print(len(doors_fractions_rejected[i].index))
        info_doors+=float(len(doors_present_list[i].index)/total_count*entropy(len(doors_fractions_accepted[i].index), len(doors_fractions_rejected[i].index)))
    info_gain_doors = total_info - info_doors
    print(info_gain_doors)
    persons_fractions_accepted=[0,0,0]
    persons_fractions_rejected=[0,0,0]
    persons_present_list=[0,0,0]
    info_persons=0
    for i in range(0,3):
        persons_fractions_accepted[i] = Training_frame.loc[(Training_frame['persons'] == persons_possible_list[i]) & Training_frame['class_label'].isin(accepted)]
        persons_fractions_rejected[i] = Training_frame.loc[(Training_frame['persons'] == persons_possible_list[i]) & Training_frame['class_label'].isin(rejected)]
        persons_present_list[i] = Training_frame.loc[(Training_frame['persons'] == persons_possible_list[i])]
        #print(len(persons_fractions_accepted[i].index))
        #print(len(persons_fractions_rejected[i].index))
        info_persons+=float(len(persons_present_list[i].index)/total_count*entropy(len(persons_fractions_accepted[i].index), len(persons_fractions_rejected[i].index)))
    info_gain_persons = total_info - info_persons
    print(info_gain_persons)
    lug_boot_fractions_accepted=[0,0,0]
    lug_boot_fractions_rejected=[0,0,0]
    lug_boot_present_list=[0,0,0]
    info_lug_boot=0
    for i in range(0,3):
        lug_boot_fractions_accepted[i] = Training_frame.loc[(Training_frame['lug_boot'] == lug_boot_possible_list[i]) & Training_frame['class_label'].isin(accepted)]
        lug_boot_fractions_rejected[i] = Training_frame.loc[(Training_frame['lug_boot'] == lug_boot_possible_list[i]) & Training_frame['class_label'].isin(rejected)]
        lug_boot_present_list[i] = Training_frame.loc[(Training_frame['lug_boot'] == lug_boot_possible_list[i])]
        #print(len(lug_boot_fractions_accepted[i].index))
        #print(len(lug_boot_fractions_rejected[i].index))
        info_lug_boot+=float(len(lug_boot_present_list[i].index)/total_count*entropy(len(lug_boot_fractions_accepted[i].index), len(lug_boot_fractions_rejected[i].index)))
    info_gain_lug_boot = total_info - info_lug_boot
    print(info_gain_lug_boot)
    safety_fractions_accepted = [0,0,0]
    safety_fractions_rejected = [0,0,0]
    safety_present_list=[0,0,0]
    info_safety = 0
    for i in range(0,3):
        safety_fractions_accepted[i] = Training_frame.loc[(Training_frame['safety'] == safety_possible_list[i]) & Training_frame['class_label'].isin(accepted)]
        safety_fractions_rejected[i] = Training_frame.loc[(Training_frame['safety'] == safety_possible_list[i]) & Training_frame['class_label'].isin(rejected)]
        safety_present_list[i] = Training_frame.loc[(Training_frame['safety'] == safety_possible_list[i])]
        #print(len(safety_fractions_accepted[i].index))
        #print(len(safety_fractions_rejected[i].index))
        info_safety += float(len(safety_present_list[i].index) / total_count *entropy(len(safety_fractions_accepted[i].index), len(safety_fractions_rejected[i].index)))
    info_gain_safety = total_info - info_safety
    print(info_gain_safety)
information_gain()