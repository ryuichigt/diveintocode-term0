WEEK_LIST = ['月', '火', '水', '木', '金', '土', '日']
SUBJECT_LIST = ['Python', '数学', '機械学習', '深層学習','エンジニアプロジェクト']

def output_schedule(study_time_list):
    '''今週の勉強予定を出力します'''

    SUBJECT_LIST_INDEX = 1

    for week,schetule in zip(WEEK_LIST,study_time_list):
    	if schetule > 0:
    		print("{}曜日は、".format(week) + str(schetule)  + "時間勉強する予定です。")
    		
    		for times,i in zip(range(1,schetule+1),\
    			range(SUBJECT_LIST_INDEX , SUBJECT_LIST_INDEX + schetule)):
    			
    			print("{}限目".format(times) + SUBJECT_LIST[SUBJECT_LIST_INDEX % 5])
    			SUBJECT_LIST_INDEX += 1

    	else:
    		print("{}曜日は、".format(week) + "お休みです。")

def main():
    '''勉強情報をoutput_scheduleに渡します'''
    # 1日に何時間勉強するか（1週間　月曜日〜日曜日）
    study_time_list = [3, 1, 3, 0, 4, 2, 2]
    output_schedule(study_time_list)


if __name__ == '__main__':
    main()